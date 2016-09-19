#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import sys
import zmq
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QApplication
from create_alarm import Ui_MainWindow, _translate

# from lesson_TThu import Ui_Dialog

def push():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:22334")

    alname = str(ui.lineEdit.text())
    aldesc = str(ui.textEdit.toPlainText())
    aldate = ui.calendarWidget.selectedDate().toPyDate()
    altime = ui.timeEdit.time().toPyTime()
    al_dict = {
        'alname': alname,
        'aldesc': aldesc,
        'aldate': aldate,
        'altime': altime
    }
    # print(al_dict)

    socket.send(pickle.dumps(al_dict))
    print(pickle.loads(socket.recv()))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    #def set_text_lineEdit():
    #    ui.lineEdit.setText(_translate("Dialog", "Привет, я окно", None))
    #QtCore.QObject.connect(ui.pushButton, QtCore.SIGNAL("clicked()"), set_text_lineEdit)
    QtCore.QObject.connect(ui.pushButton, QtCore.SIGNAL("clicked()"), push)

    window.show()

    sys.exit(app.exec_())

