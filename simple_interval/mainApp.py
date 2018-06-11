# -*- coding: utf-8 -*-

import sys
import logging
from ui.interval_view import Ui_MainWindow
# from core.mainUI import app, main, WindowSetuper
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSlot, QRect, QThread, pyqtSignal
from PyQt5 import QtCore


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


class Notificator(object):
    def __init__(self, app):
        self.app = app
        self.main = app
        self.setup()

        self.pushButton.clicked.connect(self.on_ok)
        self.pushButton_2.clicked.connect(self.on_cancel)

    def setup(self):
        self.General = QWidget()
        self.General.setGeometry(QRect(360, 100, 211, 21))
        self.General.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.General)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QPushButton(self.General)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("continue")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.General)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("cancel")
        self.horizontalLayout.addWidget(self.pushButton_2)
        # QtCore.QMetaObject.connectSlotsByName(self.main)

    def on_ok(self):
        logging.info('notificator continue')
        self.main.schedule_continue()

    def on_cancel(self):
        logging.info('notificator stop')
        self.main.schedule_stop()


class DelayThread(QThread):
    signal = pyqtSignal()

    def __init__(self, delay):
        QThread.__init__(self)
        self.delay = delay

    def __del__(self):
        self.wait()

    def run(self):
        self.sleep(self.delay)
        self.signal.emit()


class TimeLauncher(MainApp, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.notificator = Notificator(self)

        self.delay_thread = None
        self.work_state = False

        self.schedule = {
            #  id: [delay, name]
            1: [2, 'будильник 1'],
            2: [2, 'будильник 2'],
            3: [2, 'будильник 3'],
        }
        self.schedule_order = [1, 3, 2]
        self.cur_task_id = None
        self.cur_task_name = None

        # connections block
        self.pushButton.clicked.connect(self.begin_scheduler)
        # connections block

    def run_task(self, id):
        if id not in self.schedule:
            return
        delay, name = self.schedule.get(id)
        logging.info('run task "{}"'.format(name))
        self.cur_task_id = id
        self.cur_task_name = name
        self.delay_thread = DelayThread(delay)
        self.delay_thread.signal.connect(self.on_timeout)
        self.delay_thread.start()

    def on_timeout(self):
        logging.info('run task "{}"'.format(self.cur_task_name))
        self.notificator.General.show()

    def begin_scheduler(self):
        if self.work_state:
            return
        self.work_state = True
        task_id = self.schedule_order[0]
        self.run_task(task_id)

    def schedule_continue(self):
        logging.info('main continue')
        self.notificator.General.hide()
        task_id = self.cur_task_id
        index = self.schedule_order.index(task_id)
        if index == len(self.schedule_order) - 1:
            self.work_state = False
            return
        next_task_id = self.schedule_order[index + 1]
        self.run_task(next_task_id)

    def schedule_stop(self):
        logging.info('main stop')
        self.notificator.General.hide()
        self.work_state = False


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    app = QApplication(sys.argv)

    window = TimeLauncher()
    window.show()

    sys.exit(app.exec_())
