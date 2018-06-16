# -*- coding: utf-8 -*-

import sys
from ui.interval_view import Ui_MainWindow
from core.mainUI import app, main, WindowSetuper
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    # main = MainApp()
    w = WindowSetuper(main)
    main.show()

    sys.exit(app.exec_())
