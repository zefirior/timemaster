#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
from ui.interval_view import Ui_MainWindow
from config import MINUTE, TIC_PER_SECOND
from notificator import Notificator
from delay_thread import DelayThread
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainApp(QMainWindow):
    def __init__(self, width=400, height=400, left=400, top=400):
        super().__init__()
        self.title = 'mainApp'
        self.width = 400
        self.height = 400
        self.left = 400
        self.top = 200
        # self.workspace = None
        # self.views = {}


class TimeLauncher(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.notificator = Notificator(self)

        self.delay_thread = None
        self.work_state = False

        self.schedule = {
            #  id: [delay, name]
            1: [3, 'будильник 1'],
            2: [5, 'будильник 2'],
            3: [3, 'будильник 3'],
        }
        self.schedule_order = [1, 3, 2]
        self.cur_task_id = None
        self.cur_task_name = None

        # connections block
        self.begin_button.clicked.connect(self.begin_scheduler)
        self.pause_button.clicked.connect(self.on_pause)
        self.reset_button.clicked.connect(self.on_reset)
        # connections block

    def run_task(self, id):
        if id not in self.schedule:
            return
        delay, name = self.schedule.get(id)
        logging.info('run task "{}"'.format(name))
        self.cur_task_id = id
        self.cur_task_name = name
        self.delay_thread = DelayThread(delay)
        self.delay_thread.alarm_timeout.connect(self.on_timeout)
        self.delay_thread.alarm_tic.connect(self.on_tik)
        self.delay_thread.start()

    def on_timeout(self):
        logging.info('run task "{}"'.format(self.cur_task_name))
        self.notificator.General.show()

    def on_pause(self):
        if self.work_state:
            new_state = not self.delay_thread.pause
            self.delay_thread.pause = new_state

    def on_tik(self, number):
        minute_num = number // MINUTE
        second_num = number - minute_num * MINUTE
        self.lcd_minute.display(minute_num)
        self.lcd_second.display(second_num)

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
        self.lcd_second.display(0)
        self.lcd_minute.display(0)

    def on_reset(self):
        self.delay_thread.terminate()
        self.schedule_stop()


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    app = QApplication(sys.argv)

    window = TimeLauncher()
    window.show()

    sys.exit(app.exec_())
