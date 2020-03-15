# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_regiWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_regiWindow(object):
    def setupUi(self, regiWindow):
        regiWindow.setObjectName("regiWindow")
        regiWindow.resize(535, 400)
        regiWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(regiWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.regiLabel = QtWidgets.QLabel(self.centralwidget)
        self.regiLabel.setGeometry(QtCore.QRect(150, 20, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.regiLabel.setFont(font)
        self.regiLabel.setStyleSheet("font: 25 25pt \"Microsoft JhengHei UI Light\";")
        self.regiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.regiLabel.setObjectName("regiLabel")
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(160, 270, 100, 50))
        self.confirmButton.setStyleSheet("border-style: none;\n"
"background-color: rgb(1, 90, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.confirmButton.setObjectName("confirmButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(290, 270, 100, 50))
        self.exitButton.setStyleSheet("border-style: none;\n"
"background-color: rgb(53, 148, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.exitButton.setObjectName("exitButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 100, 341, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
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
        self.userLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userLine.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border-bottom: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.userLine.setObjectName("userLine")
        self.gridLayout.addWidget(self.userLine, 0, 1, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet("font: 15pt \"Microsoft JhengHei UI Light\";")
        self.passwordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.reenterLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reenterLabel.setFont(font)
        self.reenterLabel.setStyleSheet("font: 15pt \"Microsoft JhengHei UI Light\";")
        self.reenterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.reenterLabel.setObjectName("reenterLabel")
        self.gridLayout.addWidget(self.reenterLabel, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.reenterLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.reenterLine.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border-bottom: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.reenterLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reenterLine.setObjectName("reenterLine")
        self.gridLayout.addWidget(self.reenterLine, 2, 1, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwordLine.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border-bottom: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 1, 1, 1, 1)
        regiWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(regiWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 17))
        self.menubar.setObjectName("menubar")
        regiWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(regiWindow)
        self.statusbar.setObjectName("statusbar")
        regiWindow.setStatusBar(self.statusbar)

        self.retranslateUi(regiWindow)
        QtCore.QMetaObject.connectSlotsByName(regiWindow)

    def retranslateUi(self, regiWindow):
        _translate = QtCore.QCoreApplication.translate
        regiWindow.setWindowTitle(_translate("regiWindow", "MainWindow"))
        self.regiLabel.setText(_translate("regiWindow", "注册界面"))
        self.confirmButton.setText(_translate("regiWindow", "OK"))
        self.exitButton.setText(_translate("regiWindow", "BACK"))
        self.userLabel.setText(_translate("regiWindow", "User Name"))
        self.passwordLabel.setText(_translate("regiWindow", "Password"))
        self.reenterLabel.setText(_translate("regiWindow", "Re-enter"))
