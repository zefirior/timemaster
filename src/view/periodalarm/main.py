# from core.mainUI import main
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore
from . import Ui_Form


class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._bind_param = {}
        self.table = None

    def bind(self, **kw):
        self._bind_param.update(kw)

    def get_param(self, key):
        return self._bind_param[key]

    def rerender(self):
        pass

    def renderView(self):

        # self.setGeometry(QtCore.QRect(9, 9, 400, 400))

        self.setuper = Ui_Form()
        self.setuper.setupUi(self)

