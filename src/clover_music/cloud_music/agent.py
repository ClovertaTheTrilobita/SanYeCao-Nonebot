# -*- coding: UTF-8 -*-

import random
import execjs
agent = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/57.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',

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
def get_login_js():
    return djs('src/clover_music/cloud_music/jsdm.js')

def get_param_js():
    return djs('src/clover_music/cloud_music/param.js')

# 获取ptqrtoken
def ptqrtoken(qrsign):
    # 加载js
    execjs_execjs = execjs.compile(get_login_js())
    return execjs_execjs.call('hash33', qrsign)
# 获取UI
def guid():
    # 加载js
    execjs_execjs = execjs.compile(get_login_js())
    return execjs_execjs.call('guid')
# 获取g_tk
def get_g_tk(p_skey):
    # 加载js
    execjs_execjs = execjs.compile(get_login_js())
    return execjs_execjs.call('getToken', p_skey)
# 获取i
def S():
    # 加载js
    execjs_execjs = execjs.compile(get_login_js())
    return execjs_execjs.call('S')
# 获取key
def a():
    # 加载js
    execjs_execjs = execjs.compile(get_login_js())
    return execjs_execjs.call('a', 16)

def get_params(id):
    execjs_execjs = execjs.compile(get_param_js())
    return execjs_execjs.call('get_music', id)
