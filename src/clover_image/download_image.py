import requests

def download_image(url,file_path):
    """
    下载图片
    :param url:
    :param file_path:
    :return:
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    except requests.RequestException as e:
        print(f"下载图片时出错: {e}")