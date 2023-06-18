from ru_minecraft.database import UserSettings
from functools import lru_cache
from json import load
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_user(user_id: int) -> UserSettings:
    user, _ = UserSettings.get_or_create(user_id=user_id)
    return user


@lru_cache
def get_versions() -> dict:
    with open('ver.json', 'r', encoding='utf-8') as f:
        return load(f)


@lru_cache
def get_types() -> dict:
    with open('types.json', 'r', encoding='utf-8') as f:
        return load(f)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def to_arr(i: dict):
    return [(key, value) for key, value in i.items()]


def to_inline_kb(arr: list[tuple], data_prefix: str):
    return [InlineKeyboardButton(text=i[0], callback_data=f'{data_prefix}{i[1]}') for i in arr]
