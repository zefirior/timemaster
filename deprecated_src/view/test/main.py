# from core.mainUI import main
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore


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

        if self.table is None:

            #  setupUI
            self.table = QTableWidget(self)
            # self.table.setGeometry(QtCore.QRect(9, 9, 400, 400))
            data = self.get_param('data')
            self.table.setRowCount(len(data))
            self.table.setColumnCount(len(data[0]))
            for nrow, row in enumerate(data):
                for nitem, item in enumerate(row):
                    self.table.setItem(nrow, nitem, QTableWidgetItem(item))
            self.table.resizeColumnsToContents()



