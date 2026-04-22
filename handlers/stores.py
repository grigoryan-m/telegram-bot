import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states import StoreState
from locales.texts import t
from utils.keyboards import geo_keyboard, regions_keyboard, store_maps_button, back_to_menu_keyboard, remove_keyboard
from utils.user_data import get_lang
from utils import stores as store_utils
from utils.analytics import track

router = Router()
logger = logging.getLogger(__name__)


@router.callback_query(F.data == "menu:stores")
async def stores_start(callback: CallbackQuery, state: FSMContext):
    lang = get_lang(callback.from_user.id)
    await state.set_state(StoreState.waiting_geo)
    await callback.message.answer(
        t(lang, "stores_request_geo"),
        reply_markup=geo_keyboard(lang),
        parse_mode="Markdown"
    )
    await callback.answer()


@router.message(StoreState.waiting_geo, F.location)
async def handle_location(message: Message, state: FSMContext):
    lang = get_lang(message.from_user.id)
    lat = message.location.latitude
    lon = message.location.longitude

    await track(message.from_user.id, "store_search_geo", lang, {"lat": lat, "lon": lon})
    found = store_utils.find_stores_by_location(lat, lon)
    await state.clear()
    await _send_store_results(message, found, lang)


@router.message(StoreState.waiting_geo, F.text)
async def handle_geo_text(message: Message, state: FSMContext):
    lang = get_lang(message.from_user.id)
    text = message.text.strip()

    if text == t(lang, "btn_choose_region"):
        await state.set_state(StoreState.choosing_region)
        await message.answer(
            t(lang, "stores_choose_region"),
            reply_markup=regions_keyboard(lang)
        )
    elif text == t(lang, "btn_main_menu"):
        await state.clear()
        from handlers.start import show_main_menu
        from utils.keyboards import main_menu_keyboard
        await message.answer("...", reply_markup=remove_keyboard())
        await show_main_menu(message, lang)


@router.callback_query(F.data.startswith("region:"))
async def handle_region(callback: CallbackQuery, state: FSMContext):
    lang = get_lang(callback.from_user.id)
    region = callback.data.split(":", 1)[1]
    await track(callback.from_user.id, "store_search_region", lang, {"region": region})
    found = store_utils.find_stores_by_region(region)
    await state.clear()
    await _send_store_results(callback.message, found, lang)
    await callback.answer()


async def _send_store_results(message: Message, stores: list, lang: str):
    if not stores:
        await message.answer(
            t(lang, "stores_not_found"),
            reply_markup=back_to_menu_keyboard(lang)
        )
        return

    await message.answer(
        t(lang, "stores_result", count=len(stores)),
        parse_mode="Markdown"
    )

    for store in stores:
        card = t(lang, "store_card",
                 name=store["name"],
                 address=store["address"],
                 hours=store["hours"])
        dist = store.get("distance_km")
        if dist is not None:
            card += f"📏 {dist} km away"

        await message.answer(
            card,
            reply_markup=store_maps_button(store["name"], store["lat"], store["lon"], lang),
            parse_mode="Markdown"
        )

    await message.answer(
        t(lang, "main_menu"),
        reply_markup=back_to_menu_keyboard(lang),
        parse_mode="Markdown"
    )
