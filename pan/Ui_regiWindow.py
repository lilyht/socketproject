# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_regiWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
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
        self.regiLabel.setGeometry(QtCore.QRect(190, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.regiLabel.setFont(font)
        self.regiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.regiLabel.setObjectName("regiLabel")
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(160, 260, 100, 50))
        self.confirmButton.setObjectName("confirmButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(290, 260, 100, 50))
        self.exitButton.setObjectName("exitButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 90, 301, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.userLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.userLabel.setFont(font)
        self.userLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 0, 0, 1, 1)
        self.userLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userLine.setObjectName("userLine")
        self.gridLayout.addWidget(self.userLine, 0, 1, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)
        self.reenterLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.reenterLabel.setFont(font)
        self.reenterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.reenterLabel.setObjectName("reenterLabel")
        self.gridLayout.addWidget(self.reenterLabel, 2, 0, 1, 1)
        self.reenterLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.reenterLine.setObjectName("reenterLine")
        self.gridLayout.addWidget(self.reenterLine, 2, 1, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 1, 1, 1, 1)
        regiWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(regiWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 22))
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
        self.regiLabel.setText(_translate("regiWindow", "很丑的注册界面"))
        self.confirmButton.setText(_translate("regiWindow", "确认"))
        self.exitButton.setText(_translate("regiWindow", "返回"))
        self.userLabel.setText(_translate("regiWindow", "user:"))
        self.passwordLabel.setText(_translate("regiWindow", "password:"))
        self.reenterLabel.setText(_translate("regiWindow", "re-enter:"))
