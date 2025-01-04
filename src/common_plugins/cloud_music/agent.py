# -*- coding: UTF-8 -*-

import random
import execjs
agent = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/57.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",

]

# 获取浏览器认证头
def get_user_agents():
    return random.choice(agent)
# 读取js
def djs(js):
    f = open(js, 'r', encoding='utf-8')
    jst = ''
    while True:
        readline = f.readline()
        if readline:
            jst += readline
        else:
            break
    return jst
def getjs():
    return djs('src/common_plugins/cloud_music/jsdm.js')

# 获取ptqrtoken
def ptqrtoken(qrsign):
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('hash33', qrsign)
# 获取UI
def guid():
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('guid')
# 获取g_tk
def get_g_tk(p_skey):
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('getToken', p_skey)
# 获取i
def S():
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('S')
# 获取key
def a():
    # 加载js
    execjs_execjs = execjs.compile(getjs())
    return execjs_execjs.call('a', 16)
