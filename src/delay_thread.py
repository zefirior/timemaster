import logging
from config import TIC_PER_SECOND
from PyQt5.QtCore import QThread, pyqtSignal


class DelayThread(QThread):
    alarm_timeout = pyqtSignal()
    alarm_tic = pyqtSignal(int)
    tic_per_second = TIC_PER_SECOND
    tic = 1 / tic_per_second

    def __init__(self, delay):
        QThread.__init__(self)
        self.delay = delay
        self.pause = False

    def __del__(self):
        self.wait()

    def delay_generator(self, delay):
        for i in range(delay):
            for _ in range(self.tic_per_second):
                yield i

    def run(self):
        time_iter = self.delay_generator(self.delay)
        while True:
            logging.info(self.tic)

            self.msleep(self.tic * 1000)
            if self.pause:
                continue
            i = next(time_iter, None)
            if i is None:
                break
            self.alarm_tic.emit(self.delay - i)
        self.alarm_tic.emit(0)
        self.alarm_timeout.emit()


