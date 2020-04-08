# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_changeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changeWindow(object):
    def setupUi(self, changeWindow):
        changeWindow.setObjectName("changeWindow")
        changeWindow.resize(709, 423)
        self.centralwidget = QtWidgets.QWidget(changeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 50, 291, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.reenterLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.reenterLabel.setObjectName("reenterLabel")
        self.gridLayout.addWidget(self.reenterLabel, 1, 0, 1, 1)
        self.newPswLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.newPswLine.setObjectName("newPswLine")
        self.gridLayout.addWidget(self.newPswLine, 0, 1, 1, 1)
        self.newPswLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.newPswLabel.setObjectName("newPswLabel")
        self.gridLayout.addWidget(self.newPswLabel, 0, 0, 1, 1)
        self.reenterLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.reenterLine.setObjectName("reenterLine")
        self.gridLayout.addWidget(self.reenterLine, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 200, 261, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.confirmButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout.addWidget(self.confirmButton)
        self.exitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        changeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(changeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 22))
        self.menubar.setObjectName("menubar")
        changeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(changeWindow)
        self.statusbar.setObjectName("statusbar")
        changeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(changeWindow)
        QtCore.QMetaObject.connectSlotsByName(changeWindow)

    def retranslateUi(self, changeWindow):
        _translate = QtCore.QCoreApplication.translate
        changeWindow.setWindowTitle(_translate("changeWindow", "MainWindow"))
        self.reenterLabel.setText(_translate("changeWindow", "再次输入："))
        self.newPswLabel.setText(_translate("changeWindow", "新的密码："))
        self.confirmButton.setText(_translate("changeWindow", "确认"))
        self.exitButton.setText(_translate("changeWindow", "取消"))
