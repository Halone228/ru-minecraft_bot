from aiogram.types import (
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup
)
from .texts import *

GREET_KB = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=KB_START_VIEW)],
    [KeyboardButton(text=KB_SET_TYPE), KeyboardButton(text=KB_SET_VERSION)]
],
    resize_keyboard=True
)


def keyboard_for_view(url):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Ссылка на мод.', url=url)],
            [InlineKeyboardButton(text='Следующий мод.', callback_data='next')]
        ]
    )