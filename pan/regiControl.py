import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_regiWindow import *
from PyQt5.QtCore import pyqtSignal


class regiWindow(QMainWindow, Ui_regiWindow):
    confirmSignal = pyqtSignal(str, str)  # 点击确认时发送信号

    def __init__(self, parent=None):
        super(regiWindow, self).__init__(parent)
        self.setupUi(self)
        self.confirmButton.clicked.connect(self.sendAndCheck)  # 确认按钮点击时，将注册名和注册密码传到client，并交给server检验
        self.exitButton.clicked.connect(self.close)
        self.reenterLine.returnPressed.connect(self.sendAndCheck)  # 输入确认密码后回车也是提交检验

    def sendAndCheck(self):
        user = self.userLine.text()
        password = self.passwordLine.text()
        reenter = self.reenterLine.text()
        if user == "":
            errorInfo = QMessageBox.critical(self, "格式错误", "用户名不能为空！")
        elif password == "":
            errorInfo = QMessageBox.critical(self, "格式错误", "密码不能为空！")
        elif reenter == "":
            errorInfo = QMessageBox.critical(self, "格式错误", "确认密码不能为空！")
        else:
            if password != reenter:
                errorInfo = QMessageBox.critical(self, "格式错误", "两次密码输入不一致！")
            else:
                print("发送给服务器进行检测")
                self.confirmSignal.emit(user, password)

