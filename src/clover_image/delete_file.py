import os


async def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
    except Exception as e:
        print(f"删除文件时发生错误: {e}")