from .core import *
from .texts import *
from .keyboard import *


@dp.message_handler(commands=['start', 'help'])
async def greet_message(message: types.Message):
    await message.answer(GREET, reply_markup=GREET_KB)
