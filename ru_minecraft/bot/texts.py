from random import choice
from aiogram.utils.markdown import hbold
KB_SET_VERSION = 'Указать желаемую версию'
KB_SET_TYPE = 'Указать желаемую тематику'
KB_START_VIEW = 'Начать просмотр модов'
GREET = 'Рады приветствовать в нашем боте!'
SELECT_TYPE = 'Выберите тематику'
SELECT_VER = 'Выберите версию'
SUCCESS = 'Успешно!'
SELECTED = lambda ver, type: f"Выбранная тематика: {type if type else 'Не выбрано'}\n" \
                             f"Выбранная версия: {ver if ver else 'Не выбрано'}\n" \
                             f"Если вы хотите поменять тематику и/или версию, то сделайте это и начните просмотр снова."


def WAIT():
    return choice(
        [
            "Получаем информацию с космоса, подождите...",
            "Илон маск отправляет нам список рекомендаций, подождите...",
            "Советуемся с Джефом Безосом, подождите...",
            "Взламываем инстаграм, чтобы узнать ваши рекомендации, подождите..."
        ]
    )


MOD_INFO = lambda title, description: f"{hbold(title)}\n{description}"