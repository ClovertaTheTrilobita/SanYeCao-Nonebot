import qrcode
from io import BytesIO
from PIL import Image

# 创建 QRCode 对象
qr = qrcode.QRCode(  version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
def create_qr_code(unikey):
    # 添加数据
    pngurl = f"http://music.163.com/login?codekey={unikey}"
    qr.add_data(pngurl)
    img = qr.make_image()
    a = BytesIO()
    img.save(a, 'png')
    png = a.getvalue()
    # 将字节数据转换为图像
    img = Image.open(BytesIO(png))
    # 保存图像到本地文件
    img.save('qrcode.png')
    # a.close()
    # # 打开二维码进行扫码操作
    # t = showpng(png)
    # t.start()


if __name__ == "__main__":
    create_qr_code("123")

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