import sys
import gol
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from Ui_loginWindow import *
from regiControl import regiWindow
from panControl import panWindow
from socket import *
import time
import threading
import json
import os

serverIP = '127.0.0.1'
# serverIP = '172.28.161.66'
# serverIP = '172.28.179.111'
serverPort = 12000
buf = 2048


def main():
    # 程序的开始，所有的窗口都由登陆界面（w1）衍生
    app = QApplication(sys.argv)
    w1 = loginWindow()  # w1表示登录窗口的对象
    w1.show()
    app.exec_()


# 登陆界面的类
class loginWindow(QMainWindow, Ui_loginWindow):
    fileInfoSignal = pyqtSignal(list)  # 回传我的文件信息
    userInfoSignal = pyqtSignal(list)  # 回传user信息

    def __init__(self, parent=None):
        super(loginWindow, self).__init__(parent)
        self.setupUi(self)

        # 一些变量
        self.user = ""
        self.password = ""
        self.regiUser = ""
        self.regiPassword = ""
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.settimeout(10)  # 设置连接超时
        # time.sleep(2)
        # SOL_SOCKET: 65535  SO_KEEPALIVE: 8
        # self.client.settimeout(100)
        self.alive = True

        self.client.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)  # 在客户端开启心跳维护
        self.client.connect((serverIP, serverPort))

        # 子窗口对象
        self.w2 = regiWindow()
        self.w3 = panWindow()

        # 点击登录按钮时，启动checkUP，把用户名密码发送到client，并交给server检验
        self.loginButton.clicked.connect(self.check)
        # 点击注册按钮时，弹出注册界面
        self.regiButton.clicked.connect(self.regi)
        # 输入密码按回车键也是跳转到检验函数
        self.passwordLine.returnPressed.connect(self.check)
        # 回传我的文件信息到网盘界面
        self.fileInfoSignal.connect(self.w3.recvFileInfo)
        # 回传user信息到网盘界面
        self.userInfoSignal.connect(self.w3.recvUserInfo)
        # 退出程序
        self.exitButton.clicked.connect(self.recvExit)

    def dealConn(self):
        while True:
            # time.sleep(3)
            data = self.client.recv(buf)
            datastr = data.decode(encoding='UTF-8')  # type: 'str'
            if datastr != "":
                dstr = datastr.split('&&&')
                cmd = dstr[0]
                if cmd == "fl":  # 文件列表
                    fileList = dstr[1]
                    self.dealFileList(fileList)
                if cmd == "ul":  # 用户列表
                    userList = dstr[1]
                    self.dealUserList(userList)
                if cmd == "up":
                    filePath = dstr[1]
                    self.dealUpload(filePath)

    # 发送心跳包
    def sendHeartbeat(self):
        a = 0
        while True:
            time.sleep(4)
            a += 1
            keepconn = "kc 已连接"+str(a*4)+"秒"
            # self.client.send(bytes(keepconn, 'UTF-8'))  # 向服务端发送消息
            self.client.send(keepconn.encode("UTF-8"))

    # 点击注册按钮时的响应
    def regi(self):
        self.w2.show()  # 注册界面弹出
        self.w2.confirmSignal.connect(self.recvRegi)  # 获取登陆界面的提交信息

    # 登录成功后的响应
    def pan(self, user):
        heart = threading.Thread(target=self.sendHeartbeat, args=())
        recvServer = threading.Thread(target=self.dealConn, args=())
        self.w3.show()  # 网盘界面弹出
        self.w3.user = user
        self.w3.usernameLine.setText(user)

        heart.start()
        recvServer.start()

        self.w3.clareSignal.connect(self.recvPanClare)  # 接收到网盘界面的资源声明
        self.w3.exitSignal.connect(self.recvExit)  # 接收到网盘界面的退出
        self.w3.listSignal.connect(self.recvPanShowList)  # 接收到网盘界面的显示文件列表
        self.w3.searchSignal.connect(self.recvPanSearchUser)  # 接收到网盘搜索资源持有者
        self.w3.querySignal.connect(self.recvPanQueryFile)  # 接收到网盘请求获取资源

    # 接收注册界面传来的注册名和注册密码
    def recvRegi(self, text1, text2):
        self.regiUser = text1
        self.regiPassword = text2
        self.check2(self.regiUser, self.regiPassword)  # 传给客户端让它发送给服务器检测

    # 接收网盘界面的资源声明消息
    def recvPanClare(self, localFileInfo):
        clareInfo = 'cl' + ' ' + localFileInfo
        self.client.send(clareInfo.encode("UTF-8"))
        # print(clareInfo)
        # waste = self.client.recv(buf)  # 接收冗余回复（插入资源信息表的反馈）

    # 接收网盘界面的显示文件列表消息
    def recvPanShowList(self):
        self.client.send("ls".encode("UTF-8"))
        print("请求显示文件列表")
        # time.sleep(1)

    def dealFileList(self, fileList):
        # fileList = self.client.recv(buf)
        # fileList = fileList.decode("UTF-8")
        fileList = fileList.split("###")

        self.fileInfoSignal.emit(fileList)

    # 接收到网盘界面搜索资源持有者
    def recvPanSearchUser(self, filename):
        searchInfo = "sc" + ' ' + filename
        print("搜索资源：", filename)
        # time.sleep(1)
        self.client.send(searchInfo.encode("UTF-8"))

    def dealUserList(self, userList):
        # userList = self.client.recv(buf)
        # userList = userList.decode("UTF-8")
        userList = userList.split("***")

        self.userInfoSignal.emit(userList)

    def recvPanQueryFile(self, fileId, username):
        queryInfo = "qf" + ' ' + fileId + ' ' + username
        self.client.send(queryInfo.encode("UTF-8"))

    def recvExit(self):
        self.alive = False
        self.client.close()  # 断开连接
        self.close()  # 退出程序

    # 向服务器发送登录输入的账号密码，检查是否正确，如果正确则跳转界面，否则提示错误
    def check(self):
        self.user = self.userLine.text()
        self.password = self.passwordLine.text()

        if self.user == "":
            errorInfo = QMessageBox.critical(self, "格式错误", "用户名不能为空！")
        elif self.password == "":
            errorInfo = QMessageBox.critical(self, "格式错误", "密码不能为空！")
        else:
            # json格式封装用户信息
            userInfo = {
                'cmd': "log",
                'username': self.user,
                'psw': self.password
            }
            userInfoJson = json.dumps(userInfo)
            print("客户端开始发送登录指令和用户名密码")

            self.client.send(userInfoJson.encode("UTF-8"))  # 客户端传递指令、用户名、密码

            reply = self.client.recv(buf)  # 接收服务器的回复
            reply = reply.decode(encoding='UTF-8')
            print(reply)
            if reply == "0":
                logInfo = QMessageBox.critical(self, "登录反馈", "密码错误！")
            elif reply == "-1":
                logInfo = QMessageBox.critical(self, "登录反馈", "用户不存在！")
            else:
                logInfo = QMessageBox.information(self, "登录反馈", "登录成功！")
                # waste = self.client.recv(buf)  # 接收冗余回复（更新设备列表）
                self.pan(self.user)  # 调用pan界面响应
                self.hide()  # 登录界面隐藏，但仍然能传递参数

    # 向服务器发送注册输入的账号密码，检查是否已经有注册的了，如果没有，把账号密码添加进数据库。
    def check2(self, regiUsertext, regiPasswordtext):
        # json格式封装注册信息
        regiInfo = {
            'cmd': "regi",
            'username': regiUsertext,
            'psw': regiPasswordtext
        }
        regiInfoJson = json.dumps(regiInfo)
        print("客户端开始发送注册指令和用户名密码")
        self.client.send(regiInfoJson.encode("UTF-8"))  # 客户端传递指令、用户名、密码

        reply = self.client.recv(buf)  # 接收服务器的回复
        reply = reply.decode(encoding='UTF-8')
        print(reply)
        if reply == "1":
            regiInfo = QMessageBox.information(self, "注册反馈", "注册成功！请移步登录")
            # waste = self.client.recv(buf)  # 接收冗余回复（插入设备信息表的反馈）
            self.w2.close()
        elif reply == "0":
            regiInfo = QMessageBox.critical(self, "注册反馈", "用户名已存在！")
        else:
            regiInfo = QMessageBox.critical(self, "注册反馈", "出现未知错误！")

    def dealUpload(self, filePath):
        # 上传文件大小
        filetotal_size = os.path.getsize(filePath)
        # 上传文件名称
        file_name = os.path.basename(filePath)
        self.client.send(("alUp" + " " + filetotal_size + " " + file_name).encode("UTF-8"))
        send_size = 0
        print("filetotal_size: {}, file_name:{}".format(filetotal_size, file_name))
        f= open(filePath, 'rb')
        Flag = True
        while Flag:
            if send_size + 1024 >= filetotal_size:
                data = f.read(filetotal_size - send_size)
                Flag = False
            else:
                data = f.read(1024)
                send_size += 1024
            self.client.send(data)
        f.close()


if __name__ == '__main__':
    main()

