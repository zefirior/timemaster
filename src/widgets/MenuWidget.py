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

    class MainApp(QMainWindow):
        def __init__(self, width=400, height=400, left=400, top=400):
            super().__init__()
            self.resize(500, 500)
            self.menu = QWidget(self)
            self.menu.setGeometry(QtCore.QRect(200, 200, 100, 100))

    app = QApplication(sys.argv)
    main = MainApp()
    setuper = Ui_MenuWidget()
    setuper.setupUi(main.menu)
    menu_label = setuper.label

    ani = QtCore.QPropertyAnimation()

    with open('./menu.css') as css:
        main.setStyleSheet(css.read())
    # setuper.verticalLayoutWidget.setStyleSheet("background-color: rgba(30, 130, 230, 1);")
    # setuper.verticalLayoutWidget.setStyleSheet("border-radius: 0 30px 30px 0;")

    main.show()

    sys.exit(app.exec_())
