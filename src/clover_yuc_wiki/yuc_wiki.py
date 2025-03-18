import os
from pathlib import Path
import requests
from os import getcwd
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
from nonebot_plugin_htmlrender import template_to_pic
from src.configs.path_config import yuc_wiki_path

base_url = "https://yuc.wiki/"
new =  "https://yuc.wiki/new"

async def get_yuc_wiki(keyword):
    """
    获取当季动漫
    """
    template_name,response = '',''
    try:
        if keyword == '本季新番':
            template_name = await generate_season_url()
            response = requests.get(base_url + f'{template_name}')
        elif keyword == '下季新番':
            template_name = await generate_next_season_url()
            response = requests.get(base_url + f'{template_name}')
        else:
            template_name = 'forecast_anime'
            response = requests.get(new)

        if response.status_code != 200:
            return None

        soup = await dispose_html(response)
        with open(yuc_wiki_path+f'{template_name}.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        await get_yuc_wiki_image(template_name,568,1885)
    except (Exception, IOError) as e:
        print(f"Error occurred: {e}")

    return yuc_wiki_path+f'{template_name}.jpeg'

async def generate_season_url():
    """
    获取当前季度
    :return:
    """
    now = datetime.now()
    quarter_month = ((now.month - 1) // 3) * 3 + 1
    return f"{now.year}{quarter_month:02d}"

async def generate_next_season_url():
    """
    获取下季度
    :return:
    """
    now = datetime.now()
    quarter_month = ((now.month - 1) // 3) * 3 + 1
    current_quarter_start = datetime(now.year, quarter_month, 1)

    next_quarter_start = current_quarter_start + timedelta(days=90)
    next_quarter_month = ((next_quarter_start.month - 1) // 3) * 3 + 1
    return f"{next_quarter_start.year}{next_quarter_month:02d}"

async def dispose_html(response):
    """
    处理html
    :param response:
    :return:
    """
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    first_table = soup.select_one('table')
    if first_table:
        first_table.decompose()

    for tag in soup.select('header, aside'):
        tag.decompose()

    hr_tags = soup.find_all('hr')
    if len(hr_tags) >= 2:
        second_hr = hr_tags[1]

        next_element = second_hr.next_sibling
        while next_element:
            next_sibling = next_element.next_sibling
            next_element.extract()
            next_element = next_sibling

    for tag in soup.find_all(['a', 'link', 'img', 'script', 'source']):

        if tag.name == 'img' and tag.get('data-src'):
            tag['src'] = tag['data-src']
            del tag['data-src']

        attr = 'href' if tag.name in ['a', 'link'] else 'src'
        if tag.has_attr(attr):
            path = tag[attr].lstrip('/\\')
            if not path.startswith(('http://', 'https://')):
                tag[attr] = f"{base_url}{path}"
            if path.startswith('http://'):
                tag[attr] = path.replace('http://', 'https://', 1)
    return  soup

async def get_yuc_wiki_image(template_name,width,height):

    file = os.path.join(yuc_wiki_path, f"{template_name}.jpeg")
    if os.path.exists(file):
        with  open(file,"rb") as image_file:
            return image_file.read()

    image_bytes = await template_to_pic(
        template_path=yuc_wiki_path,
        template_name=f'{template_name}.html',
        templates={"data": None},
        quality=40,
        type="jpeg",
        pages={
            "viewport": {"width": width, "height": height},
            "base_url": f"file://{getcwd()}",
        },
        wait=2,
    )
    await save_img(image_bytes,template_name)

async def save_img(data: bytes,template_name : str):

    """
     保存yuc_wiki图片
     :param template_name:
     :param data:
     :return:
     """
    file_path = yuc_wiki_path + f"{template_name}.jpeg"
    with open(file_path, "wb") as file:
        file.write(data)
    print("保存图片完成")


