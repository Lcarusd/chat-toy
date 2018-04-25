import MySQLdb

import main

# 创建连接
conn = MySQLdb.Connect(
    host='localhost',  # 主机名
    port=3306,  # 端口号(默认的)
    user='root',  # 用户名
    passwd='19950925',  # 密码
    db='chattoy',  # 数据库名
    charset='utf8',  # 这里设置编码是为了输出中文
)

# 获取cursor
cur = conn.cursor()

# 创建sql语句
sql = 'create table friends (id varchar(20) primary key, name varchar(20))'

# 执行sql语句
# 这里的a返回的是结果有多少行，执行这条语句后游标在第一条结果前。
a = cur.execute(sql)

i = main.text_reply()

print(i)
print('ddddddd')

sql = 'insert into user (id, name) values ( % s, % s)', [
    '1', i]

# 关闭连接对象
cur.close()
conn.close()

print("执行成功！")
