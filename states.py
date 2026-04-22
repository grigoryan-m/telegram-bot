from aiogram.fsm.state import State, StatesGroup


class LanguageState(StatesGroup):
    choosing = State()


class LoyaltyState(StatesGroup):
    phone = State()
    otp = State()
    name = State()        # NEW: full name
    country = State()
    tourist = State()     # NEW: yes/no inline keyboard
    thai_citizen = State()  # NEW: yes/no inline keyboard


class StoreState(StatesGroup):
    waiting_geo = State()
    choosing_region = State()


class ManagerState(StatesGroup):
    chatting = State()
