import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_loginWindow import *
from PyQt5.QtCore import pyqtSignal
from regiControl import regiWindow
import gol
from socket import *

serverIP = '127.0.0.1'
serverPort = 12000

global user
global password
global client
global regiUser
global regiPassword

def main():
    # 程序的开始，所有的窗口都由登陆界面（w1）衍生
    app = QApplication(sys.argv)
    w1 = loginWindow()  # w1表示登录窗口的对象
    w1.show()
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((serverIP, serverPort))
    app.exec_()


# 向服务器发送登录输入的账号密码，检查是否正确，如果正确则跳转界面，否则提示错误
def check(usertext, passwordtext):
    # global client
    print(usertext, passwordtext)
    client.send(usertext.encode("utf8"))
    print(client.recv(1024))

# 向服务器发送注册输入的账号密码，检查是否已经有注册的了，如果没有，把账号密码添加进数据库。
def check2(regiusertext, regipasswordtext):
    # global client
    print(regiusertext, regipasswordtext)
    client.send(regiusertext.encode("UTF-8"))
    print(client.recv(1024))


# 登陆界面的类
class loginWindow(QMainWindow, Ui_loginWindow):

    def __init__(self, parent=None):
        super(loginWindow, self).__init__(parent)
        self.setupUi(self)
        self.w2 = regiWindow()

        # 点击登录按钮时，启动checkUP，把用户名密码发送到client，并交给server检验
        self.loginButton.clicked.connect(self.checkUP)
        # 点击注册按钮时，弹出注册界面
        self.regiButton.clicked.connect(self.regi)

    # 点击注册按钮时的响应
    def regi(self):
        self.w2.show()
        self.w2.confirmSignal.connect(self.recvRegi)

    # 类外接收注册界面传来的注册名和注册密码
    def recvRegi(self, text1, text2):
        global regiUser
        global regiPassword
        regiUser = text1
        regiPassword = text2
        # print(regiUser, regiPassword)
        check2(regiUser, regiPassword)

    # 获取登陆界面输入的用户名密码，并传递到类外
    def checkUP(self):
        global user
        global password

        user = self.userLine.text()
        password = self.passwordLine.text()
        print(user, password)
        if user is "":
            print("用户名不能为空！")
        elif password is "":
            print("密码不能为空！")
        else:
            check(user, password)


if __name__ == '__main__':
    main()


