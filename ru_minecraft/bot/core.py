from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types

__all__ = [
    'bot',
    'dp',
    'types'
]

bot = Bot('',parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
