import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from noteControl import noteWindow
from changeControl import changeWindow
from Ui_panWindow import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableView, QHeaderView, QMessageBox


class panWindow(QMainWindow, Ui_panWindow):
    exitSignal = pyqtSignal(str)  # 点击确认时发送信号
    clareSignal = pyqtSignal(str)  # 资源声明信号
    listSignal = pyqtSignal(str)  # 显示文件列表信号
    searchSignal = pyqtSignal(str)  # 搜索资源持有者信号
    querySignal = pyqtSignal(str, str)  # 资源请求信号（ID, user）
    changeSignal = pyqtSignal(str)  # 密码修改

    def __init__(self, parent=None):
        super(panWindow, self).__init__(parent)
        self.setupUi(self)

        self.user = ""
        self.nw = noteWindow()  # 备注窗口
        self.cp = changeWindow()  # 修改密码窗口
        self.fileInfo = ""

        # model1
        self.myFileModel = QStandardItemModel()  # 显示文件列表的model
        self.myFileModel.setHorizontalHeaderLabels(['ID', '文件名', '绝对路径', '备注'])
        # model2
        self.userModel = QStandardItemModel()  # 显示资源持有者列表的model
        self.userModel.setHorizontalHeaderLabels(['资源ID', '绝对路径', '用户名', 'IP地址', '端口号'])
        # 一个空model，用于初始化
        self.emptyModel = QStandardItemModel()  # 空的

        self.nw.noteSignal.connect(self.recvNoteAndSendAll)  # 接收备注文本
        self.cp.changeSignal.connect(self.recvNewPsw)  # 接收新密码

        # 槽函数
        self.exitButton.clicked.connect(self.shutdown)
        self.declareButton.clicked.connect(self.getLocalFile)
        self.showButton.clicked.connect(self.showList)
        self.searchButton.clicked.connect(self.searchUserByFilename)
        self.queryButton.clicked.connect(self.queryFile)
        self.changeButton.clicked.connect(self.changePsw)

    # 点击资源声明后打开本地文件夹并获取路径，并经过client发送到服务器插入
    def getLocalFile(self):
        clarePath = QtWidgets.QFileDialog.getOpenFileName(self, "资源声明", "~")
        absPath = clarePath[0]  # 绝对路径
        if absPath == '':  # 用户点击了取消
            return None
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

    # 接收备注信息并且将所有信息发送到父窗口
    def recvNoteAndSendAll(self, notetext):
        if notetext != "":
            notetext = notetext.replace(' ', '-')
            self.fileInfo += notetext
        else:
            self.fileInfo += "NULL"

        self.clareSignal.emit(self.fileInfo)

    def changePsw(self):
        self.cp.show()

    def recvNewPsw(self, newPsw):
        self.changeSignal.emit(newPsw)

    # 点击显示当前账号文件列表按钮响应
    def showList(self):
        # 初始化
        self.resultTable.setModel(self.emptyModel)
        self.listSignal.emit("")

    # 收到显示文件列表的反馈
    def recvFileInfo(self, wholeInfo):
        print("收到文件信息")
        print(wholeInfo)

        # 初始化模型
        self.myFileModel.clear()
        self.myFileModel.setHorizontalHeaderLabels(['ID', '文件名', '绝对路径', '备注'])

        if wholeInfo[0] != "NULL":
            # 在表中显示结果
            row = 0
            for info in wholeInfo:
                info = info.split(' ')
                for column in range(4):
                    item = QStandardItem(info[column])
                    self.myFileModel.setItem(row, column, item)
                row += 1

            self.resultTable.setModel(self.myFileModel)
            self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
            self.resultTable.verticalHeader().show()  # 显示行头
        else:
            print("无数据可显示")
            errorInfo = QMessageBox.critical(self, "消息", "无数据可显示！")

    # 点击搜索资源持有者
    def searchUserByFilename(self):
        filename = self.searchLine.text()
        self.searchSignal.emit(filename)

    # 收到user信息
    def recvUserInfo(self, userInfo):
        # print("收到user信息")
        # 初始化模型
        self.userModel.clear()
        self.userModel.setHorizontalHeaderLabels(['资源ID', '绝对路径', '用户名', 'IP地址', '端口号'])

        if userInfo[0] != "NULL":
            # 在表中显示结果
            row = 0
            for info in userInfo:
                info = info.split(' ')
                for column in range(5):
                    item = QStandardItem(info[column])
                    self.userModel.setItem(row, column, item)
                row += 1

            self.resultTable.setModel(self.userModel)
            self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
            self.resultTable.verticalHeader().show()  # 显示行头
        else:
            print("无数据可显示")
            errorInfo = QMessageBox.critical(self, "消息", "无数据可显示！")

    # 请求文件
    def queryFile(self):
        destId = self.queryIdLine.text()
        destUser = self.queryUserLine.text()
        if destUser == self.user:
            errInfo = QMessageBox.critical(self, "错误", "您不能向自己获取文件哦")
        self.querySignal.emit(destId, destUser)

    # 接收资源反馈
    def getFeedbackCl(self, feedback):
        if feedback == "1":
            okInfo = QMessageBox.information(self, "资源声明反馈", "声明成功！")
        else:
            error = QMessageBox.critical(self, "资源声明反馈", "出现未知错误，声明失败！")

    def shutdown(self):
        self.exitSignal.emit("-9")
        self.close()
