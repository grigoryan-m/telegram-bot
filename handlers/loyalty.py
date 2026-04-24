import re
import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from states import LoyaltyState
from locales.texts import t
from utils.keyboards import back_to_menu_keyboard
from utils.user_data import get_lang
from utils.otp import generate_otp, verify_otp, send_otp_sms
from utils.odoo import register_customer
from utils.analytics import track
import json

from utils.reminders import start_reminder, cancel_reminder
router = Router()
logger = logging.getLogger(__name__)

PHONE_REGEX = re.compile(r"^\+?[1-9]\d{7,14}$")


def _yes_no_keyboard(lang: str, yes_cb: str, no_cb: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=t(lang, "btn_yes"), callback_data=yes_cb),
        InlineKeyboardButton(text=t(lang, "btn_no"),  callback_data=no_cb),
    ]])


# ──────────────────────────────────────────────────────────
# Step 1: entry — ask for phone
# ──────────────────────────────────────────────────────────
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
    cancel_reminder(
        callback.message.chat.id,
        "loyalty5m"
    )


# ──────────────────────────────────────────────────────────
# Step 2: validate phone → send OTP
# ──────────────────────────────────────────────────────────
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

    start_reminder

    await state.set_state(LoyaltyState.otp)
    await message.answer(
        t(lang, "loyalty_otp_sent", phone=phone),
        parse_mode="Markdown"
    )
    start_reminder(
        message.bot,
        message.chat.id,
        lang,
        name="after_phone_reminder",
        delay=300,
        text_key="after_phone_reminder"
    )


# ──────────────────────────────────────────────────────────
# Step 3: verify OTP → ask full name
# ──────────────────────────────────────────────────────────
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

    await state.set_state(LoyaltyState.name)
    await message.answer(t(lang, "loyalty_ask_name"))


# ──────────────────────────────────────────────────────────
# Step 4: save name → ask country
# ──────────────────────────────────────────────────────────
@router.message(LoyaltyState.name)
async def process_name(message: Message, state: FSMContext):
    lang = get_lang(message.from_user.id)
    name = message.text.strip()

    if len(name) < 2:
        await message.answer(t(lang, "loyalty_name_invalid"))
        return

    await state.update_data(name=name)
    await state.set_state(LoyaltyState.country)
    await message.answer(t(lang, "loyalty_ask_country"))


# ──────────────────────────────────────────────────────────
# Step 5: save country → ask tourist?
# ──────────────────────────────────────────────────────────
@router.message(LoyaltyState.country)
async def process_country(message: Message, state: FSMContext):
    lang = get_lang(message.from_user.id)
    country = message.text.strip()
    await state.update_data(country=country)
    await state.set_state(LoyaltyState.tourist)
    await message.answer(
        t(lang, "loyalty_ask_tourist"),
        reply_markup=_yes_no_keyboard(lang, "tourist:yes", "tourist:no")
    )


# ──────────────────────────────────────────────────────────
# Step 6: tourist answer → ask thai_citizen?
# ──────────────────────────────────────────────────────────
@router.callback_query(F.data.in_({"tourist:yes", "tourist:no"}))
async def process_tourist(callback: CallbackQuery, state: FSMContext):
    lang = get_lang(callback.from_user.id)
    tourist = callback.data == "tourist:yes"
    await state.update_data(tourist=tourist)

    if tourist:
        # tourists can't be Thai citizens — skip that question
        await state.update_data(thai_citizen=False)
        await _finalize(callback.message, state, lang)
    else:
        await state.set_state(LoyaltyState.thai_citizen)
        await callback.message.answer(
            t(lang, "loyalty_ask_thai_citizen"),
            reply_markup=_yes_no_keyboard(lang, "thai_citizen:yes", "thai_citizen:no")
        )

    await callback.answer()


# ──────────────────────────────────────────────────────────
# Step 7: thai_citizen answer → call API
# ──────────────────────────────────────────────────────────
@router.callback_query(F.data.in_({"thai_citizen:yes", "thai_citizen:no"}))
async def process_thai_citizen(callback: CallbackQuery, state: FSMContext):
    lang = get_lang(callback.from_user.id)
    thai_citizen = callback.data == "thai_citizen:yes"
    await state.update_data(thai_citizen=thai_citizen)
    await _finalize(callback.message, state, lang)
    await callback.answer()


# ──────────────────────────────────────────────────────────
# Final: call API, show result
# ──────────────────────────────────────────────────────────
async def _finalize(message: Message, state: FSMContext, lang: str):
    data = await state.get_data()
    await state.clear()

    phone = data["phone"]
    name = data["name"]
    country = data.get("country")
    tourist = data.get("tourist", False)
    thai_citizen = data.get("thai_citizen", False)

    await message.answer(t(lang, "loading"))

    result = register_customer(
        name=name,
        phone=phone,
        lang=lang,
        tourist=tourist,
        thai_citizen=thai_citizen,
        country=country,
        bot_platform="telegram",
    )

    if result is None:
        await track(message.chat.id, "loyalty_error", lang)
        await message.answer(
            t(lang, "loyalty_crm_error"),
            reply_markup=back_to_menu_keyboard(lang)
        )
        return

    messages = result.get("content", {}).get("messages", [])

    api_message = None
    barcode = None

    for msg in messages:
        if msg.get("type") == "text":
            api_message = msg.get("text")
        elif msg.get("type") == "image":
            barcode = msg.get("url")
            
    # Cancel loyalty reminder:
    cancel_reminder(message.chat.id, "loyalty2h")
    cancel_reminder(message.chat.id, "after_phone_reminder")
    cancel_reminder(message.chat.id, "loyalty24h")
    if api_message:
        # Trust the Odoo-formatted message (already localised by the API)
        await track(message.chat.id, "loyalty_completed", lang)
        await message.answer(
            api_message,
            reply_markup=back_to_menu_keyboard(lang),
            parse_mode="Markdown"
        )
    if barcode:
        await message.answer_photo(barcode)
    else:
        # Unexpected shape — log and show generic error
        logger.error(f"Unexpected Odoo API response: {result}")
        await message.answer(
            t(lang, "loyalty_crm_error"),
            reply_markup=back_to_menu_keyboard(lang)
        )
