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
        self.exitButton.setGeometry(QtCore.QRect(630, 490, 112, 32))
        self.exitButton.setObjectName("exitButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 0, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.resultText = QtWidgets.QTextEdit(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(350, 160, 401, 251))
        self.resultText.setObjectName("resultText")
        self.ipLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ipLine.setGeometry(QtCore.QRect(60, 170, 113, 21))
        self.ipLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ipLine.setObjectName("ipLine")
        self.portLine = QtWidgets.QLineEdit(self.centralwidget)
        self.portLine.setGeometry(QtCore.QRect(60, 210, 113, 21))
        self.portLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.portLine.setObjectName("portLine")
        self.usernameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLine.setGeometry(QtCore.QRect(60, 140, 113, 21))
        self.usernameLine.setFocusPolicy(QtCore.Qt.NoFocus)
        self.usernameLine.setObjectName("usernameLine")
        self.searchLine = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLine.setGeometry(QtCore.QRect(360, 80, 191, 21))
        self.searchLine.setObjectName("searchLine")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(570, 70, 112, 32))
        self.searchButton.setObjectName("searchButton")
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(470, 490, 112, 32))
        self.showButton.setObjectName("showButton")
        self.declareButton = QtWidgets.QPushButton(self.centralwidget)
        self.declareButton.setGeometry(QtCore.QRect(310, 490, 112, 32))
        self.declareButton.setObjectName("declareButton")
        self.queryButton = QtWidgets.QPushButton(self.centralwidget)
        self.queryButton.setGeometry(QtCore.QRect(570, 120, 112, 32))
        self.queryButton.setObjectName("queryButton")
        self.queryLine = QtWidgets.QLineEdit(self.centralwidget)
        self.queryLine.setGeometry(QtCore.QRect(360, 120, 191, 21))
        self.queryLine.setObjectName("queryLine")
        panWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(panWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.label.setText(_translate("panWindow", "丑陋的网盘主面板"))
        self.ipLine.setText(_translate("panWindow", "当前IP"))
        self.portLine.setText(_translate("panWindow", "当前端口"))
        self.usernameLine.setText(_translate("panWindow", "用户名"))
        self.searchLine.setText(_translate("panWindow", "搜索框"))
        self.searchButton.setText(_translate("panWindow", "搜索资源持有者"))
        self.showButton.setText(_translate("panWindow", "显示文件列表"))
        self.declareButton.setText(_translate("panWindow", "资源声明*"))
        self.queryButton.setText(_translate("panWindow", "获取资源*"))
        self.queryLine.setText(_translate("panWindow", "请求用户名"))
