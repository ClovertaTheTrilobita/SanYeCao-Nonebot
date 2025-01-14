from sqlalchemy import Column, Integer, String, Date, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker


def touch_count(member_openid):
    session = SqliteSqlalchemy().session
    #
    result = session.execute(selectTouchCount,
                             {'member_openid': member_openid}).scalar()
    session.close()
    return result


def touch(status):
    session = SqliteSqlalchemy().session
    result = session.execute(selectTouchContent,{'status': status}).fetchone()
    session.close()
    return result


def insert_touch_log(QrTouchLog):
    session = SqliteSqlalchemy().session
    session.execute(insertTouchLog,
                    {'touch_status': QrTouchLog.touch_status,
                     'reply_touch_content': QrTouchLog.reply_touch_content,
                     'member_openid': QrTouchLog.user_id})
    session.commit()
    session.close()
    return ""

# 申明基类对象
Base = declarative_base()

class QrTouch:
    __tablename__ = 'qr_touch'
    id = Column(Integer, primary_key=True)
    touch_status = Column(Integer)
    reply_touch_content = Column(String(255))

    def __repr__(self):
        return (
            "QrTouch(id:{},touch_status:{},reply_touch_content:{})" .format(
                self.id,
                self.touch_status,
                self.reply_touch_content
            ))

class QrTouchLog:
    __tablename__ = 'qr_touch_log'
    id = Column(Integer, primary_key=True)
    touch_status = Column(Integer)
    reply_touch_content = Column(String(255))
    user_id = Column(String(255))
    extract_time = Column(Date)

    def __repr__(self):
        return (
            "QrFortune(id:{},touch_status:{},reply_touch_content:{},user_id:{})" .format(
                self.id,
                self.touch_status,
                self.reply_touch_content,
                self.user_id))


class SqliteSqlalchemy(object):
    def __init__(self):
        # 创建Sqlite连接引擎
        engine = create_engine('sqlite:///./chat_bot.db', echo=True)
        # 创建Sqlite的session连接对象
        self.session = sessionmaker(bind=engine)()


# 查询初始化表是否存在
selectInit = text(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='qr_touch';")
# 查询回复内容
selectTouchContent = text("select * from qr_touch where touch_status = :status order by random() limit 1")
# 查询触摸次数
selectTouchCount = text(
    "select count(*) from qr_touch_log where user_id = :member_openid  and extract_time = date('now')")
# 插入日志表
insertTouchLog = text(
    "insert into qr_touch_log (touch_status, reply_touch_content,user_id,extract_time) values (:touch_status, :reply_touch_content, :member_openid,date('now'))")
