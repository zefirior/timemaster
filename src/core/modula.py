# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
from random import randint

class Modula(QWidget):
    def __init__(self):
        super().__init__()
        self.buttonsCase = QVBoxLayout()
        # self.generate_buttons(buttons)
        self.root = QFrame()
        self.frameLayout = QVBoxLayout(self.root)
        self.frameLayout.addStretch(1)
        # self.root.setGeometry()
        self.label = QLabel("hi")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.boxGlobal = QVBoxLayout()
        # self.boxGlobal.addWidget(self.label)
        # self.boxGlobal.addLayout(self.buttonsCase)
        # self.boxGlobal.addWidget(self.root)
        self.boxGlobal = QVBoxLayout()
        self.bodybox = QHBoxLayout()
        self.boxGlobal.addWidget(self.label)
        self.boxGlobal.addLayout(self.bodybox)
        self.bodybox.addLayout(self.buttonsCase)
        self.bodybox.addWidget(self.root)
        self.setLayout(self.boxGlobal)

    def inject(self):
        # if not isinstance(widget, QWidget):
        #     raise Exception
        some_button = QPushButton('some button' + str(randint(1, 9)))
        self.frameLayout.insertWidget(1, some_button)
        self.update()

    def eject(self):
        while not self.frameLayout.isEmpty():
            item = self.frameLayout.takeAt(0)
            self.frameLayout.removeWidget(item.widget())
            self.frameLayout.removeItem(item)
            item.widget().setParent(None)
            self.frameLayout.update()

        # lst_widget = self.root.children()
        # for widget in lst_widget:
        #     widget.setParent(None)
        #     del widget

    def generate_buttons(self, buttons):
        if not isinstance(buttons, list):
            raise Exception
        for k, v in buttons:
            button = QPushButton(k)
            self.buttonsCase.addWidget(button)
            if v is not None and callable(v):
                button.clicked.connect(v)
        self.buttonsCase.addStretch(1)

    def set_button(self, buttons):
        self.generate_buttons(buttons)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Modula()
    buttons = [['inject', window.inject], ['eject', window.eject], ['quit', qApp.quit], ]
    window.set_button(buttons)
    window.setWindowTitle("Application")
    window.setGeometry(300, 100, 600, 200)
    window.show()

    sys.exit(app.exec_())
