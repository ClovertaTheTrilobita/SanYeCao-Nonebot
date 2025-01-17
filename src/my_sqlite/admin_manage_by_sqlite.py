from sqlalchemy import Column, Integer, String, Date, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

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

# 插入数据
insertAdminID = text(
    "INSERT INTO admin_list (user_id) VALUES (:member_openid)")

# 查找用户
selectAdminID = text(
    "SELECT user_id FROM admin_list WHERE user_id = :member_openid")

if __name__ == "__main__":
    insert_administrator('1234')
    print(check_admin_access('1234'))