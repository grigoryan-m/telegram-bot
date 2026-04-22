from aiogram.fsm.state import State, StatesGroup


class LanguageState(StatesGroup):
    choosing = State()


class LoyaltyState(StatesGroup):
    phone = State()
    otp = State()
    age = State()
    country = State()


class StoreState(StatesGroup):
    waiting_geo = State()
    choosing_region = State()


class ManagerState(StatesGroup):
    chatting = State()
