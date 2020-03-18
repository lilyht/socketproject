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

serverIP = '127.0.0.1'
# serverIP = '172.28.179.111'
serverPort = 12000


def main():
    # 程序的开始，所有的窗口都由登陆界面（w1）衍生
    app = QApplication(sys.argv)
    w1 = loginWindow()  # w1表示登录窗口的对象
    w1.show()
    app.exec_()


# 登陆界面的类
class loginWindow(QMainWindow, Ui_loginWindow):

    def __init__(self, parent=None):
        super(loginWindow, self).__init__(parent)
        self.setupUi(self)

        # 一些变量
        self.user = ""
        self.password = ""
        self.regiUser = ""
        self.regiPassword = ""
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.settimeout(10) # 设置连接超时
        # time.sleep(2)
        # SOL_SOCKET: 65535  SO_KEEPALIVE: 8
        # self.client.settimeout(100)
        self.clientIP = ""
        self.clientPort = ""
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

    # 发送心跳包
    def sendHeartbeat(self):
        a = 0
        while True:
            time.sleep(4)
            a += 1
            keepconn = "已连接"+str(a*4)+"秒"
            self.client.send(bytes(keepconn, 'UTF-8'))  # 向服务端发送消息

    # 点击注册按钮时的响应
    def regi(self):
        self.w2.show()  # 注册界面弹出
        self.w2.confirmSignal.connect(self.recvRegi)  # 获取登陆界面的提交信息

    # 登录成功后的响应
    def pan(self, user, clientIP, clientPort):
        heart = threading.Thread(target=self.sendHeartbeat, args=())
        self.w3.show()  # 网盘界面弹出
        self.w3.user = user
        self.w3.clientIP = clientIP
        self.w3.clientPort = clientPort
        self.w3.usernameLine.setText(user)
        self.w3.ipLine.setText(clientIP)
        self.w3.portLine.setText(clientPort)

        heart.start()

        self.w3.clareSignal.connect(self.recvPanClare)  # 接收到网盘界面的资源声明
        self.w3.exitSignal.connect(self.recvPanExit)  # 接收到网盘界面的退出
        self.w3.listSignal.connect(self.recvPanShowList)  # 接收到网盘界面的显示文件列表

    # 接收注册界面传来的注册名和注册密码
    def recvRegi(self, text1, text2):
        self.regiUser = text1
        self.regiPassword = text2
        self.check2(self.regiUser, self.regiPassword)  # 传给客户端让它发送给服务器检测

    # 接收网盘界面的资源声明消息
    def recvPanClare(self, localFilePath):
        clareInfo = 'cl' + ' ' + localFilePath
        self.client.send(clareInfo.encode("UTF-8"))
        print('声明资源：'+localFilePath)

    # 接收网盘界面的显示文件列表消息
    def recvPanShowList(self):
        self.client.send("ls".encode("UTF-8"))
        print("请求显示文件列表")

    def recvPanExit(self):
        self.client.close()  # 断开连接
        self.close()  # 退出程序

    # 向服务器发送登录输入的账号密码，检查是否正确，如果正确则跳转界面，否则提示错误
    def check(self):
        self.user = self.userLine.text()
        self.password = self.passwordLine.text()
        userinfo = 'log' + ' ' + self.user + ' ' + self.password
        print(userinfo)
        if self.user == "":
            errorInfo = QMessageBox.information(self, "格式错误", "用户名不能为空！")
        elif self.password == "":
            errorInfo = QMessageBox.information(self, "格式错误", "密码不能为空！")
        else:

            print("客户端开始发送登录指令和用户名密码")

            self.client.send(userinfo.encode("UTF-8"))  # 客户端传递指令、用户名、密码

            reply = self.client.recv(1024)  # 接收服务器的回复
            reply = reply.decode(encoding='UTF-8')
            print(reply)
            if reply == "0":
                logInfo = QMessageBox.information(self, "登录反馈", "密码错误！")
            elif reply == "-1":
                logInfo = QMessageBox.information(self, "登录反馈", "用户不存在！")
            else:
                reply = reply.split()
                self.clientIP = reply[1]
                self.clientPort = reply[2]
                logInfo = QMessageBox.information(self, "登录反馈", "登录成功！")
                self.pan(self.user, self.clientIP, self.clientPort)  # 调用pan界面响应
                self.hide()  # 登录界面隐藏，但仍然能传递参数

    # 向服务器发送注册输入的账号密码，检查是否已经有注册的了，如果没有，把账号密码添加进数据库。
    def check2(self, regiUsertext, regiPasswordtext):

        regiuserinfo = 'regi' + ' ' + regiUsertext + ' ' + regiPasswordtext
        print(regiuserinfo)
        print("客户端开始发送注册指令和用户名密码")
        self.client.send(regiuserinfo.encode("UTF-8"))  # 客户端传递指令、用户名、密码
        reply = self.client.recv(1024)  # 接收服务器的回复
        reply = reply.decode(encoding='UTF-8')
        print(reply)
        if reply == "1":
            regiInfo = QMessageBox.information(self, "注册反馈", "注册成功！请移步登录")
            self.w2.close()
        elif reply == "0":
            regiInfo = QMessageBox.information(self, "注册反馈", "用户名已存在！")
        else:
            regiInfo = QMessageBox.information(self, "注册反馈", "出现未知错误！")


if __name__ == '__main__':
    main()

