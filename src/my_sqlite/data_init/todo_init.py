import sqlite3

# 连接到数据库，如果不存在则创建
conn = sqlite3.connect('chat_bot.db')
# 创建游标
c = conn.cursor()
#
c.execute("""DROP TABLE IF EXISTS user_todo_list;  """)
c.execute("""DROP TABLE IF EXISTS user_list;  """)
# 创建表
c.execute("""

CREATE TABLE user_list (
    user_id VARCHAR(100) PRIMARY KEY
);

""")
print("user_list created")

c.execute("""

CREATE TABLE user_todo_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id VARCHAR(100),
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES user_list(user_id)
);
        """)

