import os
import glob
import time
import psutil
import platform
import logging
from pathlib import Path
from nonebot.rule import  to_me
from nonebot.plugin import on_command
from nonebot.adapters.qq import Message, MessageSegment
from src.configs.path_config import temp_path,video_path


repository = on_command("repo", rule=to_me(), priority=10, block=True)
@repository.handle()
async def github_repo():

    content = "三叶草bot仓库地址\n一起来搭个机器人吧😆"
    msg = Message([
        MessageSegment.file_image(Path("src/resources/image/github_repo/SanYeCao-Nonebot3.png")),
        MessageSegment.text(content),
    ])
    await repository.finish(msg)

platform_info = on_command("info", rule=to_me(), priority=10, block=True)
@platform_info.handle()
async def get_platform_info():
    # 获取操作系统名称
    os_name = platform.system()
    os_version = platform.version()
    processor_name = platform.processor()
    processor_architecture = platform.architecture()
    python_version = platform.python_version()
    memory = psutil.virtual_memory().total
    memory_usage = psutil.virtual_memory().percent
    cpu_usage = psutil.cpu_percent()

    content = ("\n[操作系统]: " + os_name + "\n[系统版本]: " + os_version + "\n[开机时长]: " + str(format((time.time() - psutil.boot_time()) / 3600, ".1f")) + "h" +
               "\n[服务器时间]: \n" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) +
               "\n\n[CPU架构]: " + processor_architecture[0] + ", " + processor_architecture[1] +
               "\n[CPU占用]: " + str(cpu_usage) + "%" +
               "\n\n[物理内存]: " + str(format(memory / (1024 ** 3), ".1f")) + "GB" +
               "\n[内存占用]: " + str(memory_usage) + "%"
               "\n\n[Python版本]: " + python_version +
               "\n\n[Bot源码]: 请发送 /repo \n[联系我们]: cloverta@petalmail·com")
    await platform_info.finish(content)


def clean_temp_cache():
    """定时清理缓存文件"""
    path_list =  [temp_path, video_path]

    for folder_path in path_list:
        files = get_files_in_folder(folder_path)
        for file in files:
            os.remove(file)


def get_files_in_folder(folder_path: Path):
    return [Path(f) for f in glob.glob(str(folder_path / "*")) if Path(f).is_file()]
