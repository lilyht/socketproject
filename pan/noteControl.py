import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_noteWindow import *
from PyQt5.QtCore import pyqtSignal


class noteWindow(QMainWindow, Ui_noteWindow):
    noteSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(noteWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendNote)

    def sendNote(self):
        note = self.noteLine.text()
        self.noteSignal.emit(note)
        self.close()

