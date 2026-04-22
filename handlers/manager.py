import logging
from datetime import datetime, timezone, timedelta
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from config import MANAGER_CHAT_ID, MANAGER_WORK_START, MANAGER_WORK_END
from states import ManagerState
from locales.texts import t
from utils.keyboards import manager_keyboard, back_to_menu_keyboard
from utils.user_data import get_lang
from utils.ai import ask_ai
from utils.analytics import track

router = Router()
logger = logging.getLogger(__name__)

TZ_OFFSET = timedelta(hours=7)  # UTC+7 (Bangkok). Change for your timezone.


def is_manager_online() -> bool:
    now = datetime.now(tz=timezone(TZ_OFFSET))
    return MANAGER_WORK_START <= now.hour < MANAGER_WORK_END


@router.callback_query(F.data == "menu:manager")
async def manager_start(callback: CallbackQuery, state: FSMContext):
    lang = get_lang(callback.from_user.id)
    await track(callback.from_user.id, "manager_started", lang)
    await state.set_state(ManagerState.chatting)

    if not is_manager_online():
        await callback.message.answer(
            t(lang, "manager_offline"),
            reply_markup=back_to_menu_keyboard(lang),
            parse_mode="Markdown"
        )
    else:
        await callback.message.answer(
            t(lang, "manager_hello"),
            reply_markup=manager_keyboard(lang),
            parse_mode="Markdown"
        )
    await callback.answer()


@router.callback_query(F.data == "manager:transfer")
async def transfer_to_manager(callback: CallbackQuery, state: FSMContext, bot: Bot):
    lang = get_lang(callback.from_user.id)
    await track(callback.from_user.id, "manager_transferred", lang)
    await callback.message.answer(t(lang, "manager_transfer"))
    await _notify_manager(bot, callback.from_user, "User requested human agent.", lang)
    await callback.message.answer(
        t(lang, "manager_transferred"),
        reply_markup=back_to_menu_keyboard(lang)
    )
    await state.clear()
    await callback.answer()


@router.message(ManagerState.chatting)
async def handle_user_message(message: Message, state: FSMContext, bot: Bot):
    lang = get_lang(message.from_user.id)
    user_text = message.text or ""

    if not is_manager_online():
        await _notify_manager(bot, message.from_user, user_text, lang)
        await track(message.from_user.id, "manager_message_left", lang)
        await message.answer(
            t(lang, "manager_left_message"),
            reply_markup=back_to_menu_keyboard(lang)
        )
        await state.clear()
        return

    # Try AI first
    ai_response = await ask_ai(user_text, lang)

    if "[TRANSFER_TO_HUMAN]" in ai_response:
        await message.answer(t(lang, "manager_transfer"))
        await _notify_manager(bot, message.from_user, user_text, lang)
        await track(message.from_user.id, "manager_transferred", lang, {"trigger": "ai_escalation"})
        await message.answer(
            t(lang, "manager_transferred"),
            reply_markup=back_to_menu_keyboard(lang)
        )
        await state.clear()
    else:
        await message.answer(
            ai_response,
            reply_markup=manager_keyboard(lang),
        )


async def _notify_manager(bot: Bot, user, user_text: str, lang: str):
    if not MANAGER_CHAT_ID:
        logger.warning("MANAGER_CHAT_ID not set, cannot notify manager")
        return
    try:
        username = f"@{user.username}" if user.username else f"ID:{user.id}"
        text = (
            f"🔔 *New message from user*\n"
            f"User: {username} (lang: {lang})\n\n"
            f"Message:\n{user_text}"
        )
        await bot.send_message(MANAGER_CHAT_ID, text, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Failed to notify manager: {e}")
