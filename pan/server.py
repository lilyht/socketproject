from socket import *
import MySQLdb
import threading
# -*- coding: UTF-8 -*-

serverIP = '127.0.0.1'
serverPort = 12000
maxN = 5  # 最大连接数
buf = 2048


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
    try:
        cursor.execute(sql)
        res = cursor.fetchone()
        # print("password in db:{}".format(res[0]))
        # print("输入的psw:{}".format(psw))

        if res[0] == psw:
            conn.send("1".encode("UTF-8"))
            return username
        else:
            conn.send("0".encode("UTF-8"))
            return ""
    except ValueError as e:
        print("--->", e)
        conn.send("-1".encode("UTF-8"))
    return ""


# x心跳检测保留函数
def checkConnection(conn, address):
    return ""


def keep_alive():
    return ""

def main():

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((serverIP, serverPort))
    # 最大连接数
    serverSocket.listen(maxN)

    print("The server in ready to receive.")

    while True:
        # 接收到客户连接请求后，建立新的TCP连接套接字
        conn, addr = serverSocket.accept()
        print('Accept new connection from %s:%s...' % addr)

        thread = threading.Thread(target=dealConn, args=(conn, addr))
        thread.start()


if __name__ == '__main__':
    main()
