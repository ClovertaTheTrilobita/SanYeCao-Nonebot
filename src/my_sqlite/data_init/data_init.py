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



def todo_init():
    session = SqliteSqlalchemy().session
    # 检查某个表是否存在
    table_exists1 = session.execute(selectTodoTable).fetchone()
    table_exists2 = session.execute(selectUserList).fetchone()
    if table_exists1 and table_exists2:
        return print("用户待办表状态正常。")
    else:
        print("待办功能未初始化，开始执行初始化文件。")
        execute_init_file3()
        return ""


"""
执行初始化文件todo_init.py
"""
def execute_init_file3():
    # 拼接文件的完整路径
    file_path = os.getcwd() + "/src/my_sqlite/data_init/todo_init.py"
    init_file_path = os.path.join(os.path.dirname(__file__), file_path)
    try:
        # 执行初始化文件
        subprocess.run(["python", init_file_path], check=True)
        print("初始化文件已成功执行。")
    except subprocess.CalledProcessError as e:
        print(f"执行初始化文件时出错: {e}")



# 查询待办表是否存在
selectTodoTable = text(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='user_todo_list';")
selectUserList = text(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='user_list';")

