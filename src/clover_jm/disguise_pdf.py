import os
import asyncio
import zipfile
from pathlib import Path
from PIL import Image
from natsort import natsorted


async def webp_to_pdf(input_folder, output_pdf):
    """
    WebP转PDF
    """
    webp_files = natsorted(
        [os.path.join(input_folder, f) for f in os.listdir(input_folder)
         if f.lower().endswith('.webp')],
        key=lambda x: os.path.basename(x)
    )

    if not webp_files:
        print("未找到WebP图片")

    images = []
    for webp_file in webp_files:
        try:
            img = Image.open(webp_file)
            # 处理透明背景
            if img.mode in ('RGBA', 'LA'):
                white_bg = Image.new('RGB', img.size, (255, 255, 255))
                white_bg.paste(img, mask=img.split()[-1])
                images.append(white_bg)
            else:
                images.append(img.convert('RGB'))
        except Exception as e:
            print(f"处理失败 {webp_file}: {e}")

    if not images:
        print("无有效图片")

    images[0].save(
        output_pdf,
        save_all=True,
        append_images=images[1:],
        optimize=True,
        quality=80
    )

async def batch_convert_subfolders(base_dir,output_dir):
    """
    批量转换指定目录下所有子文件夹中的WebP图片为独立PDF
    :param base_dir: 要扫描的根目录，默认当前目录
    :param output_dir: PDF输出目录
    """
    subfolders = [
        f for f in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, f))
           and not f.startswith('.')
           and f != os.path.basename(output_dir)
    ]

    if not subfolders:
        print("未找到有效子文件夹")
        return

    tasks = []
    for folder in subfolders:
        input_path = os.path.join(base_dir, folder)
        output_pdf = os.path.join(output_dir, f"{folder}.pdf")
        tasks.append(
            webp_to_pdf(input_path, output_pdf)
        )

    results = await asyncio.gather(*tasks, return_exceptions=True)
    success = 0
    for folder, result in zip(subfolders, results):
        if isinstance(result, Exception):
            print(f"转换失败 [{folder}]: {str(result)}")
        else:
            print(f"成功转换: {folder} -> {result}")
            success += 1

async def zip_pdf(pdf_path, zip_path):
    """
    压缩单文件
    """
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            arcname = os.path.basename(pdf_path)
            zipf.write(pdf_path, arcname=arcname)
    except Exception as e:
        print(f"压缩PDF时出错: {e}")


async def merge_files(jpg_path, zip_path, output_path):
    """
    将PDF伪装成图片
    """
    try:
        with open(jpg_path, 'rb') as jpg_file, open(zip_path, 'rb') as zip_file, open(output_path,'wb') as output_file:
            output_file.write(jpg_file.read())
            output_file.write(zip_file.read())
    except Exception as e:
        print(f"合并文件时出错: {e}")

async def folder_zip(folder_path, jm_zip_path):
    """
    异步压缩整个文件夹到指定路径
    :param folder_path: 需要压缩的文件夹路径
    :param jm_zip_path: 输出的zip文件路径
    :return: 压缩成功返回True，否则返回False
    """
    try:
        Path(jm_zip_path).parent.mkdir(parents=True, exist_ok=True)

        def sync_zip():
            with zipfile.ZipFile(jm_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:

                for root, dirs, files in os.walk(folder_path):

                    relative_path = Path(root).relative_to(folder_path)

                    for dir_name in dirs:
                        abs_dir = os.path.join(root, dir_name)
                        zipf.write(abs_dir, arcname=str(relative_path / dir_name))

                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = str(relative_path / file)
                        zipf.write(file_path, arcname=arcname)

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, sync_zip)
        print(f"成功压缩文件夹到: {jm_zip_path}")
        return True
    except Exception as e:
        print(f"压缩文件夹失败: {str(e)}")
        return False
