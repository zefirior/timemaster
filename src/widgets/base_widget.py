from PyQt5.QtWidgets import QWidget


class BaseWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.main = app
        self.setupUi(self)
        self.setup_dialog()

    def setup_dialog(self):
        pass


