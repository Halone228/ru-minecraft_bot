from requests import get
from bs4 import BeautifulSoup, Tag
from ru_minecraft.config import BASE_URL
from time import sleep
from json import dump


def save_ver_and_type():
    while True:
        response = get(BASE_URL.geturl())
        if response.status_code == 200:
            break
        sleep(2)

    soup = BeautifulSoup(response.text, 'lxml')
    ver = list(soup.select('div.category-menu--versions>div.category-menu__links>a'))[1:]
    types = list(soup.select('div.category-menu--categories>div.category-menu__links>a'))[1:]

    def to_dict(__list: list[Tag]):
        result = {}
        for i in __list:
            result[i.text.strip()] = i.get('href').replace('/mody-minecraft/','').replace('/','')
        return result

    ver_dict = to_dict(ver)
    types_dict = to_dict(types)
    with open('ver.json', 'w', encoding='utf-8') as f:
        dump(ver_dict, f)

    with open('types.json', 'w', encoding='utf-8') as f:
        dump(types_dict, f)
