# from socket import *
# import MySQLdb
# import threading
# import datetime
# import json
# # -*- coding: UTF-8 -*-
#
# # serverIP = '127.0.0.1'
# serverIP = '0.0.0.0'
# serverPort = 12000
#
# maxN = 5  # 最大连接数
# buf = 2048
#
# serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.bind((serverIP, serverPort))
# # 最大连接数
# serverSocket.listen(maxN)
#
# global gloUser
# gloUser = ""
# global gloPath
# gloPath = ""
#
#
# # 收发数据
# def dealConn(conn, addr):
#     global gloUser
#     # 获取客户发送的指令，如果登录成功则跳出循环
#     serverSocket.settimeout(None)
#     while True:
#         data = conn.recv(1024)  # 接收用户名和密码，中间空格分隔
#         dataJson = data.decode(encoding='UTF-8')  # type: 'json'
#         if dataJson != "":
#             dataContent = json.loads(dataJson)  # 解析Json消息
#             # 提取消息内容
#             cmd = dataContent['cmd']
#             username = dataContent['username']
#             psw = dataContent['psw']
#
#             if cmd == "regi":
#                 dealRegi(conn, addr, username, psw)
#             if cmd == "log":
#                 print("接收到了登录指令，前往验证")
#                 user = dealLogin(conn, addr, username, psw)
#                 if user != "":
#                     print("登录成功！")
#                     starttime = datetime.datetime.now()
#                     currentUser = user
#                     # t = threading.Thread(target=checkUser, args=currentUser)
#                     # t.start()
#                     break
#
#     # GUI中登录之后会进入文件面板（网盘主面板），不会再回退到登陆界面。
#     while True:
#         if currentUser == gloUser:
#             print(currentUser, " 收到文件传输请求")
#             gloUser = ""
#         try:
#             serverSocket.settimeout(5)  # 网络故障时，会收不到消息，于是设置超时
#             data = conn.recv(1024)
#             if not data:  # 连接关闭时会导致持续接收空消息
#                 break
#             datastr = data.decode(encoding='UTF-8')  # type: 'str'
#
#             if datastr != "":
#                 dstr = datastr.split(' ')
#                 cmd = dstr[0]
#
#                 print('Server received command: %s' % cmd)
#                 if cmd == "cl":
#                     filepath = dstr[1]
#                     filename = dstr[2]
#                     md5 = dstr[3]
#                     finfo = dstr[4]
#                     dealCl(conn, addr, user, filepath, filename, md5, finfo)
#                 if cmd == "ls":
#                     dealLs(conn, addr, user)
#                 if cmd == "sc":
#                     # 客户端传来 "sc" + "资源名"
#                     fname = dstr[1]
#                     dealSc(conn, addr, user, fname)
#                 if cmd == "kc":
#                     kcInfo = dstr[1]
#                     # if kcInfo != "":
#                     print("msg from client {} : {}".format(addr, kcInfo))
#                 if cmd == "qf":
#                     fid = dstr[1]
#                     user = dstr[2]
#                     dealQf(conn, addr, fid, user)
#         except:
#             # 消息超时
#             break
#
#     # 无论收到空消息还是没收到消息，都打破循环跳转到这里
#     endtime = datetime.datetime.now()
#     print("client {} 连接已断开，本次连接持续 {}秒".format(addr, str((endtime - starttime).seconds)))
#
#     # 设备下线，更新设备信息表
#     db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
#     cursor = db.cursor()
#     try:
#         cursor.execute("use pandb")
#     except:
#         print("Error: unable to use database!")
#
#     sql1 = "UPDATE deviceinfo SET status=0 WHERE IP='{}' and port='{}'".format(addr[0], str(addr[1]))
#     try:
#         cursor.execute(sql1)
#         db.commit()
#         print("设备下线，更新设备信息列表成功")
#         # conn.send("1".encode("UTF-8"))
#     except ValueError as e:
#         print("--->", e)
#         # conn.send("-1".encode("UTF-8"))
#         print("设备下线，更新设备信息列表失败")
#     '''
#     处理断开
#     '''
#     conn.close()
#
#
# def dealRegi(conn, addr, username, psw):
#     # 打开数据库连接
#     db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#     try:
#         cursor.execute("use pandb")
#     except:
#         print("Error: unable to use database!")
#
#     # 使用execute方法执行SQL语句，查询密码是否匹配
#     sql = "SELECT password FROM USER WHERE user = '%s'" % username
#     flag = False
#     try:
#         cursor.execute(sql)
#         res = cursor.fetchone()
#         # print(res)
#         print("password in db:{}".format(res[0]))
#
#         conn.send("0".encode("UTF-8"))  # 表里已经存在该用户名了，拒绝
#         return None
#
#     except:
#         sql = "INSERT INTO USER (user, password) VALUES (%s, %s)"
#         val = (username, psw)
#         try:
#             cursor.execute(sql, val)
#             db.commit()
#             print("插入成功")
#             flag = True
#             conn.send("1".encode("UTF-8"))
#         except ValueError as e:
#             print("--->", e)
#             conn.send("-1".encode("UTF-8"))
#             print("插入失败")
#     print(flag)
#     if flag == True:
#         # 注册成功后将设备名插入设备信息列表(user, NULL, NULL, NULL, NULL)
#         sql = "INSERT INTO DeviceInfo (user) VALUES ('%s')" % username
#         try:
#             cursor.execute(sql)
#             db.commit()
#             print("插入设备信息表成功")
#             flag = True
#             conn.send("1".encode("UTF-8"))
#         except ValueError as e:
#             print("--->", e)
#             conn.send("-1".encode("UTF-8"))
#             print("插入设备信息表失败")
#
#     return None
#
#
# def dealCl(conn, addr, user, fpath, fname, ID, finfo):
#     db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#     try:
#         cursor.execute("use pandb")
#     except:
#         print("Error: unable to use database!")
#     print("dealCl")
#     # 使用execute方法执行SQL语句，插入资源信息
#     sql = "INSERT INTO ResourceInfo (ID, user, fname, fpath, note) VALUES (%s, %s, %s, %s, %s)"
#     val = (ID, user, fname, fpath, finfo)
#     try:
#         cursor.execute(sql, val)
#         db.commit()
#         print("插入资源信息成功")
#         conn.send("1".encode("UTF-8"))
#     except ValueError as e:
#         print("--->", e)
#         conn.send("-1".encode("UTF-8"))
#         print("插入资源信息失败")
#     return None
#
#
# def dealLs(conn, addr, user):
#     # 打开数据库连接
#     db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#     try:
#         cursor.execute("use pandb")
#     except:
#         print("Error: unable to use database!")
#
#     wholeInfo = ""
#
#     # 使用execute方法执行SQL语句，查询密码是否匹配
#     sql = "SELECT * FROM Resourceinfo WHERE user = '%s'" % user
#
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     print(res)
#     if len(res):
#         for one in res:
#             # print(one)
#             replyInfo = one[0] + " " + one[2] + " " + one[3] + " " + one[4]  # ID，文件名，绝对路径，备注
#             print(replyInfo)
#             wholeInfo += replyInfo + '###'  # 每个文件信息之间用三个#分割
#
#         wholeInfo = wholeInfo[:-3]  # 去掉结尾多出来的三个#
#         conn.send(wholeInfo.encode("UTF-8"))
#         print(wholeInfo)
#         return None
#     else:
#         print("NULL")
#         conn.send("NULL".encode("UTF-8"))
#         return None
#
#
# def dealSc(conn, addr, user, fname):
#     db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
#     cursor = db.cursor()
#     try:
#         cursor.execute("use pandb")
#     except:
#         print("Error: unable to use database!")
#         # 使用execute方法执行SQL语句，查询密码是否匹配
#     # sql = "SELECT * FROM Resourceinfo WHERE user = '%s'" % user
#     sql = "select r.ID, r.fpath, d.user, d.IP, d.port from resourceinfo r, deviceinfo d where r.fname='%s' and r.user=d.user" % fname
#     hasFileInfo = ""
#
#
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     # fetchall()不会报异常，因为它不是None，而是返回的是空列表，所以需要判断列表是否为空
#     if len(res):
#         for one in res:
#             # print(one)
#             replyInfo = one[0] + " " + one[1] + " " + one[2] + " " + one[3] + " " + one[4]  # ID，文件路径，user, IP, 端口号
#             print(replyInfo)
#             hasFileInfo += replyInfo + '***'  # 每个文件信息之间用三个#分割
#
#         hasFileInfo = hasFileInfo[:-3]  # 去掉结尾多出来的三个#
#         conn.send(hasFileInfo.encode("UTF-8"))
#         print(hasFileInfo)
#         return None
#     else:
#         print("NULL")
#         conn.send("NULL".encode("UTF-8"))
#         return None
#
#
# def dealLogin(conn, addr, username, psw):
#     # 是否在线
#     # print(username, psw)
#     # 打开数据库连接
#     db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#     try:
#         cursor.execute("use pandb")
#     except:
#         print("Error: unable to use database!")
#
#     # 使用execute方法执行SQL语句，查询密码是否匹配
#     sql = "SELECT password FROM USER WHERE user = '%s'" % username
#
#     cursor.execute(sql)
#     res = cursor.fetchone()
#
#     if res is None:
#         conn.send("-1".encode("UTF-8"))
#         return ""
#     else:
#         if res[0] == psw:
#             reply = "1"
#             conn.send(reply.encode("UTF-8"))
#
#             # 更新设备信息列表，设置为在线，并填写IP和端口号
#             # print(str(addr[1]))
#             portstr = str(addr[1])
#             sql1 = "UPDATE deviceinfo SET status=1, IP='{}', port='{}' WHERE user='{}'".format(addr[0], portstr,
#                                                                                                username)
#             try:
#                 cursor.execute(sql1)
#                 db.commit()
#                 print("更新设备信息列表成功")
#                 conn.send("1".encode("UTF-8"))
#             except ValueError as e:
#                 print("--->", e)
#                 conn.send("-1".encode("UTF-8"))
#                 print("更新设备信息列表失败")
#             return username
#         else:
#             # print("password in db:{}".format(res[0]))
#             # print("输入的psw:{}".format(psw))
#             conn.send("0".encode("UTF-8"))
#             return ""
#
#
# def dealQf(conn, addr, fid, user):
#     global gloUser
#     global gloPath
#     db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
#     cursor = db.cursor()
#     try:
#         cursor.execute("use pandb")
#     except:
#         print("Error: unable to use database!")
#     sql = "select distinct r.user, r.fpath from deviceinfo as d, resourceinfo as r where r.id = '{}' and r.user = '{}' and r.user = d.user and d.status = 1".format(fid, user)
#     cursor.execute(sql)
#     res = cursor.fetchone()
#     # 需要判断列表是否为空
#     if res is None:
#         # conn.send("-1".encode("UTF-8"))
#         print("ERROR")
#         return ""
#     else:
#         gloUser = res[0]
#         gloPath = res[1]
#         print("全局变量golUser、golPath已赋值")
#         print(gloPath)
#
#     return None
#
#
# def main():
#     print("The server in ready to receive.")
#     while True:
#         # 接收到客户连接请求后，建立新的TCP连接套接字
#         conn, addr = serverSocket.accept()
#         print('Accept new connection from %s:%s...' % addr)
#
#         thread = threading.Thread(target=dealConn, args=(conn, addr))
#         thread.start()
#
#
# if __name__ == '__main__':
#     main()
