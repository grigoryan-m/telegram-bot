from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import SOCIALS_URL
from locales.texts import t
from utils.keyboards import socials_keyboard
from utils.user_data import get_lang
from utils.analytics import track

router = Router()


@router.callback_query(F.data == "menu:socials")
async def socials(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    await track(callback.from_user.id, "socials_opened", lang)
    await callback.message.answer(
        t(lang, "socials_text"),
        reply_markup=socials_keyboard(lang, SOCIALS_URL),
        parse_mode="Markdown"
    )
    await callback.answer()
