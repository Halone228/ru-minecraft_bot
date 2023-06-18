from aiogram.dispatcher.filters import Text
from .core import *
from .helpers import *
from .texts import *


@dp.message_handler(Text(equals=KB_SET_TYPE))
async def set_type(message: types.Message):
    types_kb = to_inline_kb(to_arr(get_types()), 'stype')
    await message.answer(SELECT_TYPE, reply_markup=InlineKeyboardMarkup(
        inline_keyboard=list(chunks(types_kb, 4))
    ))


@dp.callback_query_handler(lambda query: query.data.startswith('stype'))
async def set_type(query: types.CallbackQuery):
    user = get_user(query.from_user.id)
    __type = query.data.replace('stype', '')
    await query.answer(SUCCESS, show_alert=True)
    user.mod_type = __type
    user.save()


@dp.message_handler(Text(equals=KB_SET_VERSION))
async def set_type(message: types.Message):
    ver_kb = to_inline_kb(to_arr(get_versions()), 'sver')
    await message.answer(SELECT_VER, reply_markup=InlineKeyboardMarkup(
        inline_keyboard=list(chunks(ver_kb, 4))
    ))


@dp.callback_query_handler(lambda query: query.data.startswith('sver'))
async def set_type(query: types.CallbackQuery):
    user = get_user(query.from_user.id)
    ver = query.data.replace('sver', '')
    await query.answer(SUCCESS, show_alert=True)
    user.version = ver
    user.save()


