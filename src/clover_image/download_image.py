import aiohttp

async def download_image(url,file_path):
    """
    下载图片
    :param url:
    :param file_path:
    :return:
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                with open(file_path, 'wb') as file:
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        file.write(chunk)
    except aiohttp.ClientError as e:
        print(f"下载图片时出错: {e}")