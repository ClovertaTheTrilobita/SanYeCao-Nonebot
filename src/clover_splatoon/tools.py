import datetime
from datetime import datetime, timezone
from io import BytesIO
import time
import uuid
import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw
import random
import json,base64
from src.clover_splatoon.splatoon_data import weapons,stage,subweapons,specials, friend_list,stage3,weapons3

def get_counter(now):
    global counter
    global date
    if date == now:
        counter += 1
    else:
        date = datetime.now().strftime('%Y-%m-%d')
        counter = 1

    return counter


def random_id(rtype):
    if rtype == 'wep':
        r = int(random.choice(list(weapons.keys())))
        if r < 0:
            r = random_id('wep')
        else:
            return r
    elif rtype == 'map':
        r = (random.choice(list(stage.keys())))
        if r.isdigit():
            return r
        else:
            r = random_id('map')
    else:
        pass

    return r


def img_to_b64(pic: PIL.Image.Image):
    buf = BytesIO()

    pic.save(buf, format="PNG")
    base64_str = base64.b64encode(buf.getbuffer()).decode()
    return "base64://" + base64_str


def circle_corner(img, radii):
    # 画圆（用于分离4个角）
    circle = PIL.Image.new('L', (radii * 2, radii * 2), 0)  # 创建黑色方形
    # circle.save('1.jpg','JPEG',qulity=100)
    draw = PIL.ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radii * 2, radii * 2), fill=255)  # 黑色方形内切白色圆形
    # circle.save('2.jpg','JPEG',qulity=100)
    img = img.convert("RGBA")
    w, h = img.size
    alpha = PIL.Image.new('L', img.size, 255)
    alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))  # 左上角
    alpha.paste(circle.crop((radii, 0, radii * 2, radii)), (w - radii, 0))  # 右上角
    alpha.paste(circle.crop((radii, radii, radii * 2, radii * 2)), (w - radii, h - radii))  # 右下角
    alpha.paste(circle.crop((0, radii, radii, radii * 2)), (0, h - radii))  # 左下角
    img.putalpha(alpha)  # 白色区域透明可见，黑色区域不可见
    return img


def merge_image(base_img, tmp_img, img_x, img_y, scale):
    # 加载底图
    # base_img = Image.open(u'C:\\download\\games\\bg1.png')
    # 加载需要P上去的图片
    # tmp_img = Image.open(u'C:\\download\\games\\b.png')
    # 这里可以选择一块区域或者整张图片
    region = tmp_img

    width = int(region.size[0] * scale)
    height = int(region.size[1] * scale)
    region = region.resize((width, height), PIL.Image.ANTIALIAS)
    base_img = base_img.convert("RGBA")
    region = region.convert("RGBA")
    # 透明png不变黑白背景，需要加第三个参数,jpg和png不能直接合并
    base_img.paste(region, (img_x, img_y), region)
    return base_img

def parse_iso_z(dt_str: str) -> datetime:
    """
    Parse ISO8601 string like '2026-02-01T14:00:00Z' into aware datetime (UTC).
    """
    # Python datetime.fromisoformat 不认 'Z'，把 Z 换成 +00:00
    return datetime.fromisoformat(dt_str.replace("Z", "+00:00")).astimezone(timezone.utc)

