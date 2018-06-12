import logging
from PyQt5.QtWidgets import QWidget
from ui.continue_dialog import Ui_Form as cont_form
from ui.finish_dialog import Ui_Form as fin_form


class BaseDialog(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.main = app
        self.setupUi(self)
        self.setup_dialog()

    def setup_dialog(self):
        raise NotImplemented


class ContinueDialog(BaseDialog, cont_form):

    def setup_dialog(self):
        self.continue_button.clicked.connect(self.on_continue)
        self.cancel_button.clicked.connect(self.on_cancel)

    def display_alarm_name(self, name):
        self.cur_alarm_name.setText(name)

    def on_continue(self):
        logging.info('notificator continue')
        self.main.schedule_continue()

    def on_cancel(self):
        logging.info('notificator stop')
        self.main.schedule_stop()


class FinishDialog(BaseDialog, fin_form):

    def setup_dialog(self):
        self.button_ok.clicked.connect(self.on_ok)

    def on_ok(self):
        logging.info('recipe stop')
        self.main.schedule_stop()
