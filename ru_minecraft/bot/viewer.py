from .core import *
from .texts import *
from .helpers import get_user, get_versions, get_types
from .keyboard import keyboard_for_view
from ru_minecraft.parser.view_session import RuMinecraftSession
from aiogram.dispatcher.filters import Text
import asyncio

sessions: dict[int, RuMinecraftSession] = {}


@dp.message_handler(Text(equals=KB_START_VIEW))
async def start_view(message: types.Message):
    user = get_user(message.from_user.id)
    sessions[message.from_user.id] = RuMinecraftSession(user.mod_type, user.version)
    await message.answer(WAIT())
    sessions[message.from_user.id].parse_page()
    await message.answer(SELECTED([k for k,i in get_versions().items() if i == user.version][-1]
                                  , [k for k,i in get_types().items() if i == user.mod_type][-1]))
    item = sessions[message.from_user.id].pop_item()
    await message.answer_photo(
        photo=item.icon_url,
        caption=MOD_INFO(item.name, item.description),
        reply_markup=keyboard_for_view(item.url)
    )


@dp.callback_query_handler(lambda query: query.data == 'next')
async def next_mod(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if sessions[user_id].need_update():
        await bot.send_message(callback.message.chat.id, WAIT())
    item = sessions[user_id].pop_item()

    await asyncio.gather(
        callback.message.edit_media(media=types.input_media.InputMediaPhoto(media=item.icon_url)),
        callback.message.edit_caption(MOD_INFO(item.name, item.description), reply_markup=keyboard_for_view(item.url))
    )
