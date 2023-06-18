import time

import bs4
import loguru

from ru_minecraft.config import BASE_URL
from requests import Session
from dataclasses import dataclass


@dataclass(slots=True)
class Mod:
    name: str
    description: str
    # versions: dict[str, str]
    url: str
    icon_url: str


class RuMinecraftSession:
    def __init__(self, __type: str = '', ver: str = ''):
        __url = BASE_URL.geturl()
        if __type:
            __type += '/'
        if ver:
            ver += '/'
        self.page = 1
        self.url = f"{__url}/{__type}{ver}page/{self.page}"
        loguru.logger.info(self.url)
        self.items = []
        self.session = Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/112.0.0.0 YaBrowser/23.5.1.721 Yowser/2.5 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.7'
        }
        self.session.get('https://yandex.by/search/?text=minecraft+mods&lr=202352&clid=2595562-900&win=586')

    def update_page(self):
        self.url = self.url.replace(f'page/{self.page-1}', f'page/{self.page}')

    def parse_page(self):
        while True:
            response = self.session.get(self.url)
            if response.status_code == 200:
                break
            loguru.logger.error(response.text)
            time.sleep(5)

        soup = bs4.BeautifulSoup(response.text, 'lxml')
        __content = soup.find('div', id='dle-content')
        items = __content.find_all('div', class_='news2')
        for i in items:
            header = i.find('h2')
            name = header.text.strip()
            main_news = i.find('div', class_='main-news2')
            img_src = main_news.find('img').get('src')
            description = main_news.find('span').text
            url = header.find('a').get('href')
            self.items.append(Mod(
                name=name,
                description=description,
                icon_url=img_src,
                url=url
            ))

    def need_update(self) -> bool:
        return len(self.items) <= 1

    def pop_item(self) -> Mod:
        if not self.need_update():
            return self.items.pop(0)

        self.page += 1
        self.update_page()
        self.parse_page()

        return self.items.pop(0)
