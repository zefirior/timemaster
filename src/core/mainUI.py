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


class WindowSetuper(Ui_MainWindow):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.views = {}
        self.menu_button = {}

        self.setupUi(self.main)
        self.workspace = self.verticalFrame_2
        self.menu_build()

    def get_worklayout(self):
        return self.workspace.findChildren(QVBoxLayout, 'verticalLayout_5')[0]

    def clearWorkSpace(self):
        layout = self.get_worklayout(); print(layout.count())
        for childI in range(layout.count()):
            print('hidden ' + str(childI))
            layout.itemAt(childI).widget().setHidden(1)
            # layout.removeWidget(child)
            # child.setParent(None)
            # child.deleteLater()
            # self.workspace.setLayout(layout)

    @staticmethod
    def wrapView(name):
        return 'view' + str(name)

    def setWorkSpace(self, view):
        layout = self.get_worklayout()
        print(layout)
        layout.addWidget(view)
        # self.workspace.setLayout(layout)

    @staticmethod
    def getWidgetByName(layout, child_name):
        for chldI in range(layout.count()):
            w = layout.itemAt(chldI).widget()
            if w.objectName() == child_name:
                return w
            else:
                print(w.objectName())

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
        for section_name in controlmap:
            button = QtWidgets.QPushButton(self.verticalLayoutWidget)

            button.setObjectName(section_name)
            self.verticalLayout_4.addWidget(button)
            button.setObjectName("pushButton" + section_name)
            button.setText(section_name)
            button.section_name = section_name
            self.menu_button[section_name] = button

            button.clicked.connect(self.view_exec)



app = QApplication(sys.argv)
main = MainApp()
