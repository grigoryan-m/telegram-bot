from typing import Dict

# Simple in-memory store. For production use Redis or DB.
_user_lang: Dict[int, str] = {}


def get_lang(user_id: int) -> str:
    return _user_lang.get(user_id, "en")


def set_lang(user_id: int, lang: str) -> None:
    _user_lang[user_id] = lang
