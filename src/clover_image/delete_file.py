import os
import asyncio
import shutil


async def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
    except Exception as e:
        print(f"删除文件时发生错误: {e}")


async def delete_file_batch(file_paths):
    """
      批量删除文件的异步函数（并行版本）

      :param file_paths: 需要删除的文件路径列表
      """
    tasks = [delete_file(path) for path in file_paths]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for path, result in zip(file_paths, results):
        if isinstance(result, Exception):
            print(f"删除 {path} 失败: {result}")

async def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except FileNotFoundError:
        print(f"文件夹 {folder_path} 不存在。")
    except Exception as e:
        print(f"删除文件夹时发生错误: {e}")