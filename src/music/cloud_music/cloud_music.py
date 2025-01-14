# -*- coding: utf-8 -*-
import base64
import codecs
import json
from random import Random

from Crypto.Cipher import AES
import qrcode
import src.music.cloud_music.agent as agent
from threading import Thread
import requests
from io import BytesIO
from PIL import Image
import os
from graiax import silkcoder


requests.packages.urllib3.disable_warnings()
headers = {'User-Agent': agent.get_user_agents(), 'Referer': 'https://music.163.com/'}


class showpng(Thread):
    def __init__(self, data):
        Thread.__init__(self)
        self.data = data

    def run(self):
        img = Image.open(BytesIO(self.data))
        img.show()


# 解密params和encSecKey值
def keys(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)


def AES_aes(t, key, iv):
    def p(s): return s + (AES.block_size - len(s) %AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
    encrypt = str(base64.encodebytes(AES.new( keys(key), AES.MODE_CBC,keys(iv)).encrypt(str.encode(p(t)))),encoding='utf-8')
    return encrypt


def RSA_rsa(i, e, f):
    return format(int(codecs.encode(
        i[::-1].encode('utf-8'), 'hex_codec'), 16) ** int(e, 16) % int(f, 16), 'x').zfill(256)


# 获取的参数
key = agent.S()  # i6c的值
d = str({'key': key, 'type': "1", 'csrf_token': ""})
e = "010001"  # (["流泪", "强"])的值
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"  # (["爱心", "女孩", "惊恐", "大笑"])的值
iv = "0102030405060708"  # 偏移量
i = agent.a()  # 随机生成长度为16的字符串


def params(u):
    if u is None:
        return AES_aes(AES_aes(d, g, iv), i, iv)  # g 和 i 都是key代替
    else:
        return AES_aes(AES_aes(u,g,iv),i,iv)  # g 和 i 都是key代替

def encSecKey():
    return RSA_rsa(i, e, f)

"""

使用二维码登录网易云音乐，需要先获取二维码的key，然后使用该key生成二维码，扫描二维码登录，最后通过登录接口 返回cookie 保存起来

"""




save_path = os.getcwd()+'/src/music/netease_music'
qrcode_path = os.getcwd()+'/src/music'


# 判断cookie是否有效
def netease_cloud_music_is_login(session):
    try:
        session.cookies.load(ignore_discard=True)
    except Exception:
        pass
    csrf_token = session.cookies.get('__csrf')
    if csrf_token is None:
        return session, False
    else:
        try:
            loginurl = session.post(f'https://music.163.com/weapi/w/nuser/account/get?csrf_token={csrf_token}',data={'params': params(None), 'encSecKey': encSecKey()}, headers=headers).json()
            print(loginurl)
            print(loginurl['code'])
            if '200' in str(loginurl['code']):
                print('登录成功')
                return session, True
            else:
                print('登录失败')
                return session, False
        except BaseException:
            return session, False

# 获取二维码的key
def get_qr_key(session):
    url = f"https://music.163.com/weapi/login/qrcode/unikey"
    data = {"params": params(None),"encSecKey": encSecKey()}
    response = session.post(url, headers=headers,params=data)
    result = json.loads(response.text)
    if result.get("code") == 200:
        unikey = result.get("unikey")
        print(unikey)
        return unikey
    else:
        return None



# 创建 QRCode 对象
qr = qrcode.QRCode(  version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
# 生成二维码
def create_qr_code(unikey):
    # 添加数据
    pngurl = f"http://music.163.com/login?codekey={unikey}"
    qr.add_data(pngurl)
    img = qr.make_image()
    a = BytesIO()
    img.save(a, 'png')
    img.save(os.path.join(qrcode_path, 'qrcode.png'))
    return  qrcode_path + '/qrcode.png'


# 检查二维码状态是否被扫描
def check_qr_code(unikey,session):
    tokenurl = f"https://music.163.com/weapi/login/qrcode/client/login?csrf_token="
    u = str({'key': unikey, 'type': "1", 'csrf_token': ""})
    qrcodedata = session.post(
        tokenurl,
        data={
            'params': params(u),
            'encSecKey': encSecKey()
        },
        headers=headers).json()
    return qrcodedata.get('code')


def netease_music_search(keyword,session):
    url = "http://music.163.com/api/search/get"
    params = {
        "s": keyword,
        "type": 1,  # 1 表示搜索歌曲，2 表示搜索专辑，3 表示搜索歌手等
        "limit": 10,  # 限制搜索结果的数量
        "offset": 0,  # 搜索结果的偏移量，可用于分页
        "sub": "false",
    }
    response = session.get(url, headers=headers, params=params)
    data = response.json()
    if "result" in data and "songs" in data["result"]:
        songs = data["result"]["songs"]
        if songs:
            filtered_data = [item for item in songs if item.get('fee') == 8]# 过滤掉付费歌曲
            num = 0
            if len(filtered_data) - 1 <= 0: # 判断返回内容是否为空
                return None, None, None, None
            num = Random().randint(0, len(filtered_data) - 1)
            first_song = filtered_data[num]  # 获取第一首歌曲
            song_name = first_song["name"]
            singer = first_song["artists"][0]["name"]
            song_id = first_song["id"]
            song_url = f"https://music.163.com/song?id={song_id}"
            print(f"搜索结果：{song_name} - {singer}")
            print(f"歌曲链接：{song_url}")
            return song_id,song_name,singer,song_url
    return None, None, None, None


def netease_music_download(song_id,song_name,singer,session):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    download_url = f"http://music.163.com/song/media/outer/url?br=999000&id={song_id}.mp3"
    response = session.get(download_url, headers=headers)
    if response.status_code == 200:
        print(f"正在下载 {song_name} - {singer} 歌曲...")
        file_path = os.path.join(save_path, f"{song_name}-{singer}.mp3")
        file_name = os.path.basename(f"{song_name}-{singer}.mp3")
        with open(file_path, "wb") as f:
            f.write(response.content)
        output_silk_path = os.path.join(save_path, os.path.splitext(file_name)[0] + ".silk")
        # 使用 graiax-silkcoder 进行转换
        silkcoder.encode(file_path, output_silk_path)
        return output_silk_path
    else:
        return None


def netease_music_delete():
    for root, dirs, files in os.walk(save_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)


# def main():
#     keyword = input("请输入你想要搜索的歌曲名称：")
#     save_path = '../src/music/netease_music'
#     if not os.path.exists(save_path):
#         os.makedirs(save_path)
#     song_id,song_name,singer,song_url = netease_music_search(keyword)
#     if song_id:
#         download_result = netease_music_download(song_id,song_name,singer)
#         # download_result = netease_music_play(song_id,song_name,singer)
#         if download_result:
#             print(f"歌曲已成功下载到 {download_result}")
#         else:
#             print("歌曲下载失败，请检查网络或 API 状态。")

#
# if __name__ == "__main__":
#     main()


# def main():
#     cloud_music_login()

# if __name__ == "__main__":
#     main()
























