import re
import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states import LoyaltyState
from locales.texts import t
from utils.keyboards import back_to_menu_keyboard
from utils.user_data import get_lang
from utils.otp import generate_otp, verify_otp, send_otp_sms
from utils.odoo import create_or_update_customer, find_customer_by_phone
from utils.analytics import track

router = Router()
logger = logging.getLogger(__name__)

PHONE_REGEX = re.compile(r"^\+?[1-9]\d{7,14}$")


@router.callback_query(F.data == "menu:loyalty")
async def loyalty_start(callback: CallbackQuery, state: FSMContext):
    lang = get_lang(callback.from_user.id)
    await track(callback.from_user.id, "loyalty_started", lang)
    await state.set_state(LoyaltyState.phone)
    await callback.message.answer(
        t(lang, "loyalty_start"),
        parse_mode="Markdown"
    )
    await callback.answer()


@router.message(LoyaltyState.phone)
async def process_phone(message: Message, state: FSMContext):
    lang = get_lang(message.from_user.id)
    phone = message.text.strip().replace(" ", "").replace("-", "")

    if not PHONE_REGEX.match(phone):
        await message.answer(t(lang, "loyalty_phone_invalid"))
        return

    if not phone.startswith("+"):
        phone = "+" + phone

    await state.update_data(phone=phone)

    otp = generate_otp(phone)
    send_otp_sms(phone, otp)

    await state.set_state(LoyaltyState.otp)
    await message.answer(
        t(lang, "loyalty_otp_sent", phone=phone),
        parse_mode="Markdown"
    )


@router.message(LoyaltyState.otp)
async def process_otp(message: Message, state: FSMContext):
    lang = get_lang(message.from_user.id)
    data = await state.get_data()
    phone = data.get("phone", "")
    entered = message.text.strip()

    success, reason = verify_otp(phone, entered)

    if not success:
        if reason == "too_many":
            await state.clear()
            await message.answer(t(lang, "loyalty_otp_attempts"))
        else:
            await message.answer(t(lang, "loyalty_otp_invalid"))
        return

    await state.set_state(LoyaltyState.age)
    await message.answer(t(lang, "loyalty_ask_age"))


@router.message(LoyaltyState.age)
async def process_age(message: Message, state: FSMContext):
    lang = get_lang(message.from_user.id)
    try:
        age = int(message.text.strip())
        if not (1 <= age <= 120):
            raise ValueError
    except ValueError:
        await message.answer(t(lang, "loyalty_age_invalid"))
        return

    await state.update_data(age=age)
    await state.set_state(LoyaltyState.country)
    await message.answer(t(lang, "loyalty_ask_country"))


@router.message(LoyaltyState.country)
async def process_country(message: Message, state: FSMContext):
    lang = get_lang(message.from_user.id)
    country = message.text.strip()
    data = await state.get_data()

    phone = data["phone"]
    age = data["age"]
    messenger_id = str(message.from_user.id)

    await message.answer("⏳ Processing...")

    result = create_or_update_customer(
        phone=phone,
        age=age,
        country=country,
        messenger_id=messenger_id,
        messenger_type="telegram"
    )

    await state.clear()

    if not result:
        await track(message.from_user.id, "loyalty_error", lang)
        await message.answer(
            t(lang, "loyalty_crm_error"),
            reply_markup=back_to_menu_keyboard(lang)
        )
        return

    client_id = result["client_id"]
    barcode = result["barcode"]
    is_new = result["is_new"]

    await track(
        message.from_user.id, "loyalty_completed", lang,
        {"is_new": is_new, "country": country}
    )

    text_key = "loyalty_success" if is_new else "loyalty_already_exists"
    await message.answer(
        t(lang, text_key, client_id=client_id, phone=phone, barcode=barcode),
        reply_markup=back_to_menu_keyboard(lang),
        parse_mode="Markdown"
    )
