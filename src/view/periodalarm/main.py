# from core.mainUI import main
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore
from . import Ui_Form
from core.BackgroundTimer import TaskLauncher


class Delay(QWidget):
    pass


class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._bind_param = {}
        self.table = None
        self.window = Delay()
        self.launcher = TaskLauncher()

    def bind(self, **kw):
        self._bind_param.update(kw)

    def get_param(self, key):
        return self._bind_param[key]

    def rerender(self):
        pass

    def renderView(self):

        # self.setGeometry(QtCore.QRect(9, 9, 400, 400))
        self.launcher.add_task(5, self.window.show)
        self.setuper = Ui_Form()
        self.setuper.setupUi(self)

