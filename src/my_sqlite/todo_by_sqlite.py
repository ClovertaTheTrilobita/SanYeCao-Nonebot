from sqlalchemy import Column, Integer, String, Date, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlite3


class SqliteSqlalchemy(object):
    def __init__(self):
        # 创建Sqlite连接引擎
        engine = create_engine('sqlite:///./chat_bot.db', echo=True)
        # 创建Sqlite的session连接对象
        self.session = sessionmaker(bind=engine)()


def user_exists(member_openid):
    """
    查询数据库中是否包括此用户。

    :param member_openid:
    :return: 若包含用户返回True，否则返回False
    """
    session = SqliteSqlalchemy().session
    result = session.execute(selectUserId,
                             {'member_openid': member_openid}).fetchone()
    session.close()
    if result is None:
        return False
    else:
        return True


def insert_user_todo_list(member_openid, content):
    """
    插入用户待办

    :param member_openid:
    :param content: 待办内容(str)
    :return:
    """
    session = SqliteSqlalchemy().session
    if not user_exists(member_openid):
        session.execute(insertUserId, {'member_openid': member_openid})

    session.execute(insertUserTodo, {'member_openid': member_openid, 'content': content})
    session.commit()
    session.close()


def get_user_todo_list(member_openid):
    """
    展示用户所有待办

    :param member_openid:
    :return: 数据库查询结果(Sequence)
    """
    if not user_exists(member_openid):
        return False
    session = SqliteSqlalchemy().session
    result = session.execute(selectUserTodo,
                             {'member_openid': member_openid}).fetchall()
    session.close()
    return result


def delete_user_todo(member_openid, del_line_num):
    """
    删除某用户指定行数的待办

    :param member_openid:
    :param del_line_num: 指定的行数(int)
    :return:
    """

    if not  user_exists(member_openid):
        return -1

    session = SqliteSqlalchemy().session
    todo_list_len = session.execute(checkUserTodoLength, {'member_openid': member_openid}).fetchone()
    max_length = int(str(todo_list_len).lstrip("(").rstrip(",)"))
    if del_line_num > max_length or del_line_num < 1:
        return 1

    session.execute(deleteUserTodo, {'member_openid': member_openid, 'del_line_num': del_line_num})
    session.commit()
    session.close()
    return 0

# 查找用户
selectUserId = text(
    "select * from user_list where user_id = :member_openid")

# 插入数据
insertUserTodo = text(
    "INSERT INTO user_todo_list (user_id, content) VALUES (:member_openid, :content)")

# 插入用户id
insertUserId = text("INSERT INTO user_list (user_id) VALUES (:member_openid)")

# 删除特定行的待办
deleteUserTodo = text(
    "DELETE FROM user_todo_list WHERE id=(SELECT id FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY id) AS row_number FROM (SELECT * FROM user_todo_list WHERE user_id = :member_openid)) WHERE row_number = :del_line_num)")

# 查询用户待办数
checkUserTodoLength = text(
    "SELECT COUNT(*) FROM user_todo_list WHERE user_id = :member_openid")

# 查找用户待办
selectUserTodo = text(
    "select content from user_todo_list where user_id = :member_openid")

if __name__ == '__main__':
    print('test:')
    # insert_user_todo_list('111', '123')
    # print(get_user_todo_list('111'))
    # del_line_num = '1'
    # delete_user_todo('111', int(del_line_num))
    # print(get_user_todo_list('111'))