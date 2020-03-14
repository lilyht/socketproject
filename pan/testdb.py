#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version :")
print(data)

username = 'test1'
sql = "SELECT password FROM USER WHERE user = '%s'" % username
try:
    cursor.execute(sql)
    res = cursor.fetchone()
    print("password in db:{}".format(res[0]))

except:
    print("error")


# 关闭数据库连接
db.close()
