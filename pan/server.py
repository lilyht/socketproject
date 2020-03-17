from socket import *
import MySQLdb
import threading
import datetime
# -*- coding: UTF-8 -*-

# serverIP = '127.0.0.1'
serverIP = '0.0.0.0'
serverPort = 12000


maxN = 5  # 最大连接数
buf = 2048
starttime = None
endtime = None

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
# 最大连接数
serverSocket.listen(maxN)


# 收发数据
def dealConn(conn, addr):
    # 获取客户发送的指令，如果登录成功则跳出循环
    while True:
        data = conn.recv(1024)  # 接收用户名和密码，中间空格分隔
        datastr = data.decode(encoding='utf-8')  # type: 'str'
        if datastr != "":
            print("收到有效消息")
            dstr = datastr.split()
            cmd = dstr[0]
            username = dstr[1]
            psw = dstr[2]

            if cmd == "regi":
                dealRegi(conn, addr, username, psw)
            if cmd == "log":
                print("接收到了登录指令，前往验证")
                user = dealLogin(conn, addr, username, psw)
                if user != "":
                    print("登录成功！")
                    recordConnThread = threading.Thread(target=checkConnection, args=(conn, addr))
                    recordConnThread.start()
                    break

    # GUI中登录之后会进入文件面板（网盘主面板），不会再回退到登陆界面。
    while True:
        data = conn.recv(1024)
        datastr = data.decode(encoding='utf-8')  # type: 'str'
        if datastr != "":
            dstr = datastr.split()
            cmd = dstr[0]

            print('Server received command: %s' % cmd)

            if cmd == "ls":
                dealLs(conn, addr, user)
            if cmd == "cd":
                dealCd(conn, addr, user)
            if cmd == "que":
                dealQue(conn, addr, user)


    conn.close()


def dealRegi(conn, addr, username, psw):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        cursor.execute("use pandb")
    except:
        print("Error: unable to use database!")

    # 使用execute方法执行SQL语句，查询密码是否匹配
    sql = "SELECT password FROM USER WHERE user = '%s'" % username
    try:
        cursor.execute(sql)
        res = cursor.fetchone()
        print("password in db:{}".format(res[0]))

        conn.send("0".encode("UTF-8"))  # 表里已经存在该用户名了，拒绝
        return None

    except:
        sql = "INSERT INTO USER (user, password) VALUES (%s, %s)"
        val = (username, psw)
        try:
            cursor.execute(sql, val)
            db.commit()
            print("插入成功")
            conn.send("1".encode("UTF-8"))
        except ValueError as e:
            print("--->", e)
            conn.send("-1".encode("UTF-8"))
            print("插入失败")
    return None


def dealCd(conn, addr, user):
    return None


def dealLs(conn, addr, user):
    return None


def dealQue(conn, addr, user):
    return None


def dealTr(conn, addr, user):
    return None


def dealLogin(conn, addr, username, psw):

    # print(username, psw)

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "", "pandb", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        cursor.execute("use pandb")
    except:
        print("Error: unable to use database!")

    # 使用execute方法执行SQL语句，查询密码是否匹配
    sql = "SELECT password FROM USER WHERE user = '%s'" % username

    cursor.execute(sql)
    res = cursor.fetchone()

    if res is None:
        conn.send("-1".encode("UTF-8"))
        return ""
    else:
        if res[0] == psw:
            reply = "1" + " " + addr[0] + " " + str(addr[1])
            conn.send(reply.encode("UTF-8"))
            return username
        else:
            # print("password in db:{}".format(res[0]))
            # print("输入的psw:{}".format(psw))
            conn.send("0".encode("UTF-8"))
            return ""


# x心跳检测保留函数
def checkConnection(conn, addr):
    global starttime
    serverSocket.settimeout(None)
    starttime = datetime.datetime.now()
    # print('client addr',addr)
    client_msg=conn.recv(1024)
    if client_msg.decode(encoding='utf-8') !=  "":
        # print('client msg: %s' %(str(client_msg,'utf-8')))
        print("msg from client {} : {}".format(addr, str(client_msg, 'utf-8')))
        keep_alive(conn, addr)


def keep_alive(conn, addr):
    global endtime
    a = 1
    while a == 1:
        try:
            serverSocket.settimeout(5)
            # print('---------------------------------')
            client_msg = conn.recv(1024) # 客户端发送过来的消息
            if client_msg.decode(encoding='utf-8') != "":
                print("msg from client {} : {}".format(addr, str(client_msg, 'utf-8')))
        except:
            a = 2
            endtime = datetime.datetime.now()
    # print('连接已断开，本次连接持续 %s 秒'%str((endtime - starttime).seconds))
    print("client {} 连接已断开，本次连接持续 {}秒".format(addr, str((endtime - starttime).seconds)))
    '''
    处理断开
    '''


def main():
    print("The server in ready to receive.")
    while True:
        # 接收到客户连接请求后，建立新的TCP连接套接字
        conn, addr = serverSocket.accept()
        print('Accept new connection from %s:%s...' % addr)

        thread = threading.Thread(target=dealConn, args=(conn, addr))
        thread.start()


if __name__ == '__main__':
    main()
