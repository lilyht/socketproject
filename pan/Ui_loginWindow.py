# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(800, 584)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 360, 411, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        self.regiButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.regiButton.setObjectName("regiButton")
        self.horizontalLayout.addWidget(self.regiButton)
        self.exitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(270, 50, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 130, 391, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.userLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userLine.setObjectName("userLine")
        self.gridLayout.addWidget(self.userLine, 0, 1, 1, 1)
        self.userLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.userLabel.setFont(font)
        self.userLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 0, 0, 1, 1)
        self.paswordLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.paswordLabel.setFont(font)
        self.paswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.paswordLabel.setObjectName("paswordLabel")
        self.gridLayout.addWidget(self.paswordLabel, 1, 0, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 1, 1, 1, 1)
        loginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        loginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        self.exitButton.clicked.connect(loginWindow.close)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "MainWindow"))
        self.loginButton.setText(_translate("loginWindow", "登录"))
        self.regiButton.setText(_translate("loginWindow", "注册"))
        self.exitButton.setText(_translate("loginWindow", "退出"))
        self.title.setText(_translate("loginWindow", "丑陋的登录页面"))
        self.userLabel.setText(_translate("loginWindow", "user:"))
        self.paswordLabel.setText(_translate("loginWindow", "password:"))
