from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from locales.texts import t
from utils.keyboards import language_keyboard, main_menu_keyboard
from utils.user_data import get_lang, set_lang
from utils.analytics import track

from utils.reminders import start_reminder, cancel_reminder

router = Router()


async def show_main_menu(message: Message, lang: str):
    await message.answer(
        t(lang, "main_menu"),
        reply_markup=main_menu_keyboard(lang),
        parse_mode="Markdown"
    )
    cancel_reminder(message.chat.id)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    lang = get_lang(message.from_user.id)
    await track(message.from_user.id, "bot_started", lang)
    await message.answer(
        t(lang, "welcome"),
        reply_markup=language_keyboard()
    )


@router.message(Command("menu"))
async def cmd_menu(message: Message, state: FSMContext):
    await state.clear()
    lang = get_lang(message.from_user.id)
    await track(message.from_user.id, "menu_opened", lang)
    await show_main_menu(message, lang)


@router.message(Command("language"))
async def cmd_language(message: Message):
    lang = get_lang(message.from_user.id)
    await message.answer(t(lang, "welcome"), reply_markup=language_keyboard())


@router.callback_query(F.data.startswith("lang:"))
async def set_language(callback: CallbackQuery):
    lang = callback.data.split(":")[1]
    set_lang(callback.from_user.id, lang)
    await track(callback.from_user.id, "language_selected", lang, {"selected_lang": lang})
    await callback.message.edit_text(t(lang, "lang_set"))
    await callback.message.answer(
        t(lang, "loyalty_hint"),
        reply_markup=main_menu_keyboard(lang),
        parse_mode="Markdown"
    )
    start_reminder(
        callback.bot,
        callback.message.chat.id,
        lang,
        name="loyalty5m",
        delay=300,
        text_key="loyalty5m_reminder"
    )
    start_reminder(
        callback.bot,
        callback.message.chat.id,
        lang,
        name="loyalty2h",
        delay=7200,
        text_key="loyalty_reminder"
    )
    start_reminder(
        callback.bot,
        callback.message.chat.id,
        lang,
        name="loyalty24h",
        delay=86400,
        text_key="loyalty24h_reminder"
    )
    await callback.answer()


@router.callback_query(F.data == "menu:main")
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    lang = get_lang(callback.from_user.id)
    await callback.message.answer(
        t(lang, "main_menu"),
        reply_markup=main_menu_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()


@router.callback_query(F.data == "menu:lang")
async def change_lang_callback(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    await callback.message.answer(t(lang, "welcome"), reply_markup=language_keyboard())
    await callback.answer()
