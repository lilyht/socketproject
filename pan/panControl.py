import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from noteControl import noteWindow
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
        self.nw = noteWindow()  # 备注窗口
        self.fileInfo = ""

        self.nw.noteSignal.connect(self.recvNoteAndSendAll)  # 接收备注文本

        self.exitButton.clicked.connect(self.shutdown)
        self.declareButton.clicked.connect(self.getLocalFile)
        self.showButton.clicked.connect(self.showList)

    # 点击资源声明后打开本地文件夹并获取路径，并经过client发送到服务器插入
    def getLocalFile(self):
        clarePath = QtWidgets.QFileDialog.getOpenFileName(self, "资源声明", "~")
        absPath = clarePath[0]  # 绝对路径
        temp = absPath.split('/')
        filename = temp[-1]

        m = hashlib.md5()  # 声明一个md5库
        file = open(absPath, 'rb')  # 用二进制读取文件
        m.update(file.read())  # 编码
        file.close()
        file_md5 = m.hexdigest()  # 生成md5码
        # print(file_md5)

        self.fileInfo = absPath + " " + filename + " " + file_md5 + " "  # 不完整的资源信息
        self.nw.show()  # 显示备注填写框

    def recvNoteAndSendAll(self, notetext):
        if notetext != "":
            notetext = notetext.replace(' ', '-')
            self.fileInfo += notetext
        else:
            self.fileInfo += "NULL"

        self.clareSignal.emit(self.fileInfo)

    # 点击显示当前账号文件列表按钮响应
    def showList(self):
        self.listSignal.emit("")

    def shutdown(self):
        self.exitSignal.emit("-9")
        self.close()


