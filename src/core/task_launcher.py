# -*- coding: utf-8 -*-

import time
from itertools import count
from collections import namedtuple
import threading

TimerData = namedtuple('TimerData', ['timer', 'callback'])


class TaskLauncher:
    counter = count()

    def __init__(self):
        self._tasks = {}

    def add_task(self, delay, callback):
        task_id = next(self.counter)
        timer = threading.Timer(delay, self._task_wrapper(task_id))
        self._tasks[task_id] = TimerData(timer, callback)
        timer.start()
        return task_id

    def _task_wrapper(self, task_id):
        def wrap():
            callback = self._tasks[task_id].callback
            del self._tasks[task_id]
            return callback()
        return wrap

    def remove_task(self, task_id):
        if task_id not in self._tasks:
            return False
        self._tasks[task_id].timer.cancel()
        del self._tasks[task_id]
        return True


if __name__ == '__main__':

    def get_printer(*obj):
        def printer():
            print(*obj)
        return printer

    l = [
        [3, get_printer('qwe1')],
        [4, get_printer('qwe2')],
        [7, get_printer('qwe3')],
        [4, get_printer('qwe4')],
        [6, get_printer('qwe5')],
    ]


    def get_printer():
        if not len(l):
            return None, None
        tm, caller = l.pop(0)

        return tm, caller


    TL = TaskLauncher()
    ids = []
    for task in l:
        task_id = TL.add_task(*task)
        print(task_id)
        ids.append(task_id)

    time.sleep(4)

    for task_id in ids:
        print(TL.remove_task(task_id))

