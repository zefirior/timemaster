import logging
from config import MINUTE
from PyQt5.QtWidgets import QWidget
from ui.continue_dialog import Ui_Form as cont_form
from ui.finish_dialog import Ui_Form as fin_form
from ui.edit_interval import Ui_Form as editor_form
from ui.tomate_view import Ui_Form as tomate_form


class BaseWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.main = app
        self.setupUi(self)
        self.setup_dialog()

    def setup_dialog(self):
        raise NotImplemented


class ContinueDialog(BaseWidget, cont_form):

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


class FinishDialog(BaseWidget, fin_form):

    def setup_dialog(self):
        self.button_ok.clicked.connect(self.on_ok)

    def on_ok(self):
        logging.info('recipe stop')
        self.main.schedule_stop()


class RecipeEditorView(BaseWidget, editor_form):
    def setup_dialog(self):
        self.tomates = []

    def add_tomate(self, tomate):
        tomate_view = TomateView(self)
        tomate_view.tomat_name.setText(tomate.name)

        minute = tomate.delay // MINUTE
        second = tomate.delay - (minute * MINUTE)

        tomate_view.spin_minute.setValue(minute)
        tomate_view.spin_second.setValue(second)

        self.tomates.append(tomate_view)
        self.verticalLayout_2.addWidget(tomate_view)
        self.verticalLayout_2.insertWidget(0, tomate_view)


class TomateView(QWidget, tomate_form):

    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.main = app
        self.setupUi(self)
        self.setup_dialog()

    def setup_dialog(self):
        pass

