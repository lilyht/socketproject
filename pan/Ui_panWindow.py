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
        self.exitButton.setGeometry(QtCore.QRect(640, 500, 112, 32))
        self.exitButton.setObjectName("exitButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
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
