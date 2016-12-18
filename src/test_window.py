# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys



class MiniWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("mini hi")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnQuit = QPushButton("mini quit")
        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(QtCore.Qt.AlignTop)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(self.hide)


class MMWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("hi")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label2 = QLabel("hi2")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.btnQuit = QPushButton("quit")
        self.btndel = QPushButton("delete label")
        self.miniWindow = MiniWindow()
        self.miniWindow.setWindowTitle("mini window")
        self.miniWindow.resize(300, 70)
        self.miniWindow.hide()
        self.specialButton = QPushButton("call mini")
        self.vboxGlobal = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.specialButton)
        self.vbox.addWidget(self.btnQuit)
        # self.setLayout(self.vbox)
        self.vboxGlobal.addLayout(self.vbox)
        self.vbox2 = QVBoxLayout()
        self.vbox2.addWidget(self.label2)
        self.vbox2.addWidget(self.btndel)
        # self.setLayout(self.vbox2)
        self.vboxGlobal.addLayout(self.vbox2)
        self.setLayout(self.vboxGlobal)
        self.btnQuit.clicked.connect(qApp.quit)
        self.specialButton.clicked.connect(self.miniWindow.show)
        self.btndel.clicked.connect(self.ejectElement)
        self.widgets = []

    def ejectElement(self):
        while not self.vbox.isEmpty():
            item = self.vbox.takeAt(0)
            self.vbox.removeWidget(item.widget())
            self.vbox.removeItem(item)
            item.widget().setParent(None)
            self.vbox.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MMWindow()
    window.setWindowTitle("big window")
    window.resize(300, 70)
    window.show()

    sys.exit(app.exec_())
