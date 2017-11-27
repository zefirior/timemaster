# from models.models import Menu
# from config.config import scoper
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore
from setup_MenuWidget import Ui_MenuWidget


class _MenuView(QWidget):
    def __init__(self, struct, parent=None):
        super().__init__(parent)
        self.struct = struct
        self.setupUI()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    class MainApp(QWidget, Ui_MenuWidget):
        icon_clicker = QtCore.pyqtSignal()

        def __init__(self, w=160, h=250, t=0, r=0):
            super().__init__()
            self.w = w
            self.h = h
            self.t = t
            self.r = r
            self.resize(500, 500)
            self.menu = QWidget(self)
            self.setupUi(self.menu)
            self.menu.setGeometry(QtCore.QRect(self.t, self.r, self.w, self.h))
            self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.w, self.h))

            # animation drive
            self.machine = QtCore.QStateMachine()
            self.state_open = QtCore.QState(self.machine)
            self.state_close = QtCore.QState(self.machine)

            # state_open
            self.state_open.assignProperty(self, 'size', QtCore.QSize(self.w, self.h))
            self.state_open.assignProperty(self.verticalLayoutWidget, 'size', QtCore.QSize(self.w, self.h))
            self.state_open.assignProperty(self.pushButton, 'hidder', 0)
            self.state_open.assignProperty(self.pushButton_2, 'hidder', 0)
            self.state_open.assignProperty(self.pushButton_3, 'hidder', 0)

            # state_close
            self.state_close.assignProperty(self, 'size', QtCore.QSize(50, self.h))
            self.state_close.assignProperty(self.verticalLayoutWidget, 'size', QtCore.QSize(50, self.h))
            self.state_close.assignProperty(self.pushButton, 'hidder', 1)
            self.state_close.assignProperty(self.pushButton_2, 'hidder', 1)
            self.state_close.assignProperty(self.pushButton_3, 'hidder', 1)

            # label become button
            self.label.mousePressEvent = lambda e:self.icon_clicker.emit()

            self.t_close = self.state_open.addTransition(self.icon_clicker, self.state_close)
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self, b'size', self.state_close))
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self.verticalLayoutWidget, b'size', self.state_close))
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self.pushButton, b'hidder', self.state_close))
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self.pushButton_2, b'hidder', self.state_close))
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self.pushButton_3, b'hidder', self.state_close))

            self.t_open = self.state_close.addTransition(self.icon_clicker, self.state_open)
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self, b'size', self.state_open))
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self.verticalLayoutWidget, b'size', self.state_open))
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self.pushButton, b'hidder', self.state_open))
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self.pushButton_2, b'hidder', self.state_open))
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self.pushButton_3, b'hidder', self.state_open))

            self.machine.setInitialState(self.state_open)

            self.machine.start()

    app = QApplication(sys.argv)
    main = MainApp()

    with open('./menu.css') as css:
        main.setStyleSheet(css.read())

    main.show()

    sys.exit(app.exec_())
