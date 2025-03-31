import jmcomic
from src.clover_jm.disguise_pdf import *
from src.configs.path_config import jm_path
from src.clover_image.delete_file import delete_file_batch,delete_folder

async def download_jm(album_id: str| None):

    album_detail,downloader = jmcomic.download_album(album_id)

    original_path = os.getcwd()+f"/{album_detail.title}"
    # 将图片转换为PDF
    await webp_to_pdf(original_path,jm_path +f"{album_id}.pdf")
    pdf_file = jm_path + f"{album_id}.pdf"
    jpg_file = jm_path + 'temp.jpg'
    zip_file = jm_path + "resume.zip"
    output_file =  jm_path +"merged.jpg"

    if os.path.exists(pdf_file) and os.path.exists(jpg_file):
        await zip_pdf(pdf_file, zip_file)
        await merge_files(jpg_file, zip_file, output_file)

        await delete_file_batch([zip_file, pdf_file])
        await delete_folder(original_path)
    else:
        print("PDF文件或JPG文件不存在，请检查文件路径。")

    return output_file

