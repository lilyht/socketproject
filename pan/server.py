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
    # 获取客户发送的指令
    print("开始处理连接")
    data = conn.recv(1024)  # 接收用户名和密码，中间空格分隔
    print(data.decode(encoding='utf-8'))
    datastr = data.decode(encoding='utf-8')  # type: 'str'
    dstr = datastr.split()
    cmd = dstr[0]
    username = dstr[1]
    psw = dstr[2]

    print("接收的指令是：", cmd)
    if cmd == "regi":
        dealRegi(conn, addr)
    if cmd == "log":
        print("接收到了登录指令")
        user = dealLogin(conn, addr, username, psw)
        if user != "":
            print("登录成功！")

    # GUI中登录之后会进入文件面板（网盘主面板），不会再回退到登陆界面。
    while True:
        cmd = conn.recv(buf)
        print('Server received command: %s' % cmd)

        if cmd == "ls":
            dealLs(conn, addr, user)
        if cmd == "cd":
            dealCd(conn, addr, user)
        if cmd == "que":
            dealQue(conn, addr, user)


    conn.close()


def dealRegi(conn, addr, user):
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

    print(username, psw)
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "yrp990716", "pandb", charset='utf8' )
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
        # print("输入的psw:{}".format(psw))

        if res[0] == psw:
            conn.send("1".encode("UTF-8"))
            return username
        else:
            conn.send("0".encode("UTF-8"))
            return ""
    except:
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
