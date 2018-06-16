# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QVBoxLayout
from PyQt5 import QtWidgets
from Ui_MainWindow import Ui_MainWindow
from core import controlmap
from widgets import MenuWidget


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


class WindowSetuper(Ui_MainWindow):
    def __init__(self, main):
        super(WindowSetuper).__init__()
        self.main = main
        self.views = {}
        self.menu_button = {}

        self.setupUi(self.main)
        self.workspace = self.verticalFrame_2
        self.menu_build()

    def get_worklayout(self):
        return self.workspace.findChildren(QVBoxLayout, 'verticalLayout_5')[0]

    def clearWorkSpace(self):
        layout = self.get_worklayout()
        for childI in range(layout.count()):
            layout.itemAt(childI).widget().setHidden(1)

    @staticmethod
    def wrapView(name):
        return 'view' + str(name)

    def setWorkSpace(self, view):
        layout = self.get_worklayout()
        layout.addWidget(view)

    @staticmethod
    def getWidgetByName(layout, child_name):
        for chldI in range(layout.count()):
            w = layout.itemAt(chldI).widget()
            if w.objectName() == child_name:
                return w
            # else:
            #     print(w.objectName())

    def view_exec(self):
        sender = self.main.sender()
        section_name = sender.section_name
        self.clearWorkSpace()
        if section_name in self.views:
            self.views[section_name].rerender()
            w = self.getWidgetByName(self.get_worklayout(), self.wrapView(section_name))
            w.setHidden(0)
        else:
            control = controlmap[section_name]
            view = control.render(parent=self.workspace)
            self.views[section_name] = view
            view.setObjectName(self.wrapView(section_name))
            self.setWorkSpace(view)

    def menu_build(self):

        menu_line = [{'name': section_name, 'action': self.view_exec} for section_name in controlmap]

        self.menu = MenuWidget(menu_line, self.main, 0, 100)



app = QApplication(sys.argv)
main = MainApp()
