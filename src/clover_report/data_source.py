import asyncio
import os
from datetime import datetime
import xml.etree.ElementTree as ET
from os import getcwd
from pathlib import Path
import httpx
from httpx import ConnectError, HTTPStatusError, Response, TimeoutException
from nonebot.log import logger
from nonebot_plugin_htmlrender import template_to_pic
import tenacity
from tenacity import retry, stop_after_attempt, wait_fixed
from zhdate import ZhDate
from .config import Anime, Hitokoto, SixData
from .date import get_festivals_dates
from src.configs.path_config import temp_path
from playwright.async_api import async_playwright


class AsyncHttpx:
    @classmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(1),
        retry=(
            tenacity.retry_if_exception_type(
                (TimeoutException, ConnectError, HTTPStatusError)
            )
        ),
    )
    async def get(cls, url: str) -> Response:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                response.raise_for_status()
                return response
            except (TimeoutException, ConnectError, HTTPStatusError) as e:
                logger.error(f"Request to {url} failed due to: {e}")
                raise

    @classmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(1),
        retry=(
            tenacity.retry_if_exception_type(
                (TimeoutException, ConnectError, HTTPStatusError)
            )
        ),
    )
    async def post(
        cls, url: str, data: dict[str, str], headers: dict[str, str]
    ) -> Response:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, data=data, headers=headers)
                response.raise_for_status()
                return response
            except (TimeoutException, ConnectError, HTTPStatusError) as e:
                logger.error(f"Request to {url} failed due to: {e}")
                raise


async def save_img(data: bytes):

    """
     保存日报图片
     :param data:
     :return:
     """
    file_path = temp_path + f"{datetime.now().date()}日报.png"
    with open(file_path, "wb") as file:
        file.write(data)


class Report:
    hitokoto_url = "https://v1.hitokoto.cn/?c=a"
    alapi_url = "https://v2.alapi.cn/api/zaobao"
    alapi_token = "48x3u7iqryztowlnwbnrwjucebzieu"
    six_url = "https://60s.viki.moe/?v2=1"
    game_url = "https://www.4gamers.com.tw/rss/latest-news"
    bili_url = "https://s.search.bilibili.com/main/hotword"
    it_url = "https://www.ithome.com/rss/"
    anime_url = "https://api.bgm.tv/calendar"


    week = {  # noqa: RUF012
        0: "一",
        1: "二",
        2: "三",
        3: "四",
        4: "五",
        5: "六",
        6: "日",
    }

    @classmethod
    async def get_report_image(cls) -> bytes:
        """获取数据"""
        now = datetime.now()
        file = Path() / temp_path / f"{now.date()}日报.png"
        if os.path.exists(file):
            with file.open("rb") as image_file:
                return image_file.read()
        zhdata = ZhDate.from_datetime(now)
        result = await asyncio.gather(
            *[
                cls.get_hitokoto(),
                cls.get_bili(),
                cls.get_six(),
                cls.get_anime(),
                cls.get_it(),
            ]
        )
        data = {
            "data_festival": get_festivals_dates(),
            "data_hitokoto": result[0],
            "data_bili": result[1],
            "data_six": result[2],
            "data_anime": result[3],
            "data_it": result[4],
            "week": cls.week[now.weekday()],
            "date": now.date(),
            "zh_date": zhdata.chinese().split()[0][5:],
            "full_show": True,
        }
        async with async_playwright() as p:
            browser = await p.chromium.launch()

        image_bytes = await template_to_pic(
            template_path=getcwd() + "/src/clover_report/daily_report",
            template_name="main.html",
            templates={"data": data},
            pages={
                "viewport": {"width": 578, "height": 1885},
                "base_url": f"file://{getcwd()}",
            },
            wait=2,
        )
        await save_img(image_bytes)
        await browser.close()
        return image_bytes

    @classmethod
    async def get_hitokoto(cls) -> str:
        """获取一言"""
        res = await AsyncHttpx.get(cls.hitokoto_url)
        data = Hitokoto(**res.json())
        return data.hitokoto

    @classmethod
    async def get_bili(cls) -> list[str]:
        """获取哔哩哔哩热搜"""
        res = await AsyncHttpx.get(cls.bili_url)
        data = res.json()
        return [item["keyword"] for item in data["list"]]

    @classmethod
    async def get_alapi_data(cls) -> list[str]:
        """获取alapi数据"""
        payload = {"token": cls.alapi_token, "format": "json"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = await AsyncHttpx.post(cls.alapi_url, data=payload, headers=headers)
        if res.status_code != 200:
            return ["Error: Unable to fetch data"]
        data = res.json()
        news_items = data.get("data", {}).get("news", [])
        return news_items[:11] if len(news_items) > 11 else news_items

    @classmethod
    async def get_six(cls) -> list[str]:
        """获取60s数据"""
        if True:
            return await cls.get_alapi_data()
        res = await AsyncHttpx.get(cls.six_url)
        data = SixData(**res.json())
        return data.data.news[:11] if len(
            data.data.news) > 11 else data.data.news

    @classmethod
    async def get_it(cls) -> list[str]:
        """获取it数据"""
        res = await AsyncHttpx.get(cls.it_url)
        root = ET.fromstring(res.text)
        titles = []
        for item in root.findall("./channel/item"):
            title_element = item.find("title")
            if title_element is not None:
                titles.append(title_element.text)
        return titles[:11] if len(titles) > 11 else titles

    @classmethod
    async def get_anime(cls) -> list[tuple[str, str]]:
        """获取动漫数据"""
        res = await AsyncHttpx.get(cls.anime_url)
        data_list = []
        week = datetime.now().weekday()
        try:
            anime = Anime(**res.json()[week])
        except IndexError:
            anime = Anime(**res.json()[-1])
        data_list.extend(
            (data.name_cn or data.name, data.image) for data in anime.items
        )
        return data_list[:8] if len(data_list) > 8 else data_list
