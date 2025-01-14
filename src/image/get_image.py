import os
import yaml
import random
import requests


with open(os.getcwd() +'/src/image/config/image.yaml', 'r', encoding='utf-8') as f:
    image = yaml.load(f.read(), Loader=yaml.FullLoader).get('image')
    image_local_path = image.get('image_local_path')
    image_local_qq_image_path = image.get('image_local_qq_image_path')
    smms_token = image.get('smms_token')
    smms_image_upload_history = image.get('smms_image_upload_history')
    ju_he_token = image.get('ju_he_token')
    ju_he_image_list = image.get('ju_he_image_list')
    app_id = image.get('app_id')

"""本地图片"""
def get_image_names():
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 定义常见的图片文件扩展名
    image_names = []
    for root, dirs, files in os.walk(os.getcwd()+'/'+image_local_path):
        for file in files:
            if any(file.endswith(ext) for ext in image_extensions):  # 检查文件是否是图片文件
                image_names.append(file)
    random.choice(image_names)  # 随机选取一张图片
    local_image_path = os.getcwd() + '/' + image_local_path + '/' + random.choice(image_names)  # 随机选取一张图片的路径
    return local_image_path

"""获取QQ头像"""
def download_qq_image(member_open_id):
    save_path = os.getcwd() + '/' + image_local_qq_image_path + '/' + member_open_id + '.jpg'
    size = 640 #尺寸 40、100、140、640
    url = f"https://q.qlogo.cn/qqapp/{app_id}/{member_open_id}/{size}"
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


if __name__ == '__main__':
    print(get_smms_image_url())
    print(get_juhe_image_url())
    print(get_image_names())