from sqlalchemy import Column, Integer, String, Date, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

class SqliteSqlalchemy(object):
    def __init__(self):
        # 创建Sqlite连接引擎
        engine = create_engine('sqlite:///./chat_bot.db', echo=True)
        # 创建Sqlite的session连接对象
        self.session = sessionmaker(bind=engine)()

def insert_administrator(member_openid, group_id):
    session = SqliteSqlalchemy().session
    session.execute(insertAdminID, {'member_openid': member_openid, 'group_id': group_id})
    session.commit()
    session.close()

def check_admin_access(member_openid,group_id):
    session = SqliteSqlalchemy().session
    result = session.execute(selectAdminID, {'member_openid': member_openid,'group_id': group_id}).fetchone()
    session.close()
    return result


def select_status(group_id):
    session = SqliteSqlalchemy().session
    result = session.execute(selectIsOn, {'group_id': group_id}).fetchone()
    session.close()
    return result

def update_administrator(group_id, is_on):
    session = SqliteSqlalchemy().session
    session.execute(updateIsOn, {'group_id': group_id, 'is_on': is_on})
    session.commit()
    session.close()

# 插入数据
insertAdminID = text("INSERT INTO admin_list (user_id,group_id) VALUES (:member_openid,:group_id)")

# 查找用户
selectAdminID = text("SELECT * FROM admin_list WHERE user_id = :member_openid")

# 更新数据
selectIsOn = text("SELECT is_on FROM admin_list WHERE group_id = :group_id")

# 更新数据
updateIsOn = text("UPDATE admin_list SET is_on = :is_on WHERE group_id = :group_id ")


if __name__ == "__main__":
    insert_administrator('1234')
    print(check_admin_access('1234'))