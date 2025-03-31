import os
import zipfile
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
        # raise ValueError("未找到WebP图片")

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
        # raise ValueError("无有效图片")

    images[0].save(
        output_pdf,
        save_all=True,
        append_images=images[1:],
        optimize=True,
        quality=85
    )
    return output_pdf



async def zip_pdf(pdf_path, zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            arcname = os.path.basename(pdf_path)
            zipf.write(pdf_path, arcname=arcname)
    except Exception as e:
        print(f"压缩PDF时出错: {e}")


async def merge_files(jpg_path, zip_path, output_path):
    try:
        with open(jpg_path, 'rb') as jpg_file, open(zip_path, 'rb') as zip_file, open(output_path,'wb') as output_file:
            output_file.write(jpg_file.read())
            output_file.write(zip_file.read())
    except Exception as e:
        print(f"合并文件时出错: {e}")
