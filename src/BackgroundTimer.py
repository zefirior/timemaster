# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta
import threading


# TODO: remove loop
class BackgroundTimer:

    def __init__(self, callable_get_next_point):
        self.__timer = None
        self.__caller = None
        self.__loop = False
        self.__loop_time = 1
        self.__point_getter = callable_get_next_point

    def clear(self):
        if self.__timer:
            self.__timer.cancel()
        self.__timer = None
        self.__caller = None

    def set_next_timer(self):
        self.clear()
        dttm, caller = self.__point_getter()
        if not dttm:
            if self.__loop:
                self.__timer = threading.Timer(self.__loop_time, self._loop_handler)
                self.__timer.start()
            return
        timeout = dttm.timestamp() - datetime.now().timestamp()
        if timeout < 0:
            if self.__loop:
                self.__timer = threading.Timer(self.__loop_time, self._loop_handler)
                self.__timer.start()
            return
        if callable(caller):
            self.__caller = caller
        else:
            if self.__loop:
                self.__timer = threading.Timer(self.__loop_time, self._loop_handler)
                self.__timer.start()
            return
        self.__timer = threading.Timer(timeout, self._timer_handler)
        self.__timer.start()

    def _timer_handler(self):
        if callable(self.__caller):
            self.__caller()
        self.set_next_timer()

    def is_sleeped(self):
        return self.__timer is None

    def set_next_point_callable(self, caller):
        self.__point_getter = caller

    def run_loop(self):
        self.__loop = True
        self.set_next_timer()

    def stop_loop(self):
        self.__loop = False
        self.clear()

    def _loop_handler(self):
        self.set_next_timer()


if __name__ == '__main__':

    from . import conf
    FILE_PATH = conf['Magic setting']['clock_path']

    times = []
    with open(FILE_PATH) as f:
        while True:
            row = f.readline().strip()
            if not row:
                break
            _, str_time = row.split('=', 2)
            times.append(datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S'))
        f.close()


    def wrapper(msg):
        def wrapped():
            print(msg)

        return wrapped


    l = [
        [datetime.now() - timedelta(seconds=3), wrapper('qwe1')],
        [datetime.now() + timedelta(seconds=3), wrapper('qwe2')],
        [datetime.now() + timedelta(seconds=4), wrapper('qwe4')],
        [datetime.now() + timedelta(seconds=7), wrapper('qwe6')],
    ]


    def get_printer():
        if not len(l):
            return None, None
        tm, caller = l.pop(0)

        return tm, caller


    TM = BackgroundTimer(get_printer)
    TM.run_loop()
    while len(l):
        time.sleep(1)
    # TM.set_next_timer()
    # time.sleep(7)
    TM.stop_loop()
    # TM.clear()
    print(1)
