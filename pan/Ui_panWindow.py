# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_panWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
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
        self.exitButton.setGeometry(QtCore.QRect(620, 460, 112, 32))
        self.exitButton.setObjectName("exitButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 25 25pt \"Microsoft JhengHei UI Light\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.resultText = QtWidgets.QTextEdit(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(300, 200, 401, 221))
        self.resultText.setObjectName("resultText")
        self.ipLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ipLine.setGeometry(QtCore.QRect(80, 180, 113, 21))
        self.ipLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ipLine.setObjectName("ipLine")
        self.portLine = QtWidgets.QLineEdit(self.centralwidget)
        self.portLine.setGeometry(QtCore.QRect(80, 210, 113, 21))
        self.portLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.portLine.setObjectName("portLine")
        self.usernameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLine.setGeometry(QtCore.QRect(80, 140, 113, 21))
        self.usernameLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.usernameLine.setObjectName("usernameLine")
        self.searchLine = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLine.setGeometry(QtCore.QRect(300, 100, 191, 31))
        self.searchLine.setStyleSheet("font: 25 9pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.searchLine.setObjectName("searchLine")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(520, 100, 171, 31))
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
        self.showButton.setGeometry(QtCore.QRect(460, 460, 112, 32))
        self.showButton.setObjectName("showButton")
        self.declareButton = QtWidgets.QPushButton(self.centralwidget)
        self.declareButton.setGeometry(QtCore.QRect(300, 460, 112, 32))
        self.declareButton.setObjectName("declareButton")
        self.queryButton = QtWidgets.QPushButton(self.centralwidget)
        self.queryButton.setGeometry(QtCore.QRect(520, 141, 171, 31))
        self.queryButton.setObjectName("queryButton")
        self.queryLine = QtWidgets.QLineEdit(self.centralwidget)
        self.queryLine.setGeometry(QtCore.QRect(300, 150, 191, 21))
        self.queryLine.setStyleSheet("font: 25 9pt \"微软雅黑 Light\";\n"
"")
        self.queryLine.setObjectName("queryLine")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(210, 80, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
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
        self.ipLine.setText(_translate("panWindow", "当前IP"))
        self.portLine.setText(_translate("panWindow", "当前端口"))
        self.usernameLine.setText(_translate("panWindow", "用户名"))
        self.searchLine.setText(_translate("panWindow", "搜索框"))
        self.searchButton.setText(_translate("panWindow", "搜索资源持有者"))
        self.showButton.setText(_translate("panWindow", "显示文件列表"))
        self.declareButton.setText(_translate("panWindow", "资源声明*"))
        self.queryButton.setText(_translate("panWindow", "获取资源*"))
        self.queryLine.setText(_translate("panWindow", "请求用户名"))
