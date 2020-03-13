import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_loginWindow import *
from PyQt5.QtCore import pyqtSignal
from regiControl import regiWindow
import gol
from socket import *

serverIP = '127.0.0.1'
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
        self.client.connect((serverIP, serverPort))

        self.w2 = regiWindow()

        # 点击登录按钮时，启动checkUP，把用户名密码发送到client，并交给server检验
        self.loginButton.clicked.connect(self.check)
        # 点击注册按钮时，弹出注册界面
        self.regiButton.clicked.connect(self.regi)

    # 点击注册按钮时的响应
    def regi(self):
        self.w2.show()  # 注册界面弹出
        self.w2.confirmSignal.connect(self.recvRegi)  # 添加槽

    # 类外接收注册界面传来的注册名和注册密码
    def recvRegi(self, text1, text2):

        self.regiUser = text1
        self.regiPassword = text2
        self.check2(self.regiUser, self.regiPassword)

    # 向服务器发送登录输入的账号密码，检查是否正确，如果正确则跳转界面，否则提示错误
    def check(self):
        self.user = self.userLine.text()
        self.password = self.passwordLine.text()
        userinfo = 'log' + ' ' + self.user + ' ' + self.password
        print(userinfo)
        if self.user == "":
            print("用户名不能为空！")
        elif self.password == "":
            print("密码不能为空！")
        else:

            print("客户端开始发送登录指令和用户名密码")

            self.client.send(userinfo.encode("UTF-8"))  # 客户端传递指令、用户名、密码

            reply = self.client.recv(1024)  # 接收服务器的回复
            reply = reply.decode(encoding='utf-8')
            print(reply)
            if reply == "1":
                print("隐藏登录窗口，并跳转到云盘主界面")
            elif reply == "0":
                print("提示密码错误")
            else:
                print("提示用户不存在")

    # 向服务器发送注册输入的账号密码，检查是否已经有注册的了，如果没有，把账号密码添加进数据库。
    def check2(self, regiUsertext, regiPasswodtext):
        print(regiUsertext, regiPasswodtext)
        self.client.send(regiUsertext.encode("UTF-8"))
        print(self.client.recv(1024))

        regiInfo = QMessageBox.information(self, "注册反馈", "注册成功，请返回登录")


if __name__ == '__main__':
    main()


