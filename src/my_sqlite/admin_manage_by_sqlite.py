from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class SqliteSqlalchemy(object):
    def __init__(self):
        # 创建Sqlite连接引擎
        engine = create_engine('sqlite:///./chat_bot.db', echo=True)
        # 创建Sqlite的session连接对象
        self.session = sessionmaker(bind=engine)()

def insert_administrator(member_openid):
    session = SqliteSqlalchemy().session
    session.execute(insertAdminID, {'member_openid': member_openid})
    session.commit()
    session.close()

def check_admin_access(member_openid):
    session = SqliteSqlalchemy().session
    result = session.execute(selectAdminID, {'member_openid': member_openid}).fetchone()
    session.close()
    return result


def select_status(group_id):
    session = SqliteSqlalchemy().session
    result = session.execute(selectIsOn, {'group_id': group_id}).fetchone()
    session.close()
    return result

def update_ai_availability(group_id, is_on):
    session = SqliteSqlalchemy().session
    result = session.execute(selectGroupID, {'group_id': group_id}).fetchone()
    if result is None:
        session.execute(insertGroupID, {'group_id': group_id, 'is_on': is_on})
        session.commit()
    else:
        session.execute(updateIsOn, {'group_id': group_id, 'is_on': is_on})
        session.commit()
    session.close()

# 插入数据
insertAdminID = text("INSERT INTO admin_list (user_id) VALUES (:member_openid)")

# 查找用户
selectAdminID = text("SELECT * FROM admin_list WHERE user_id = :member_openid")

# 更新数据
selectIsOn = text("SELECT is_on FROM group_list WHERE group_id = :group_id")

# 更新数据
updateIsOn = text("UPDATE group_list SET is_on = :is_on WHERE group_id = :group_id")

# 查询是否已存该群
selectGroupID = text("SELECT * FROM group_list WHERE group_id = :group_id")

# 存储群聊ID
insertGroupID = text("INSERT INTO group_list (group_id, is_on) VALUES (:group_id, :is_on)")


if __name__ == "__main__":
    insert_administrator('1234')
    print(check_admin_access('1234'))