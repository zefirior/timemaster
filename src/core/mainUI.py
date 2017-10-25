# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QVBoxLayout
from PyQt5 import QtWidgets
from Ui_MainWindow import Ui_MainWindow
from core import controlmap


class MainApp(QMainWindow):
    def __init__(self, width=400, height=400, left=400, top=400):
        super().__init__()
        self.title = 'mainApp'
        self.width = 400
        self.height = 400
        self.left = 400
        self.top = 200
        self.workspace = None
        self.views = {}

    def get_worklayout(self):
        return self.workspace.findChildren(QVBoxLayout, 'verticalLayout_5')[0]

    def clearWorkSpace(self):
        layout = self.get_worklayout()
        for child in layout.children():
            child.hide()
            # layout.removeWidget(child)
            # child.setParent(None)
            # child.deleteLater()
            # self.workspace.setLayout(layout)

    def setWorkSpace(self, view):
        layout = self.get_worklayout()

        layout.addWidget(view)
        self.workspace.setLayout(layout)


class WindowSetuper(Ui_MainWindow):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.views = {}
        self.menu_button = {}

        self.setupUi(self.main)
        self.main.workspace = self.verticalFrame_2
        self.menu_build()

    def view_exec(self):
        sender = self.main.sender()
        section_name = sender.section_name

        if section_name in self.views:
            self.views[section_name].rerender()
        else:
            control = controlmap[section_name]
            self.main.clearWorkSpace()
            view = control.render(parent=self.main.workspace)
            self.views[section_name] = view
            self.main.setWorkSpace(view)

    def menu_build(self):
        for section_name in controlmap:
            button = QtWidgets.QPushButton(self.verticalLayoutWidget)

            button.setObjectName(section_name)
            self.verticalLayout_4.addWidget(button)
            self.menu_button[section_name] = button
            button.section_name = section_name

            button.clicked.connect(self.view_exec())



app = QApplication(sys.argv)
main = MainApp()
