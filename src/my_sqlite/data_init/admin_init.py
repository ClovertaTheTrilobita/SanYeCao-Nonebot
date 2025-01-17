import sqlite3

# 连接到数据库，如果不存在则创建
conn = sqlite3.connect('chat_bot.db')
# 创建游标
c = conn.cursor()
# 创建表
c.execute("""

CREATE TABLE IF NOT EXISTS admin_list (
    user_id VARCHAR(100) PRIMARY KEY
);

""")