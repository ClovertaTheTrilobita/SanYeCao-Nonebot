import os

import requests

from src.configs.path_config import image_local_qq_image_path
from src.configs.api_config import app_id,bot_account



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

