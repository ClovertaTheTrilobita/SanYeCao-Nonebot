from os import getcwd

import requests
from bs4 import BeautifulSoup
from src.configs.api_config import wenku8_username, wenku8_password

# 登录页面的URL
login_url = 'https://www.wenku8.net/login.php?jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php'
index_url = 'https://www.wenku8.net/index.php'

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Upgrade-Insecure-Requests': '1'
}

# 登录表单数据
login_data = {
    'username': wenku8_username,
    'password': wenku8_password,
    'usecookie': '0',
    'action': 'login'
}


async def login():
    # 发送登录请求
    with requests.Session() as session:
        # 注意：这里使用了Session对象来保持会话状态
        login_response = session.post(login_url, data=login_data, headers=headers)

        # 检查登录是否成功（根据实际需求调整）
        if login_response.status_code == 200:
            # 登录成功后，Session对象已经自动保存了Cookie
            # 可以直接使用该Session对象访问受保护的页面
            print("登录成功！")
            # 获取 Cookie
            cookies = session.cookies

            # 保存 Cookie 到文件
            with open('wenku8.cookie', 'w') as f:
                for cookie in cookies:
                    f.write(f"{cookie.name}={cookie.value}; ")
            print("Cookie 保存成功！")
        else:
            print("登录失败，状态码：", login_response.status_code)


async def get_books():
    with open('wenku8.cookie', 'r') as f:
        cookie = f.read()
    headers1 = {
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': cookie
    }

    response = requests.get(index_url, headers=headers1)
    print(response)
    html = response.content.decode('gbk')
    soup = BeautifulSoup(html, 'html.parser')
    orders = soup.find_all(name='div', class_='block')
    head = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <title>轻小说文库 - 最新最全的日本动漫轻小说在线阅读与下载基地</title>
    <meta content="IE=EmulateIE7" http-equiv="X-UA-Compatible"/>
    <meta content="ie-comp" name="renderer"/>
    <meta content="轻小说,sf轻小说,dmzj轻小说,日本轻小说,动漫小说,轻小说电子书,轻小说TXT下载" name="keywords"/>
    <meta content="轻小说文库(www.wenku8.com)是收录最全更新最快的动漫sf轻小说网站,提供轻小说在线阅读,TXT与电子书下载,支持手机WAP访问."
          name="description"/>
    <meta content="no-cache" http-equiv="Cache-Control"/>
    <link href="style.css" media="all" rel="stylesheet" rev="stylesheet" type="text/css"/>
    <script language="javascript" src="/scripts/common.js" type="text/javascript"></script>
    <script language="javascript" src="/themes/wenku8/theme.js" type="text/javascript"></script>
<!--    <link rel="stylesheet" href="main.css">-->
</head>
    """
    with open(getcwd() + "/src/clover_lightnovel/output1.html", 'w', encoding='utf-8') as file:
        file.write(head + str(orders[7]).replace('(<a href="https://www.wenku8.net/zt/sugoi/2025.php"', '').replace(
            'target="_blank">查看 这本轻小说真厉害！2025 TOP榜单</a>)', '') + str(orders[8]) + str(orders[9]))


if __name__ == '__main__':
    login()
    get_books()
