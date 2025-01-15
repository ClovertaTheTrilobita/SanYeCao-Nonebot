import os
import subprocess
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Date, create_engine, text


class SqliteSqlalchemy(object):
    def __init__(self):
        # 创建Sqlite连接引擎
        engine = create_engine('sqlite:///./chat_bot.db', echo=True)
        # 创建Sqlite的session连接对象
        self.session = sessionmaker(bind=engine)()


def QrFortune_init():
    session = SqliteSqlalchemy().session
    # 检查某个表是否存在
    table_exists = session.execute(selectQrFortune).fetchone()
    session.close()
    if table_exists:
        return print("今日运势已初始化。")
    else:
        print("今日运势未初始化，开始执行初始化文件。")
        execute_init_file()
        return ""
"""
执行初始化文件for_init_database.py
"""
def execute_init_file():
    # 拼接文件的完整路径
    file_path = os.getcwd() + "\\src\\my_sqlite\\data_init\\fortune_init_data.py"
    init_file_path = os.path.join(os.path.dirname(__file__), file_path)
    try:
        # 执行初始化文件
        subprocess.run(["python", init_file_path], check=True)
        print("初始化文件已成功执行。")
    except subprocess.CalledProcessError as e:
        print(f"执行初始化文件时出错: {e}")

def touch_init():
    session = SqliteSqlalchemy().session
    # 检查某个表是否存在
    table_exists = session.execute(selectQrTouch).fetchone()
    if table_exists:
        return print("摸摸功能已初始化。")
    else:
        print("摸摸功能未初始化，开始执行初始化文件。")
        execute_init_file2()
        return ""

"""
执行初始化文件touch_init_data.py
"""
def execute_init_file2():
    # 拼接文件的完整路径
    file_path = os.getcwd() + "\\src\\my_sqlite\\data_init\\touch_init_data.py"
    init_file_path = os.path.join(os.path.dirname(__file__), file_path)
    try:
        # 执行初始化文件
        subprocess.run(["python", init_file_path], check=True)
        print("初始化文件已成功执行。")
    except subprocess.CalledProcessError as e:
        print(f"执行初始化文件时出错: {e}")

# 查询初始化表是否存在
selectQrFortune = text( "SELECT name FROM sqlite_master WHERE type='table' AND name='qr_fortune';")

# 查询初始化表是否存在
selectQrTouch = text(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='qr_touch';")