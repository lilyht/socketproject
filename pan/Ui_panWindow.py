# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_panWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_panWindow(object):
    def setupUi(self, panWindow):
        panWindow.setObjectName("panWindow")
        panWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(panWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(610, 510, 112, 32))
        self.exitButton.setObjectName("exitButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 24 25pt \"Microsoft JhengHei UI Light\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.usernameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLine.setGeometry(QtCore.QRect(200, 100, 101, 31))
        self.usernameLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.usernameLine.setStyleSheet("font: 12pt \"Leelawadee UI Semilight\";\n"
"border-style: none;\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.usernameLine.setObjectName("usernameLine")
        self.searchLine = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLine.setGeometry(QtCore.QRect(70, 395, 191, 31))
        self.searchLine.setStyleSheet("font: 25 9pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.searchLine.setText("")
        self.searchLine.setObjectName("searchLine")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(530, 395, 191, 31))
        self.searchButton.setStyleSheet("font: 10pt \"Microsoft YaHei UI Light\";\n"
"background-color: rgb(1, 90, 255);\n"
"color: white;\n"
"font-weight: bold;\n"
"loginButton hover{\n"
"    background-color: rgb(53, 148, 255)\n"
"}\n"
"")
        self.searchButton.setObjectName("searchButton")
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(200, 510, 112, 32))
        self.showButton.setObjectName("showButton")
        self.declareButton = QtWidgets.QPushButton(self.centralwidget)
        self.declareButton.setGeometry(QtCore.QRect(70, 510, 112, 32))
        self.declareButton.setObjectName("declareButton")
        self.queryButton = QtWidgets.QPushButton(self.centralwidget)
        self.queryButton.setGeometry(QtCore.QRect(530, 440, 191, 31))
        self.queryButton.setStyleSheet("font: 10pt \"Microsoft YaHei UI Light\";\n"
"background-color: rgb(1, 90, 255);\n"
"color: white;\n"
"font-weight: bold;\n"
"loginButton hover{\n"
"    background-color: rgb(53, 148, 255)\n"
"}")
        self.queryButton.setObjectName("queryButton")
        self.queryIdLine = QtWidgets.QLineEdit(self.centralwidget)
        self.queryIdLine.setGeometry(QtCore.QRect(70, 440, 191, 31))
        self.queryIdLine.setStyleSheet("font: 25 9pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.queryIdLine.setText("")
        self.queryIdLine.setObjectName("queryIdLine")
        self.resultTable = QtWidgets.QTableView(self.centralwidget)
        self.resultTable.setGeometry(QtCore.QRect(70, 140, 661, 231))
        self.resultTable.setObjectName("resultTable")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 12pt \"Leelawadee UI Semilight\";\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.queryUserLine = QtWidgets.QLineEdit(self.centralwidget)
        self.queryUserLine.setGeometry(QtCore.QRect(270, 440, 191, 31))
        self.queryUserLine.setStyleSheet("font: 25 9pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.queryUserLine.setText("")
        self.queryUserLine.setObjectName("queryUserLine")
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(550, 100, 181, 31))
        self.changeButton.setStyleSheet("font: 10pt \"Microsoft YaHei UI Light\";\n"
"background-color: rgb(0, 155, 255);\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.changeButton.setObjectName("changeButton")
        panWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(panWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        panWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(panWindow)
        self.statusbar.setObjectName("statusbar")
        panWindow.setStatusBar(self.statusbar)

        self.retranslateUi(panWindow)
        QtCore.QMetaObject.connectSlotsByName(panWindow)

    def retranslateUi(self, panWindow):
        _translate = QtCore.QCoreApplication.translate
        panWindow.setWindowTitle(_translate("panWindow", "MainWindow"))
        self.exitButton.setText(_translate("panWindow", "退出"))
        self.label.setText(_translate("panWindow", "云盘主面板"))
        self.usernameLine.setText(_translate("panWindow", "用户名"))
        self.searchLine.setPlaceholderText(_translate("panWindow", "请输入资源名称"))
        self.searchButton.setText(_translate("panWindow", "搜索资源持有者"))
        self.showButton.setText(_translate("panWindow", "显示文件列表"))
        self.declareButton.setText(_translate("panWindow", "资源声明*"))
        self.queryButton.setText(_translate("panWindow", "获取资源*"))
        self.queryIdLine.setPlaceholderText(_translate("panWindow", "请输入文件ID"))
        self.label_2.setText(_translate("panWindow", "当前用户："))
        self.queryUserLine.setPlaceholderText(_translate("panWindow", "请输入持有者用户名"))
        self.changeButton.setText(_translate("panWindow", "修改密码"))
