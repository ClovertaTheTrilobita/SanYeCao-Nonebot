import requests


def saucenao_search(image_path=None, image_url=None, api_key='your_api_key', numres=5):
    """
    使用 SauceNAO API 进行以图搜图

    :param image_path: 本地图片的文件路径，若提供图片 URL 则此参数可省略
    :param image_url: 图片的网络 URL，若提供本地图片路径则此参数可省略
    :param api_key: SauceNAO API Key
    :param numres: 要返回的搜索结果数量
    :return: 搜索结果的 JSON 数据
    """
    base_url = 'https://saucenao.com/search.php'
    params = {
        'output_type': 2,  # 输出类型为 JSON
        'numres': numres,  # 返回的结果数量
        'api_key': api_key
    }

    if image_url:
        params['url'] = image_url
    elif image_path:
        files = {'file': open(image_path, 'rb')}
        response = requests.post(base_url, params=params, files=files)
    else:
        raise ValueError("url错误")

    if image_url:
        response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None


def parse_saucenao_result(result):
    """
    解析 SauceNAO 的搜索结果
    """
    if not result or 'results' not in result:
        print("未找到有效的搜索结果。")
        return

    print(result)
    for index, item in enumerate(result['results'], start=1):
        header = item['header']
        data = item['data']

        similarity = header.get('similarity', '未知')
        thumbnail = header.get('thumbnail', '未知')
        title = data.get('title', '未知')
        author = data.get('member_name', data.get('author_name', '未知'))
        ext_urls = data.get('ext_urls', [])
        pixiv_id = data.get('pixiv_id', '未知')

        print(f"结果 {index}:")
        print(f"  相似度: {similarity}%")
        print(f"预览图{thumbnail}  ")
        print(f"  标题: {title}")
        print(f"  作者: {author}")
        if ext_urls:
            print(f"  来源链接: {ext_urls[0]}")
        else:
            print("  来源链接: 未知")
        print(f"pixiv_id:{pixiv_id}")
        print()

if __name__ == "__main__":
    # 若使用本地图片，提供图片路径
    image_path = 's.png'
    # 若使用网络图片，提供图片 URL
    # image_url = 'https://example.com/your_image.jpg'
    api_key = 'b2f961a88d854dc457a235c55d8486a764e8ff7d'
    result = saucenao_search(image_path=image_path, api_key=api_key)
    if result:
        parse_saucenao_result(result)