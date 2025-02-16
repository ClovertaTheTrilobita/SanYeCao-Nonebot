import os
import pickle

import ffmpeg
import requests
import hashlib
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.configs.path_config import video_path

chrome_options = Options()
chrome_options.add_argument("--headless")

headers0 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
}

if not os.path.exists('bili.cookie'):
    # # 使用Selenium模拟浏览器获取Cookie
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.bilibili.com")
    # cookies = driver.get_cookies()
    with open('bili.cookie', 'wb') as f:
        pickle.dump(driver.get_cookies(), f)
    driver.quit()
    # with requests.Session() as session:
    #
    #     login_response = session.post("https://www.bilibili.com/")
    #
    #     cookies = session.cookies
    #
    #     # 保存 Cookie 到文件
    #     with open('bili.cookie', 'w') as f:
    #         for cookie in cookies:
    #             f.write(f"{cookie.name}={cookie.value}; ")

cookies = pickle.load(open('bili.cookie', 'rb'))
# with open('bili.cookie', 'r') as f:
#     cookies = f.read()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "referer": "https://www.bilibili.com/",
    "Cookie": "; ".join([f"{c['name']}={c['value']}" for c in cookies])
}



appkey = '1d8b6e7d45233436'
appsec = '560c52ccd288fed045859ed18bffd973'


def appsign(params, appkey, appsec):
    """为请求参数进行 APP 签名"""
    params.update({'appkey': appkey})
    params = dict(sorted(params.items())) # 按照 key 重排参数
    query = urllib.parse.urlencode(params) # 序列化参数
    sign = hashlib.md5((query+appsec).encode()).hexdigest() # 计算 api 签名
    params.update({'sign':sign})
    return params


def get_video_info(keyword):
    params = {
        'search_type': 'video'
    }

    signed_params = appsign(params, appkey, appsec)
    query = urllib.parse.urlencode(signed_params)
    url = f"https://api.bilibili.com/x/web-interface/search/type?keyword={keyword}&"

    session = requests.session()
    session.get("https://www.bilibili.com/", headers=headers)
    response = session.get(url + query, headers=headers).json()
    # print(response['code'])
    return response

def get_video_info_bv(keyword):
    params = {
        'bvid': keyword
    }

    signed_params = appsign(params, appkey, appsec)
    query = urllib.parse.urlencode(signed_params)
    url = "https://api.bilibili.com/x/web-interface/view?&"
    session = requests.session()
    session.get("https://www.bilibili.com/", headers=headers)
    response = session.get(url + query, headers=headers).json()
    return response

def get_video_pages_info(keyword):
    """
    通过BV号获取视频信息

    :param keyword:

    :return:
        len(vid_pages_info_list): 视频集数->int
        vid_pages_info_list: 视频分集信息->dict
        vid_title: 视频标题->str
        vid_author: 视频UP主->str
        vid_pic: 视频封面URL->str
    """
    response = get_video_info_bv(keyword)
    vid_pages_info_list = response['data']['pages']
    vid_title = response['data']['title']
    vid_author = response['data']['owner']['name']
    vid_pic = response['data']['pic']
    return len(vid_pages_info_list), vid_pages_info_list, vid_title, vid_author, vid_pic

def get_video_pages_cid(vid_pages_info_list, num):
    cid = vid_pages_info_list[num - 1]['cid']
    return cid

def get_video_file_url(bvid, cid):
    params = {
        'bvid': bvid,
        'cid': cid,
        'qn': '64',
        'platform': 'html5'
    }

    signed_params = appsign(params, appkey, appsec)
    query = urllib.parse.urlencode(signed_params)
    url = "https://api.bilibili.com/x/player/playurl?&"

    session = requests.session()
    session.get("https://www.bilibili.com/", headers=headers)
    response = session.get(url + query, headers=headers).json()

    file_url = response['data']['durl'][0]['url']

    return file_url

def video_download(file_url, cid):
    response = requests.get(file_url, headers=headers,stream=True)

    # 检查请求是否成功
    if response.status_code == 200:
        # 将视频保存到本地文件
        with open(video_path + f'/{cid}.mp4', 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print("视频下载完成")
    else:
        print(f"下载失败，状态码：{response.status_code}")

def delete_video(cid):
    # 指定要删除的文件路径
    file_path = video_path + f"/{cid}.mp4"

    # 检查文件是否存在
    if os.path.exists(file_path):
        # 删除文件
        os.remove(file_path)
        print(f"文件 {file_path} 已被删除。")
    else:
        print(f"文件 {file_path} 不存在。")

def transcode_video(input_file, output_file):
    try:
        # 转码视频为 H.264 编码
        (
            ffmpeg.input(input_file)
            .output(output_file, c="libx264", crf=23, preset="veryfast")
            .run(capture_stdout=True, capture_stderr=True)
        )
        print(f"视频转码完成，输出文件：{output_file}")
    except ffmpeg.Error as e:
        print(f"转码失败：{e.stderr.decode()}")

if __name__ == "__main__":
    print(get_video_info('海南某211台风过后现状111'))
    print(get_video_file_url('BV1p2PDeEENs', '28194047730'))

    print(get_video_pages_info('BV1p2PDeEENs'))
