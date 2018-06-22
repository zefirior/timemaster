import logging
from .base_widget import BaseWidget
from .continue_setuper import Ui_Form as continue_setuper
from .finish_setuper import Ui_Form as finish_setuper


class ContinueDialog(BaseWidget, continue_setuper):

    def setup_dialog(self):
        self.continue_button.clicked.connect(self.on_continue)
        self.cancel_button.clicked.connect(self.on_cancel)

    def display_alarm_name(self, name):
        self.cur_alarm_name.setText(name)

    def on_continue(self):
        logging.info('notificator continue')
        self.main.setDisabled(False)
        self.main.schedule_continue()

    def on_cancel(self):
        logging.info('notificator stop')
        self.main.setDisabled(False)
        self.main.schedule_stop()

    def closeEvent(self, QCloseEvent):
        self.main.setDisabled(False)
        self.main.schedule_stop()


class FinishDialog(BaseWidget, finish_setuper):

    def setup_dialog(self):
        self.button_ok.clicked.connect(self.on_ok)

    def on_ok(self):
        logging.info('recipe stop')
        self.main.setDisabled(False)
        self.main.schedule_stop()

    def closeEvent(self, QCloseEvent):
        self.main.setDisabled(False)
        self.main.schedule_stop()

