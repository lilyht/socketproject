# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_changeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 30, 351, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.reenterLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.reenterLabel.setStyleSheet("font: 15pt")
        self.reenterLabel.setObjectName("reenterLabel")
        self.gridLayout.addWidget(self.reenterLabel, 1, 0, 1, 1)
        self.newPswLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.newPswLine.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border-bottom: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.newPswLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPswLine.setObjectName("newPswLine")
        self.gridLayout.addWidget(self.newPswLine, 0, 1, 1, 1)
        self.newPswLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.newPswLabel.setStyleSheet("font: 15pt")
        self.newPswLabel.setObjectName("newPswLabel")
        self.gridLayout.addWidget(self.newPswLabel, 0, 0, 1, 1)
        self.reenterLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        font.setStrikeOut(False)
        self.reenterLine.setFont(font)
        self.reenterLine.setStyleSheet("font: 25 12pt \"微软雅黑 Light\";\n"
"border-style: none;\n"
"border-bottom: 1px solid rgb(135, 135, 135);\n"
"background-color: rgba(255,255,255,0)\n"
"")
        self.reenterLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reenterLine.setObjectName("reenterLine")
        self.gridLayout.addWidget(self.reenterLine, 1, 1, 1, 1)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(190, 250, 171, 41))
        self.confirmButton.setStyleSheet("border-style: none;\n"
"background-color: rgb(1, 90, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"font-weight: bold;")
        self.confirmButton.setObjectName("confirmButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(360, 250, 181, 41))
        self.exitButton.setStyleSheet("border-style: none;\n"
"background-color: rgb(53, 148, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.exitButton.setObjectName("exitButton")
        changeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(changeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 17))
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
