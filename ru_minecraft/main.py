from aiogram import executor
from .bot.core import dp


def main():
    executor.start_polling(dp, skip_updates=True)