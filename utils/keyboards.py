from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from locales.texts import t


def language_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="🇬🇧 English", callback_data="lang:en")
    builder.button(text="🇷🇺 Русский", callback_data="lang:ru")
    builder.button(text="🇹🇭 ภาษาไทย", callback_data="lang:th")
    builder.adjust(1)
    return builder.as_markup()


def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_stores"), callback_data="menu:stores")
    builder.button(text=t(lang, "btn_loyalty"), callback_data="menu:loyalty")
    builder.button(text=t(lang, "btn_manager"), callback_data="menu:manager")
    builder.button(text=t(lang, "btn_about"), callback_data="menu:about")
    builder.button(text=t(lang, "btn_socials"), callback_data="menu:socials")
    builder.button(text=t(lang, "btn_change_lang"), callback_data="menu:lang")
    builder.adjust(1)
    return builder.as_markup()


def back_to_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_main_menu"), callback_data="menu:main")
    return builder.as_markup()


def geo_keyboard(lang: str) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=t(lang, "btn_send_geo"), request_location=True)
    builder.button(text=t(lang, "btn_choose_region"))
    builder.button(text=t(lang, "btn_main_menu"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def regions_keyboard(lang: str) -> InlineKeyboardMarkup:
    # TODO: заменить на реальные регионы из базы магазинов
    regions = ["Bangkok", "Phuket", "Chiang Mai", "Pattaya", "Moscow", "Saint Petersburg"]
    builder = InlineKeyboardBuilder()
    for region in regions:
        builder.button(text=region, callback_data=f"region:{region}")
    builder.button(text=t(lang, "btn_back"), callback_data="menu:stores")
    builder.adjust(2)
    return builder.as_markup()


def store_maps_button(name: str, lat: float, lon: float, lang: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    maps_url = f"https://www.google.com/maps?q={lat},{lon}"
    builder.button(text=t(lang, "btn_open_maps"), url=maps_url)
    return builder.as_markup()


def manager_keyboard(lang: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_transfer_manager"), callback_data="manager:transfer")
    builder.button(text=t(lang, "btn_main_menu"), callback_data="menu:main")
    builder.adjust(1)
    return builder.as_markup()


def remove_keyboard() -> ReplyKeyboardRemove:
    return ReplyKeyboardRemove()


def socials_keyboard(lang: str, url: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_open_socials"), url=url)
    builder.button(text=t(lang, "btn_main_menu"), callback_data="menu:main")
    builder.adjust(1)
    return builder.as_markup()
