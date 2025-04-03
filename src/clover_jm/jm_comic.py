import yaml
import jmcomic
from src.clover_jm.disguise_pdf import *
from concurrent.futures import ThreadPoolExecutor
from src.configs.path_config import jm_path,jm_config_path
from src.clover_image.delete_file import delete_folder,delete_file
from src.clover_email.send_email import send_email_by_google,send_email_by_qq

# 创建线程池
jm_executor = ThreadPoolExecutor(max_workers=2)
jm_executor.submit(lambda: None).result()

async def download_jm(album_id: str| None,receiver_email: str| None):
    # 修改配置文件的下载路径
    source_path = await get_jm_config(receiver_email)
    option = jmcomic.JmOption.from_file(jm_config_path)
    # 还原配置文件
    await recover_jm_config(source_path)
    #调用JM下载api
    album_detail,downloader = await asyncio.get_event_loop().run_in_executor(jm_executor,jmcomic.download_album,album_id,option)
    if album_detail.title is None:
        return "下载失败,请检查JM ID 是否正确"
    # 创建变量
    folder_path = f"{jm_path}{receiver_email}"
    zip_path = f"{jm_path}{album_detail.title}.zip"
    # 压缩文件
    zip_status = await folder_zip(folder_path,zip_path)
    if not zip_status:
        await delete_folder(folder_path)
        return "压缩文件失败"
    # 发送邮件
    send_status = await send_email_by_qq(receiver_email,zip_path)
    if send_status:
        # 删除文件
        await delete_folder(folder_path)
        await delete_file(zip_path)
        return "发送成功,请注意查收\n如遇邮箱接收不到,请检查发送的邮箱是否正确,或者是否在垃圾箱"
    else:
        await delete_folder(folder_path)
        await delete_file(zip_path)
        return "发送邮件失败，请重试!"


async def get_jm_config(receiver_email: str):

    with open(jm_config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        source_path = config['dir_rule']['base_dir']
        new_base_dir = str(Path(source_path) / receiver_email)
        config['dir_rule']['base_dir'] = new_base_dir
    with open(jm_config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)
    return source_path

async def recover_jm_config(source_path : str):

    with open(jm_config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        new_base_dir = str(Path(source_path))
        config['dir_rule']['base_dir'] = new_base_dir
    with open(jm_config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)