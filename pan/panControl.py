import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_panWindow import *
from PyQt5.QtCore import pyqtSignal


class panWindow(QMainWindow, Ui_panWindow):
    exitSignal = pyqtSignal(str)  # 点击确认时发送信号

    def __init__(self, parent=None):
        super(panWindow, self).__init__(parent)
        self.setupUi(self)
        self.exitButton.clicked.connect(self.shutdown)

    def shutdown(self):
        self.exitSignal.emit("-9")
        self.close()

