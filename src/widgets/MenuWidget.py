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

    # def setupUI(self):



# class MenuWidget(object):
#     def __init__(self, scope):
#         self.conf = scoper(scope)
#         self._connection = self.conf.connection
#         self._session = self.conf.session
#
#     def get_menu_date(self):
#         menu_data = self._session.query(Menu).all()
#         return menu_data
#
#     def get_menu(self, parent=None):
#         pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    class MainApp(QMainWindow, Ui_MenuWidget):
        def __init__(self, w=160, h=250, t=200, r=200):
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

            self.hidder = QtCore.pyqtProperty(int, fset=self._hidder)
            self.hidder_2 = QtCore.pyqtProperty(int, fset=self._hidder)
            self.hidder_3 = QtCore.pyqtProperty(int, fset=self._hidder)

            # self.label.mouseReleaseEvent = lambda ev: self.label.emit(QtCore.SIGNAL('clicked()'))

            self.machine = QtCore.QStateMachine()
            self.state_open = QtCore.QState(self.machine)
            self.state_close = QtCore.QState(self.machine)
            self.machine.setInitialState(self.state_open)

            # state_open
            self.state_open.assignProperty(self, 'size', QtCore.QSize(self.w, self.h))
            self.state_open.assignProperty(self.verticalLayoutWidget, 'size', QtCore.QSize(self.w, self.h))
            self.state_open.assignProperty(self, 'hidder', [self.pushButton, 0])
            self.state_open.assignProperty(self, 'hidder_2', [self.pushButton_2, 0])
            self.state_open.assignProperty(self, 'hidder_3', [self.pushButton_3, 0])

            # state_close
            self.state_close.assignProperty(self, 'size', QtCore.QSize(50, self.h))
            self.state_close.assignProperty(self.verticalLayoutWidget, 'size', QtCore.QSize(50, self.h))
            self.state_close.assignProperty(self, 'hidder', [self.pushButton, 1])
            self.state_close.assignProperty(self, 'hidder_2', [self.pushButton_2, 1])
            self.state_close.assignProperty(self, 'hidder_3', [self.pushButton_3, 1])

            self.t_close = self.state_open.addTransition(self.label.linkActivated, self.state_close)
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self, b'size', self.state_close))
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self.verticalLayoutWidget, b'size', self.state_close))
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self, b'hidder', self.state_close))
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self, b'hidder_2', self.state_close))
            self.t_close.addAnimation(QtCore.QPropertyAnimation(self, b'hidder_3', self.state_close))

            self.t_open = self.state_open.addTransition(self.label.linkActivated, self.state_open)
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self, b'size', self.state_open))
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self.verticalLayoutWidget, b'size', self.state_open))
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self, b'hidder', self.state_open))
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self, b'hidder_2', self.state_open))
            self.t_open.addAnimation(QtCore.QPropertyAnimation(self, b'hidder_3', self.state_open))

            self.machine.start()

        def _hidder(self, obj):
            widg, hide_val = obj
            widg.setHidden(hide_val)


    app = QApplication(sys.argv)
    main = MainApp()
    # setuper = Ui_MenuWidget()
    # setuper.setupUi(main.menu)
    # menu_label = setuper.label

    # ani = QtCore.QPropertyAnimation()

    with open('./menu.css') as css:
        main.setStyleSheet(css.read())
    # setuper.verticalLayoutWidget.setStyleSheet("background-color: rgba(30, 130, 230, 1);")
    # setuper.verticalLayoutWidget.setStyleSheet("border-radius: 0 30px 30px 0;")

    main.show()

    sys.exit(app.exec_())
