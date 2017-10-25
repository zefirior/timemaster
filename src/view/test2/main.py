# from core.mainUI import main
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem


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

        if self.table is None:

            #  setupUI
            self.table = QTableWidget(self)
            data = self.get_param('data')
            self.table.setRowCount(len(data))
            self.table.setColumnCount(len(data[0]))
            for nrow, row in enumerate(data):
                for nitem, item in enumerate(row):
                    self.table.setItem(nrow, nitem, QTableWidgetItem(item))
            self.table.resizeColumnsToContents()



