# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5 import QtCore, QtGui, QtWidgets
# from Ui_loginWindow import *
# from PyQt5.QtCore import pyqtSignal
# from regiControl import regiWindow
# import gol
# from socket import *
#
# serverIP = '127.0.0.1'
# serverPort = 12000
#
# global user
# global password
# global client
#
# client = socket(AF_INET, SOCK_STREAM)
# client.connect((serverIP, serverPort))
#
# def main():
#     app = QApplication(sys.argv)
#     # client = socket(AF_INET, SOCK_STREAM)
#     # client.connect((serverIP, serverPort))
#     w1 = loginWindow()
#     w1.show()
#     app.exec_()
#
#
# def check(user, password):
#     global client
#     print(user, password)
#     client.send(user.encode("utf8"))
#     print(client.recv(1024))
#
# class loginWindow(QMainWindow, Ui_loginWindow):
#     loginSignal = pyqtSignal(str, str)  # 点击登录时发送账号密码给服务器验证
#
#     def __init__(self, parent=None):
#         super(loginWindow, self).__init__(parent)
#         self.setupUi(self)
#         self.regiwindow = regiWindow()
#         # 登录按钮相关
#         self.loginButton.clicked.connect(self.checkUP)  # 登录按钮点击时
#         # self.loginSignal.connect()  # 未完成，这个应该是要传给服务器的
#
#         # 注册按钮相关
#         self.regiButton.clicked.connect(self.regiwindow.recvShow)
#
#     # 发送用户名和密码
#     def checkUP(self):
#         global user
#         global password
#
#         user = self.userLine.text()
#         password = self.passwordLine.text()
#         check(user, password)
#
#
# if __name__ == '__main__':
#     main()
#
#
