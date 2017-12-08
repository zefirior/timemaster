# from models.models import Menu
# from config.config import scoper
from PyQt5 import QtWidgets as QW
from PyQt5 import QtCore
from .setup_MenuWidget import Ui_MenuWidget
import sys


class _HidButton(QW.QPushButton):

    @QtCore.pyqtProperty(int)
    def hidder(self):
        return self.isHidden()

    @hidder.setter
    def hidder(self, value):
        self.setHidden(value)


class MenuWidget(QW.QWidget, Ui_MenuWidget):
    icon_clicker = QtCore.pyqtSignal()

    def __init__(self, buttons, parent=None, t=0, r=0):
        super(MenuWidget, self).__init__(parent)
        button_height = 30
        self._buttons_meta = buttons
        self._buttons = []
        self.w = 160
        self.h = 100 + len(self._buttons_meta) * button_height
        self.t = t
        self.r = r

        #remove
        self.resize(500, 500)

        # self.menu = QW.QWidget(self)
        self.setupUi(self)
        # self.setupUi(self.menu)
        self.setGeometry(QtCore.QRect(self.t, self.r, self.w, self.h))
        # self.menu.setGeometry(QtCore.QRect(self.t, self.r, self.w, self.h))
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.w, self.h))

        self.button_fill()
        self.machine_prepare()

    def button_fill(self):
        for button_meta in self._buttons_meta:
            pushButton = _HidButton(self.verticalLayoutWidget)
            self._buttons.append(pushButton)
            pushButton.setObjectName("pushButton_" + button_meta['name'])
            pushButton.section_name = button_meta['name']
            pushButton.setText(button_meta['name'])
            self.verticalLayout_2.addWidget(pushButton)

            action = button_meta['action']
            if action is not None:
                pushButton.clicked.connect(action)

    def machine_prepare(self):
        # animation drive
        self.machine = QtCore.QStateMachine()
        self.state_open = QtCore.QState(self.machine)
        self.state_close = QtCore.QState(self.machine)

        # state_open
        self.state_open.assignProperty(self, 'size', QtCore.QSize(self.w, self.h))
        self.state_open.assignProperty(self.verticalLayoutWidget, 'size', QtCore.QSize(self.w, self.h))

        # state_close
        self.state_close.assignProperty(self, 'size', QtCore.QSize(50, self.h))
        self.state_close.assignProperty(self.verticalLayoutWidget, 'size', QtCore.QSize(50, self.h))

        # label become button
        self.label.mousePressEvent = lambda e:self.icon_clicker.emit()

        self.t_close = self.state_open.addTransition(self.icon_clicker, self.state_close)
        self.t_close.addAnimation(QtCore.QPropertyAnimation(self, b'size', self.state_close))
        self.t_close.addAnimation(QtCore.QPropertyAnimation(self.verticalLayoutWidget, b'size', self.state_close))

        self.t_open = self.state_close.addTransition(self.icon_clicker, self.state_open)
        self.t_open.addAnimation(QtCore.QPropertyAnimation(self, b'size', self.state_open))
        self.t_open.addAnimation(QtCore.QPropertyAnimation(self.verticalLayoutWidget, b'size', self.state_open))

        for button in self._buttons:
            self.state_open.assignProperty(button, 'hidder', 0)
            self.state_close.assignProperty(button, 'hidder', 1)
            self.t_close.addAnimation(QtCore.QPropertyAnimation(button, b'hidder', self.state_close))
            self.t_open.addAnimation(QtCore.QPropertyAnimation(button, b'hidder', self.state_open))

        self.machine.setInitialState(self.state_open)

        self.machine.start()

        with open('./menu.css') as css:
            self.setStyleSheet(css.read())

if __name__ == '__main__':

    def emit_action(_name):
        def printer():
            print(_name.upper())
        return printer

    buttons = []
    button_names = ['one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for name in button_names:

        buttons.append({'name': 'button ' + name.upper(), 'action': emit_action(name)})

    app = QW.QApplication(sys.argv)
    main = MenuWidget(buttons)

    with open('./menu.css') as css:
        main.setStyleSheet(css.read())

    main.show()

    sys.exit(app.exec_())
