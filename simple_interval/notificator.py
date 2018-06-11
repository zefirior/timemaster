import logging
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QRect


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


