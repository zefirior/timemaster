from icon import icons
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from .tomate_edit_setuper import Ui_Form as tomate_edit_setuper
from .tomate_view_setuper import Ui_Tomate_view as tomate_view_setuper
from core.utils import int_2_time_attr


class TomateEditView(QWidget, tomate_edit_setuper):
    up_signal = pyqtSignal(int)
    down_signal = pyqtSignal(int)
    minute_signal = pyqtSignal(int, int)
    second_signal = pyqtSignal(int, int)
    name_signal = pyqtSignal(int, str)
    add_signal = pyqtSignal(int)
    remove_signal = pyqtSignal(int)

    def __init__(self, app, tomate):
        super().__init__(app)
        self.app = app
        self.main = app
        self.tomate = tomate

        self.setupUi(self)
        self.setup_dialog()
        self.setup_icon()

    def setup_dialog(self):
        self.up.clicked.connect(self.on_up)
        self.down.clicked.connect(self.on_down)
        self.spin_minute.valueChanged.connect(self.on_minute_change)
        self.spin_second.valueChanged.connect(self.on_second_change)
        self.tomat_name.textChanged.connect(self.on_name_change)
        self.add.clicked.connect(self.on_add_tomate)
        self.remove.clicked.connect(self.on_remove_tomate)

    def setup_icon(self):
        icon_map = [
            (icons.up, self.up),
            (icons.down, self.down),
            (icons.add, self.add),
            (icons.remove, self.remove),
        ]

        for icon_path, widget in icon_map:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            widget.setIcon(icon)

    def on_up(self):
        self.up_signal.emit(self.tomate._self_id)

    def on_down(self):
        self.down_signal.emit(self.tomate._self_id)

    def on_minute_change(self, minute):
        self.minute_signal.emit(self.tomate._self_id, minute)

    def on_second_change(self, second):
        self.second_signal.emit(self.tomate._self_id, second)

    def on_name_change(self, name):
        self.name_signal.emit(self.tomate._self_id, name)

    def on_add_tomate(self):
        self.add_signal.emit(self.tomate._self_id)

    def on_remove_tomate(self):
        self.remove_signal.emit(self.tomate._self_id)


class TomateView(QWidget, tomate_view_setuper):
    def __init__(self, app, tomate):
        super().__init__(app)
        self.app = app
        self.main = app
        self.tomate = tomate

        self.setupUi(self)
        self.setup_tomate()

    def setup_tomate(self):
        self.tomat_name.setText(self.tomate.name)
        minute, second = int_2_time_attr(self.tomate.delay)
        self.minute.setText(str(minute))
        self.second.setText(str(second))

