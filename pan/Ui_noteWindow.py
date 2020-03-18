# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_noteWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_noteWindow(object):
    def setupUi(self, noteWindow):
        noteWindow.setObjectName("noteWindow")
        noteWindow.resize(402, 213)
        self.centralwidget = QtWidgets.QWidget(noteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 110, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.noteLine = QtWidgets.QLineEdit(self.centralwidget)
        self.noteLine.setGeometry(QtCore.QRect(70, 60, 251, 31))
        self.noteLine.setObjectName("noteLine")
        self.noteLabel = QtWidgets.QLabel(self.centralwidget)
        self.noteLabel.setGeometry(QtCore.QRect(30, 30, 271, 16))
        self.noteLabel.setObjectName("noteLabel")
        noteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(noteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 22))
        self.menubar.setObjectName("menubar")
        noteWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(noteWindow)
        self.statusbar.setObjectName("statusbar")
        noteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(noteWindow)
        QtCore.QMetaObject.connectSlotsByName(noteWindow)

    def retranslateUi(self, noteWindow):
        _translate = QtCore.QCoreApplication.translate
        noteWindow.setWindowTitle(_translate("noteWindow", "MainWindow"))
        self.pushButton.setText(_translate("noteWindow", "提交"))
        self.noteLabel.setText(_translate("noteWindow", "请输入备注（可以为空，请不要出现字符 \'-\'）："))
