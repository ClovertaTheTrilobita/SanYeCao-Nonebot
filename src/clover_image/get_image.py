import os
import random
import requests
from PIL import Image, ImageDraw,ImageFont

from src.configs.path_config import image_local_path,image_local_qq_image_path,rua_png,temp_path
from src.configs.api_config import smms_token,smms_image_upload_history,ju_he_token,ju_he_image_list,app_id,bot_account

"""本地图片"""
def get_image_names():
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 定义常见的图片文件扩展名
    image_names = []
    for root, dirs, files in os.walk(image_local_path):
        for file in files:
            if any(file.endswith(ext) for ext in image_extensions):  # 检查文件是否是图片文件
                image_names.append(file)
    random.choice(image_names)  # 随机选取一张图片
    local_image_path = image_local_path + '/' + random.choice(image_names)  # 随机选取一张图片的路径
    return local_image_path

"""获取QQ头像"""
def download_qq_image(member_open_id):
    if not os.path.exists(image_local_qq_image_path):
        os.makedirs(image_local_qq_image_path)

    save_path = image_local_qq_image_path + '/' + member_open_id + '.jpg'
    size = 640 #尺寸 40、100、140、640
    url = f"https://q.qlogo.cn/qqapp/{app_id}/{member_open_id}/{size}"
    response = requests.get(url)  # 发送 GET 请求获取图片资源
    if response.status_code == 200:  # 判断请求是否成功
        with open(save_path, 'wb') as file:  # 以二进制写入模式打开文件
            file.write(response.content)  # 将响应内容写入文件
        return save_path

"""获取QQ头像"""
def download_qq_image_by_account(account):
    if not os.path.exists(image_local_qq_image_path):
        os.makedirs(image_local_qq_image_path)
    if account is None:
        account = bot_account
    save_path = image_local_qq_image_path + '/' + account + '.jpg'
    size = 640  # 尺寸 40、100、140、640
    url = f"https://q2.qlogo.cn/headimg_dl?dst_uin={account}&spec={size}"
    response = requests.get(url)  # 发送 GET 请求获取图片资源
    if response.status_code == 200:  # 判断请求是否成功
        with open(save_path, 'wb') as file:  # 以二进制写入模式打开文件
            file.write(response.content)  # 将响应内容写入文件
        return save_path

