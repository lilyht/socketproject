
# x心跳检测保留函数
# def checkConnection(conn, addr, kcInfo):
#     global starttime
#     serverSocket.settimeout(None)
#     starttime = datetime.datetime.now()
#
#     client_msg = kcInfo
#
#     if client_msg != "":
#         # print('client msg: %s' %(str(client_msg,'UTF-8')))
#         # print("msg from client {} : {}".format(addr, str(client_msg, 'UTF-8')))
#         print("msg from client {} : {}".format(addr, client_msg))
#         keep_alive(conn, addr)


# def keep_alive(conn, addr, kcInfo):
#     # print(addr)
#     global endtime, starttime
#     a = 1
#
#     try:
#         serverSocket.settimeout(5)
#         # print('---------------------------------')
#         # client_msg = conn.recv(1024)  # 客户端发送过来的消息
#         if kcInfo != "":
#             print("msg from client {} : {}".format(addr, kcInfo))
#     except:
#         a = 2
#         endtime = datetime.datetime.now()

# print('连接已断开，本次连接持续 %s 秒'%str((endtime - starttime).seconds))

# print("client {} 连接已断开，本次连接持续 {}秒".format(addr, str((endtime - starttime).seconds)))
# # 设备下线，更新设备信息表
# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
# cursor = db.cursor()
# try:
#     cursor.execute("use pandb")
# except:
#     print("Error: unable to use database!")
#
# sql1 = "UPDATE deviceinfo SET status=0 WHERE IP='{}' and port='{}'".format(addr[0], str(addr[1]))
# try:
#     cursor.execute(sql1)
#     db.commit()
#     print("设备下线，更新设备信息列表成功")
#     conn.send("1".encode("UTF-8"))
# except ValueError as e:
#     print("--->", e)
#     conn.send("-1".encode("UTF-8"))
#     print("设备下线，更新设备信息列表失败")
# '''
# 处理断开
# '''

