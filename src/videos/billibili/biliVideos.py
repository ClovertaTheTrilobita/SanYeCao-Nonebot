import os
import pickle

import requests
import hashlib
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

if not os.path.exists('bili.cookie'):
    # 使用Selenium模拟浏览器获取Cookie
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.bilibili.com")
    # cookies = driver.get_cookies()
    with open('bili.cookie', 'wb') as f:
        pickle.dump(driver.get_cookies(), f)
    driver.quit()

cookies = pickle.load(open('bili.cookie', 'rb'))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "referer": "https://www.bilibili.com/",
    "Cookie": "; ".join([f"{c['name']}={c['value']}" for c in cookies])
}



appkey = '1d8b6e7d45233436'
appsec = '560c52ccd288fed045859ed18bffd973'
params = {
    'search_type':'video'
}

def appsign(params, appkey, appsec):
    """为请求参数进行 APP 签名"""
    params.update({'appkey': appkey})
    params = dict(sorted(params.items())) # 按照 key 重排参数
    query = urllib.parse.urlencode(params) # 序列化参数
    sign = hashlib.md5((query+appsec).encode()).hexdigest() # 计算 api 签名
    params.update({'sign':sign})
    return params


def get(keyword):
    signed_params = appsign(params, appkey, appsec)
    query = urllib.parse.urlencode(signed_params)
    url = f"https://api.bilibili.com/x/web-interface/search/type?keyword={keyword}&"
    session = requests.session()
    session.get("https://www.bilibili.com/", headers=headers)
    response = session.get(url + query, headers=headers).json()
    # print(response['code'])
    return response
# print(signed_params)
# print(query)

if __name__ == "__main__":
    print(get('海南某211台风过后现状111'))
