import os
import random
import aiohttp

from src.configs.path_config import image_local_path
from src.configs.api_config import smms_token,smms_image_upload_history,ju_he_token,ju_he_image_list,anosu_url

"""本地图片"""
async def get_image_names():
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 定义常见的图片文件扩展名
    image_names = []
    for root, dirs, files in os.walk(image_local_path):
        for file in files:
            if any(file.endswith(ext) for ext in image_extensions):  # 检查文件是否是图片文件
                image_names.append(file)
    local_image_path = image_local_path + '/' + random.choice(image_names)  # 随机选取一张图片的路径
    return local_image_path

""" sm.ms  图床"""
async def get_smms_image_url():
    async with aiohttp.ClientSession() as session:
        async with session.get(smms_image_upload_history, headers={'Authorization': smms_token}, params={"page": "1"}) as response:
            data = await response.json()
            urls = [item['url'] for item in data.get('data', [])]
            random_url = random.choice(urls)
            return random_url

"""聚合图床"""
async def get_juhe_image_url():
    params = {"token": ju_he_token, "f": "json", "categories": "猫羽雫", "page": 1, "size": 400}
    async with aiohttp.ClientSession() as session:
        async with session.get(ju_he_image_list, params=params) as response:
            data = await response.json()
            random_url = random.choice(data.get('docs', [])).get('url')
            return random_url

"""
随机图api
"""
async def get_anosu_image(keyword: str, is_r18: int, num: int, proxy: str = "i.pixiv.re"):
    url = anosu_url + f"?keyword={keyword}&r18={is_r18}&num={num}&proxy={proxy}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            urls = [item['url'] for item in data]
            return urls