# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 330, 411, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 40))
        self.loginButton.setStyleSheet("border-style: none;\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(1, 90, 255);\n"
"color: white;\n"
"font-weight: bold;\n"
"loginButton hover{\n"
"    background-color: rgb(53, 148, 255)\n"
"}\n"
"")
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        self.regiButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.regiButton.setMinimumSize(QtCore.QSize(0, 40))
        self.regiButton.setStyleSheet("border-style: none;\n"
"background-color: rgb(1, 90, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.regiButton.setObjectName("regiButton")
        self.horizontalLayout.addWidget(self.regiButton)
        self.exitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exitButton.setMinimumSize(QtCore.QSize(0, 40))
        self.exitButton.setStyleSheet("border-style: none;\n"
"background-color: rgb(53, 148, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(220, 60, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.title.setFont(font)
        self.title.setStyleSheet("font: 25 25pt \"Microsoft JhengHei UI Light\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 150, 391, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.paswordLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.paswordLabel.setFont(font)
        self.paswordLabel.setStyleSheet("font: 15pt \"Microsoft JhengHei UI Light\";")
        self.paswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.paswordLabel.setObjectName("paswordLabel")
        self.gridLayout.addWidget(self.paswordLabel, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.userLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet("font: 15pt \"Microsoft JhengHei UI Light\";")
        self.userLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.passwordLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwordLine.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border-bottom: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.passwordLine.setFrame(True)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 1, 1, 1, 1)
        self.userLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userLine.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border-bottom: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.userLine.setObjectName("userLine")
        self.gridLayout.addWidget(self.userLine, 0, 1, 1, 1)
        loginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
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
        self.loginButton.setText(_translate("loginWindow", "LOGIN"))
        self.regiButton.setText(_translate("loginWindow", "SIGN UP"))
        self.exitButton.setText(_translate("loginWindow", "SIGN OUT"))
        self.title.setText(_translate("loginWindow", "个人云盘登录页面"))
        self.paswordLabel.setText(_translate("loginWindow", "Password"))
        self.userLabel.setText(_translate("loginWindow", "User Name"))
