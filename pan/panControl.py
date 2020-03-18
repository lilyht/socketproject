import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_panWindow import *
from PyQt5.QtCore import pyqtSignal


class panWindow(QMainWindow, Ui_panWindow):
    exitSignal = pyqtSignal(str)  # 点击确认时发送信号
    clareSignal = pyqtSignal(str)  # 资源声明信号
    listSignal = pyqtSignal(str)  # 显示文件列表信号

    def __init__(self, parent=None):
        super(panWindow, self).__init__(parent)
        self.setupUi(self)

        self.user = ""
        self.clientIP = ""
        self.clientPort = ""
        self.exitButton.clicked.connect(self.shutdown)
        self.declareButton.clicked.connect(self.getLocalPath)
        self.showButton.clicked.connect(self.showList)

    # 点击资源声明后打开本地文件夹并获取路径，并经过client发送到服务器插入
    def getLocalPath(self):
        clarePath = QtWidgets.QFileDialog.getOpenFileName(self, "资源声明", "~")
        print(clarePath[0])
        self.clareSignal.emit(clarePath[0])

    # 点击显示当前账号文件列表按钮响应
    def showList(self):
        self.listSignal.emit("")

    def shutdown(self):
        self.exitSignal.emit("-9")
        self.close()


