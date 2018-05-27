# -*- coding: utf-8 -*-

import sys
import logging
from ui.interval_view import Ui_MainWindow
from core.task_launcher import TaskLauncher
# from core.mainUI import app, main, WindowSetuper
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSlot, QRect


class MainApp(QMainWindow):
    def __init__(self, width=400, height=400, left=400, top=400):
        super().__init__()
        self.title = 'mainApp'
        self.width = 400
        self.height = 400
        self.left = 400
        self.top = 200
        self.workspace = None
        self.views = {}


class Notificator(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setup()

        self.pushButton.clicked.connect(self.on_ok)
        self.pushButton_2.clicked.connect(self.on_cancel)

    def setup(self):
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(360, 100, 211, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

    def on_ok(self):
        logging.info('notificator continue')
        self.main.schedule_continue()

    def on_cancel(self):
        logging.info('notificator stop')
        self.main.schedule_stop()


class WindowSetuper(Ui_MainWindow):
    def __init__(self, main):
        super(WindowSetuper).__init__()
        self.main = main
        self.views = {}
        self.menu_button = {}

        self.setupUi(self.main)

        self.notificator = None
        self.tlauncher = TaskLauncher()
        self.work_state = False
        self.pushButton.clicked.connect(self.begin_scheduler)

        self.schedule = {
            #  id: [delay, name]
            1: [2, 'будильник 1'],
            2: [2, 'будильник 2'],
            3: [2, 'будильник 3'],
        }
        self.schedule_order = [1, 3, 2]
        self.cur_task_id = None
        self.cur_task_name = None
        # self.run_task(1)

    def run_task(self, id):
        if id not in self.schedule:
            return
        delay, name = self.schedule.get(id)
        logging.info('run task "{}"'.format(name))
        self.cur_task_id = id
        self.cur_task_name = name
        self.tlauncher.add_task(delay, self.on_timeout)

    def on_timeout(self):
        # self.work_state = False
        logging.info('run task "{}"'.format(self.cur_task_name))
        self.notificator = Notificator(self)
        self.notificator.show()
        # self.cur_task_id = None
        # self.cur_task_name = None

    def begin_scheduler(self):
        if self.work_state:
            return
        self.work_state = True
        task_id = self.schedule_order[0]
        self.run_task(task_id)

    def schedule_continue(self):
        logging.info('main continue')
        self.notificator.hide()
        self.notificator = None
        task_id = self.cur_task_id
        index = self.schedule_order.index(task_id)
        if index == len(self.schedule_order) - 1:
            self.work_state = False
            return
        next_task_id = self.schedule_order[index + 1]
        self.run_task(next_task_id)

    def schedule_stop(self):
        logging.info('main stop')
        self.notificator.hide()
        self.notificator = None
        self.work_state = False


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    app = QApplication(sys.argv)

    main = MainApp()
    w = WindowSetuper(main)
    main.show()

    sys.exit(app.exec_())