"""删除QQ头像"""
def qq_image_delete():
    for root, dirs, files in os.walk(image_local_qq_image_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

""" sm.ms  图床"""
def get_smms_image_url():
    # 定义请求的参数
    data = requests.get(smms_image_upload_history, headers={'Authorization': smms_token}, params={"page": "1"}).json().get('data')
    urls = [item['url'] for item in data]
    random_url = random.choice(urls)
    return random_url

"""聚合图床"""
def get_juhe_image_url():
    # 定义请求的参数
    params = {"token": ju_he_token,"f": "json","categories": "猫羽雫","page": 1, "size": 400}
    random_url = random.choice(requests.get(ju_he_image_list, params=params).json().get('docs', [])).get('url')
    return random_url


""" rua 头动图生成"""
class rua():
    def __init__(self, img_file):
        self.author = Image.open(img_file)

    def add_png(self, png_d):
        # 重置图片大小
        author = self.author.resize((png_d[0], png_d[1] - png_d[2]))

        # 载入素材
        rua_p1 = Image.open(png_d[3])

        # 创建背景模板
        rua_png1 = Image.new('RGBA', (110, 110), (255, 255, 255, 255))

        # 使用预定义的参数：jd，合成一帧的样例
        rua_png1.paste(author, (110 - png_d[0], 110 - png_d[1] + png_d[2]), author)
        rua_png1.paste(rua_p1, (0, 110 - png_d[1] - png_d[2]), rua_p1)
        return rua_png1

    def add_gif(self):

        # 获取素材列表
        pst = os.listdir(rua_png)
        for i in range(len(pst)):
            pst[i] = rua_png + pst[i]

        # 预调试好的参数，传入素材列表
        jd = [[90, 90, 5, pst[0]],
              [90, 87, 5, pst[2]],
              [90, 84, 10, pst[3]],
              [90, 81, 8, pst[4]],
              [90, 78, 5, pst[5]],
              [90, 75, 5, pst[6]],
              [90, 72, 8, pst[7]],
              [90, 74, 8, pst[8]],
              [90, 77, 9, pst[9]],
              [90, 80, 8, pst[1]]]

        # 重置要生成的图片大小
        self.author = self.author.resize((90, 90))

        # 绘制模板
        alpha_layer = Image.new('L', (90, 90), 0)
        draw = ImageDraw.Draw(alpha_layer)
        draw.ellipse((0, 0, 90, 90), fill=255)
        self.author.putalpha(alpha_layer)

        # gif列表
        gifs = []
        for i in range(len(jd)):
            # 将参数传递给生成方法
            # 添加到gif列表
            gifs.append(self.add_png(jd[i]))

        # 文件名,是否保存所有,图片列表,fps/ms
        gifs[0].save(image_local_qq_image_path + '/rua.gif', "GIF", save_all=True, append_images=gifs, duration=35, loop=0)
        self.author.close()
        return image_local_qq_image_path + '/rua.gif'

"""
图文合成
"""
async def add_text_to_image(image_path, output_path,content,font_path, font_size, text_color,text_position ,position):
    """
    给图片添加文字
    :param image_path: 输入图片的路径
    :param output_path: 合成后的图片名称
    :param content: 要添加的文字内容
    :param font_path: 字体文件路径
    :param font_size: 文字的字体大小
    :param text_color: 文字颜色 (255, 0, 0) "#FF0000" "red"
    :param position: 文字位置，可选值："left", "right", "center", "top", "bottom", "top left corner", "top right corner", "bottom left corner", "bottom right corner"
    :return:
    """
    # 打开图片
    image = Image.open(image_path)
    # 创建一个可用于绘制的对象
    draw = ImageDraw.Draw(image)
    # 设置字体和字体大小
    font = ImageFont.truetype(font_path, font_size)

    wrapped_text,current_width = "",0

    # 遍历文本中的每个字符
    for char in content:
        # 获取字符的宽度
        char_width, _ = draw.textbbox((0, 0), char, font=font)[2:]
        # 如果当前行的宽度加上字符宽度超过图片指定宽度，则换行
        if current_width + char_width > image.width * 9 // 10:  # 这里是图片的十分之九
            wrapped_text += "\n"
            current_width = 0
        # 将字符添加到当前行
        wrapped_text += char
        # 更新当前行的宽度
        current_width += char_width

    # 获取换行后文本的宽度和高度
    text_width, text_height = draw.textbbox((0, 0), wrapped_text, font=font)[2:]

    # 根据位置参数计算文本的位置
    if position == "left":
        position = (0, (image.height - text_height) // 2)
    elif position == "right":
        position = (image.width - text_width, (image.height - text_height) // 2)
    elif position == "center":
        position = ((image.width - text_width) // 2, (image.height - text_height) // 2)
    elif position == "top":
        position = ((image.width - text_width) // 2, 0)
    elif position == "bottom":
        position = ((image.width - text_width) // 2, image.height - text_height)
    elif position == "top left corner":
        position = (0, 0)
    elif position == "top right corner":
        position = (image.width - text_width, 0)
    elif position == "bottom left corner":
        position = (0, image.height - text_height)
    elif position == "bottom right corner":
        position = (image.width - text_width, image.height - text_height)
    elif position == "bottom left corner 9/10":
        position = (0, image.height * 9 // 10 - text_height)

    # 在图片上绘制文本
    draw.multiline_text(position, wrapped_text, font=font, fill=text_color, align=text_position)
    # 保存合成后的图片
    image.save(output_path)
    # 关闭图片
    # image.close()

async def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
    except Exception as e:
        print(f"删除文件时发生错误: {e}")

if __name__ == '__main__':
    # print(get_smms_image_url())
    # print(get_juhe_image_url())
    # print(get_image_names())
    # file_path = '8A91A2F3BE5B5AF3FEC97FB5AA6D9B38.jpg'
    # au = rua(file_path).add_gif()
    image_path = "021.png"
    content = "你是很大的哈设计开发哈卡斯萨夫卡是大华饭店不是的话覆盖过海宿管会啊傻瓜金佛上帝海水淡化你是很大的哈设计开发哈卡斯萨夫卡是大华饭店不是的话覆盖u过海宿管会啊傻瓜金佛上帝海水淡化你"
    output_path = "output.png"
    add_text_to_image(image_path, content, output_path, "微软雅黑.ttc",text_color = (255, 0, 0),font_size=48,position="top")