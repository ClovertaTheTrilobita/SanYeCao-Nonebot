import execjs
import requests


cookies = {
    'NMTID': '00O8y8Jmz580oVUQEj2u8z-CtjK9TAAAAGT_JaiZQ',
    '_ntes_nnid': '70ee9d950560215d692bbd3bac5f7ffd,1735109551078',
    '_ntes_nuid': '70ee9d950560215d692bbd3bac5f7ffd',
    'WM_TID': 'xAl%2FSCq1ZGxFEFQBVUOTDr%2F0kj2cJ4CW',
    'WEVNSM': '1.0.0',
    'WNMCID': 'iljzuk.1735109552031.01.0',
    'ntes_utid': 'tid._.MOPuPUX%252FlRRFVlVFAUbTH7v0liiZp44J._.0',
    'sDeviceId': 'YD-FPy2uqtGAzpEVwAFRBeVx3xH8QxWMOBV',
    '__snaker__id': 'z682UZpwWWtLZGly',
    'ntes_kaola_ad': '1',
    '_iuqxldmzr_': '32',
    'P_INFO': '15902053421|1735930696|1|music|00&99|null&null&null#gud&442000#10#0|&0|null|15902053421',
    '__csrf': 'c9c07b72fc20b640171041342a760e81',
    'MUSIC_U': '00B2B1E45F4C7D1F42BAC95F16E5D85EB2BFC68BE1BE7C6823C3C28A6304B1AB2D4A94E1D803311EF54D20985FAA383FC5003E895B02096F81188209A3BEB719E3768B01CFBCF587E947206DAA31320E0647B9475A1BBF856DFD117BAC65DD66D4A4DBC3F539F5EBA4544AECE36E35395EE562053591A64212AC8F37F30E2B8C11AB2C10C7C03AACBD5DA91C35703F339B829ABD1C51216EDDA18E9EF905F83E62BBC19376CFB5B17DF0E189C29BDA895578060D86C43BA75D89D69A4DEF267CCA705DFE2E6CA049310812FB57EDD6E4E68CE36AED458717E67246291193F48AB3E5620004ECC2E2A8D841C65D7C1A93926D80855CC9092B7FD29BFC5CAF154CB51BFA95CE76F24C732D1B7C6CFA9829025AA7478406C3B5DDBA76B0EF77E1C0B9839ED41FAAD8ED873F484158243ACC8DE9EF439FE9B018A08B3267CD8DDF0A7BC75F8D0625AB15C0F710471ACBB75B6B0220F283B168FB97899BA53E0A583378',
    'gdxidpyhxdE': 'dY7CYik9SZysPpbpa%2B9IZ0WkY%2Bf%2BbijCEJvzgRykt3gd21PLr3Ef0Nd7cJ84EZRYl9gaSyIl8MYbGPTbZonYELjmYv%5CiX5Aasgwj92PikIIxp67PCjEU7bIDfjtqO8gYNgmNKUUZfgoi8GSWC2CzIDMuoVeX0aj2E%2Bw3qgPe%2BzIj0gQo%3A1736774883618',
    'WM_NI': 'xxsz9lwGcCulm7plUDTn8EV4tPXXmBnkvNboMiKwOMaO68vvTGh%2B1%2F8geHL3MiaGz4kBNcL80kPI8L3k%2BIL2fR3rUpxQvjfQB14knTh8XpFASriLyzyWugn%2BZ8IrVmVSS3M%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eebae25ef3bf85b9f14ab5ac8ab7d44b978f8eadcb6998b9a992b3418caca88ed82af0fea7c3b92abca8bd9bbc68b599ada4f868afe9c08dd85098b2f8a6d540b89098b9f04aaeb5baafe1658fb78598ce47a391fad9f57e9899a8ccb425fcb9aba9cf398fb7afa8f940a99e8284cf34f4b5a0aabb48f1b5e5aacf3aa68efd93d87cbc8fba8be55b82effc8ced60ace89891c54b91aea7adfc72bb89bb88ed219ae88793d567968d9dd4d037e2a3',
    'JSESSIONID-WYYY': 'J1xKzQq7BEfO8faiU7GJrD54bxJC0oUwq8XyduKkEEBj8J8qy2n9Igx5l%2FQsOea4eBHs%2Bph7pHSFbPwTdCK4j6wSqY9BPMeJ828h5SZy4T4Rzx%2FQIrrvZn7ZbvrBwI9eDwd7vo9vOfVY4EIj2TpYdYP%2FTjOf5fzTq%5Ce3gB1a29J0ZyUY%3A1736913831537',
    'playerid': '81625937',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NMTID=00O8y8Jmz580oVUQEj2u8z-CtjK9TAAAAGT_JaiZQ; _ntes_nnid=70ee9d950560215d692bbd3bac5f7ffd,1735109551078; _ntes_nuid=70ee9d950560215d692bbd3bac5f7ffd; WM_TID=xAl%2FSCq1ZGxFEFQBVUOTDr%2F0kj2cJ4CW; WEVNSM=1.0.0; WNMCID=iljzuk.1735109552031.01.0; ntes_utid=tid._.MOPuPUX%252FlRRFVlVFAUbTH7v0liiZp44J._.0; sDeviceId=YD-FPy2uqtGAzpEVwAFRBeVx3xH8QxWMOBV; __snaker__id=z682UZpwWWtLZGly; ntes_kaola_ad=1; _iuqxldmzr_=32; P_INFO=15902053421|1735930696|1|music|00&99|null&null&null#gud&442000#10#0|&0|null|15902053421; __csrf=c9c07b72fc20b640171041342a760e81; MUSIC_U=00B2B1E45F4C7D1F42BAC95F16E5D85EB2BFC68BE1BE7C6823C3C28A6304B1AB2D4A94E1D803311EF54D20985FAA383FC5003E895B02096F81188209A3BEB719E3768B01CFBCF587E947206DAA31320E0647B9475A1BBF856DFD117BAC65DD66D4A4DBC3F539F5EBA4544AECE36E35395EE562053591A64212AC8F37F30E2B8C11AB2C10C7C03AACBD5DA91C35703F339B829ABD1C51216EDDA18E9EF905F83E62BBC19376CFB5B17DF0E189C29BDA895578060D86C43BA75D89D69A4DEF267CCA705DFE2E6CA049310812FB57EDD6E4E68CE36AED458717E67246291193F48AB3E5620004ECC2E2A8D841C65D7C1A93926D80855CC9092B7FD29BFC5CAF154CB51BFA95CE76F24C732D1B7C6CFA9829025AA7478406C3B5DDBA76B0EF77E1C0B9839ED41FAAD8ED873F484158243ACC8DE9EF439FE9B018A08B3267CD8DDF0A7BC75F8D0625AB15C0F710471ACBB75B6B0220F283B168FB97899BA53E0A583378; gdxidpyhxdE=dY7CYik9SZysPpbpa%2B9IZ0WkY%2Bf%2BbijCEJvzgRykt3gd21PLr3Ef0Nd7cJ84EZRYl9gaSyIl8MYbGPTbZonYELjmYv%5CiX5Aasgwj92PikIIxp67PCjEU7bIDfjtqO8gYNgmNKUUZfgoi8GSWC2CzIDMuoVeX0aj2E%2Bw3qgPe%2BzIj0gQo%3A1736774883618; WM_NI=xxsz9lwGcCulm7plUDTn8EV4tPXXmBnkvNboMiKwOMaO68vvTGh%2B1%2F8geHL3MiaGz4kBNcL80kPI8L3k%2BIL2fR3rUpxQvjfQB14knTh8XpFASriLyzyWugn%2BZ8IrVmVSS3M%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebae25ef3bf85b9f14ab5ac8ab7d44b978f8eadcb6998b9a992b3418caca88ed82af0fea7c3b92abca8bd9bbc68b599ada4f868afe9c08dd85098b2f8a6d540b89098b9f04aaeb5baafe1658fb78598ce47a391fad9f57e9899a8ccb425fcb9aba9cf398fb7afa8f940a99e8284cf34f4b5a0aabb48f1b5e5aacf3aa68efd93d87cbc8fba8be55b82effc8ced60ace89891c54b91aea7adfc72bb89bb88ed219ae88793d567968d9dd4d037e2a3; JSESSIONID-WYYY=J1xKzQq7BEfO8faiU7GJrD54bxJC0oUwq8XyduKkEEBj8J8qy2n9Igx5l%2FQsOea4eBHs%2Bph7pHSFbPwTdCK4j6wSqY9BPMeJ828h5SZy4T4Rzx%2FQIrrvZn7ZbvrBwI9eDwd7vo9vOfVY4EIj2TpYdYP%2FTjOf5fzTq%5Ce3gB1a29J0ZyUY%3A1736913831537; playerid=81625937',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

params = {
    'csrf_token': 'c9c07b72fc20b640171041342a760e81',
}

data = {
    'params': 'nvRE14quU2f1ge3FCmBfGqo3PAkgmLPWQYSjX5TTa6o3CSSvGGdecBNdLzvNymhfUyVDR6ZjboRjxOp0OaqzoXXbJUb085o+yJZWUt/+U7uBLM+zyYaAZBpSJk5wE30wJZ+/Y/NC0BDuN4lB7K+QR6VaUNly7hIk0trvh+DITgsoQqdKDie7C+EqFNEVYan9LoKVikJjaPFJAxBGtDZWrQ==',
    'encSecKey': '27dba2f08b7025a9f62b326292dfc4975cb5d1c46d524ae2bd7a0f4e47ff60acdc5f22a99cab75a2a38083fa264b618ebdcded209c1f8d167d4e62205795bb4fb367db862644489bdef6266508a6c285b2e793968e02c856a13285c7ec7d7a8c2984ae70257ec721aa674a6c64f62cbb17535c07b4378dc2a95f7e48553e8db7',
}

f = open('../../music/cloud_music/param.js', 'r', encoding='utf-8').read()
ctx = execjs.compile(f)
result = ctx.call('get_music', '1357375695')
print(result)

data = {
    'params': result['encText'],
    'encSecKey': result['encSecKey'],
}

response = requests.post('https://music.163.com/weapi/song/enhance/player/url/v1', params=params, cookies=cookies, headers=headers,
                         data=data)
print(response.text)




"""

# 判断cookie是否有效
def netease_cloud_music_is_login(session):
    try:
        session.cookies.load(ignore_discard=True)
    except Exception:
        pass
    csrf_token = session.cookies.get('__csrf')
    c = str({'csrf_token': csrf_token})
    try:
        loginurl = session.post(
            'https://music.163.com/weapi/w/nuser/account/get?csrf_token={}'.format(csrf_token),
            data={
                'params': AES_aes(AES_aes(c,g,iv),i,iv),
                'encSecKey': encSecKey()},
            headers=headers).json()
        if '200' in str(loginurl['code']):
            print('Cookies值有效：', loginurl['profile']['nickname'], '，已登录！')
            return session, True
        else:
            print('Cookies值已经失效，请重新扫码登录！')
            return session, False
    except BaseException:
        print('Cookies值已经失效，请重新扫码登录！')
        return session, False


# 登录扫码保存cookie
def netease_cloud_music_login():
    # 写入
    session = requests.session()
    if not os.path.exists('cloud_music_cookies.cookie'):
        with open('cloud_music_cookies.cookie', 'wb') as f:
            pickle.dump(session.cookies, f)
    # 读取
    session.cookies = pickle.load(open('cloud_music_cookies.cookie', 'rb'))
    session, status = netease_cloud_music_is_login(session)
    if not status:
        getlogin = session.post( 'https://music.163.com/weapi/login/qrcode/unikey?csrf_token=',
            data={
                'params': params(None),
                'encSecKey': encSecKey()
            },
            headers=headers).json()
        pngurl = 'https://music.163.com/login?codekey=' + getlogin['unikey'] + '&refer=scan'

        qr = qrcode.QRCode()
        qr.add_data(pngurl)
        img = qr.make_image()
        a = BytesIO()
        img.save(a, 'png')
        png = a.getvalue()
        a.close()
        # 打开二维码进行扫码操作
        t = showpng(png)
        t.start()

        tokenurl = 'https://music.163.com/weapi/login/qrcode/client/login?csrf_token='
        while True:
            u = str({'key': getlogin['unikey'], 'type': "1", 'csrf_token': ""})
            qrcodedata = session.post(
                tokenurl,
                data={
                    'params': params(u),
                    'encSecKey': encSecKey()
                },
                headers=headers).json()
            if '801' in str(qrcodedata['code']):
                print('二维码未失效，请扫码！')
            elif '802' in str(qrcodedata['code']):
                print('已扫码，请确认！')
            elif '803' in str(qrcodedata['code']):
                print('已确认，登入成功！')
                break
            else:
                print('其他：', qrcodedata)
            time.sleep(2)
        with open('cloud_music_cookies.cookie', 'wb') as f:
            pickle.dump(session.cookies, f)
    return session




if __name__ == '__main__':
    netease_cloud_music_login()

"""