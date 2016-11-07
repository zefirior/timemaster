# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

class MiniWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("mini hi")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnQuit = QtGui.QPushButton("mini quit")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), self.hide)


class MMWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("hi")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnQuit = QtGui.QPushButton("quit")
        self.miniWindow = MiniWindow()
        self.miniWindow.setWindowTitle("mini window")
        self.miniWindow.resize(300, 70)
        self.miniWindow.hide()
        self.specialButton = QtGui.QPushButton("call mini")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.specialButton)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        self.connect(self.specialButton, QtCore.SIGNAL("clicked()"), self.miniWindow.show)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MMWindow()
    window.setWindowTitle("big window")
    window.resize(300, 70)
    window.show()

    sys.exit(app.exec_())
