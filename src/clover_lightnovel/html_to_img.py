import os
from datetime import datetime
from os import getcwd
from pathlib import Path

from nonebot_plugin_htmlrender import template_to_pic
from playwright.async_api import async_playwright

from src.configs.path_config import temp_path
import src.clover_lightnovel.wenku8 as Wenku8


async def save_img(data: bytes):

    """
     保存日报图片
     :param data:
     :return:
     """
    file_path = temp_path + f"{datetime.now().date()}轻小说.png"
    with open(file_path, "wb") as file:
        file.write(data)

async def get_ln_image():
    now = datetime.now()
    file = os.path.join(temp_path , f"{now.date()}轻小说.png")
    if os.path.exists(file):
        with open(file,"rb") as image_file:
            return image_file.read()

    await Wenku8.login()
    await Wenku8.get_books()

    async with async_playwright() as p:
        browser = await p.chromium.launch()

    image_bytes = await template_to_pic(
        template_path=getcwd() + "/src/clover_lightnovel/",
        template_name="output1.html",
        templates={"data": None},
        pages={
            "viewport": {"width": 578, "height": 578},
            "base_url": f"file://{getcwd()}",
        },
        wait=2,
    )
    await save_img(image_bytes)
    await browser.close()
    return image_bytes


