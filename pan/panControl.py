import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_panWindow import *
from PyQt5.QtCore import pyqtSignal


class panWindow(QMainWindow, Ui_panWindow):
    exitSignal = pyqtSignal(str)  # 点击确认时发送信号

    def __init__(self, parent=None):
        super(panWindow, self).__init__(parent)
        self.setupUi(self)

        self.user = ""
        self.clientIP = ""
        self.clientPort = ""
        self.exitButton.clicked.connect(self.shutdown)
        self.declareButton.clicked.connect(self.getLocalPath)


    # 点击资源声明后打开本地文件夹并获取路径
    def getLocalPath(self):
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, "资源声明", "~")
        print(filePath[0])

    def shutdown(self):
        self.exitSignal.emit("-9")
        self.close()


