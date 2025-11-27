import yaml
import uuid
import jmcomic
from datetime import datetime
from src.configs.api_config import qrserver_url,qrserver_size,google_enabled,qq_enabled,server_enabled
from src.clover_jm.disguise_pdf import *
from concurrent.futures import ThreadPoolExecutor
from src.configs.path_config import jm_path,jm_config_path
from src.clover_providers.cloud_file_api.kukufile import Kukufile
from src.clover_image.delete_file import delete_folder,delete_file
from src.clover_email.send_email import send_email_by_google, send_email_by_qq, send_email_by_server

__name__ = "clover | jm_comic"

# 创建线程池
jm_executor = ThreadPoolExecutor(max_workers=3)
jm_executor.submit(lambda: None).result()

async def jm_email(album_id: str| None,receiver_email: str| None):

    album_detail,downloader = await download_jm(album_id = album_id,file_name = None,receiver_email = receiver_email)
    # 创建变量
    folder_path = f"{jm_path}{receiver_email}"
    zip_path = f"{jm_path}{album_detail.title}.zip"
    # 压缩文件
    zip_status = await folder_zip(folder_path,zip_path)
    if not zip_status:
        await delete_folder(folder_path)
        return "压缩文件失败"
    # 发送邮件

    if str(google_enabled).strip().lower() in {"1", "t", "true"}:
        send_status = await send_email_by_google(receiver_email, zip_path)
    elif str(qq_enabled).strip().lower() in {"1", "t", "true"}:
        send_status = await send_email_by_qq(receiver_email,zip_path)
    elif str(server_enabled).strip().lower() in {"1", "t", "true"}:
        send_status = await send_email_by_server(receiver_email,zip_path)
    else:
        logger.error("您未启用任何一个发信服务，请前往 config.yaml 修改。")
        return "管理员未配置邮箱，发送失败了喵，大哥哥真是杂鱼♥️"

    if send_status:
        # 删除文件
        await delete_folder(folder_path)
        await delete_file(zip_path)
        return "发送成功,请注意查收\n如遇邮箱接收不到,请检查发送的邮箱是否正确,或者是否在垃圾箱"
    else:
        await delete_folder(folder_path)
        await delete_file(zip_path)
        return "发送邮件失败，请重试!"

async def jm_qr(album_id: str| None):

    file_name = f"JM-{album_id}-{datetime.now().date()}@{uuid.uuid4().hex}"
    album_detail,downloader = await download_jm(album_id = album_id,file_name = file_name,receiver_email = None)
    # 创建变量
    folder_path = f"{jm_path}{file_name}"
    zip_name = f"{album_detail.title}.zip"
    zip_path = f"{folder_path}{zip_name}"
    # 压缩文件
    zip_status = await folder_zip(folder_path,zip_path)
    if not zip_status:
        await delete_folder(folder_path)
        return "压缩文件失败"

    # 发送文件
    send_status = await Kukufile.upload_file(zip_path,zip_name)
    logger.debug(f"send_status: {send_status}")
    if send_status[0] == "OK":
        # 删除文件
        await delete_folder(folder_path)
        return {
            "msg":"获取成功~！码上下载！~",
            "qr_code": f"{qrserver_url}?size={qrserver_size}&data={send_status[1]}"
        }
    else:
        logger.error(f"上传出错API返回: {send_status}")
        await delete_folder(folder_path)
        return {
            "msg":"上传出错API,请重试!"
        }

async def download_jm(album_id: str| None,file_name :str | None,receiver_email: str| None):
    # 修改配置文件的下载路径
    if not receiver_email:
        source_path = await get_jm_config(file_name)
    else:
        source_path = await get_jm_config(receiver_email)

    option = jmcomic.JmOption.from_file(jm_config_path)
    # 还原配置文件
    await recover_jm_config(source_path)
    # 调用JM下载api
    try:
        return  await asyncio.get_event_loop().run_in_executor(jm_executor, jmcomic.download_album,album_id, option)
    except Exception as e:
        logger.error(f"下载失败 :{e}")
        return "下载失败,请重试"

async def get_jm_config(file_name: str):

    with open(jm_config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        source_path = config['dir_rule']['base_dir']
        new_base_dir = str(Path(source_path) / file_name)
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