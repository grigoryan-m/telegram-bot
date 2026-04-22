from aiogram import Router, F
from aiogram.types import CallbackQuery

from locales.texts import t
from utils.keyboards import back_to_menu_keyboard
from utils.user_data import get_lang
from utils.analytics import track

router = Router()


@router.callback_query(F.data == "menu:about")
async def about(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    await track(callback.from_user.id, "about_opened", lang)
    await callback.message.answer(
        t(lang, "about_text"),
        reply_markup=back_to_menu_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()
