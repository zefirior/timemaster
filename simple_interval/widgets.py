import logging
from config import MINUTE
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from ui.continue_dialog import Ui_Form as cont_form
from ui.finish_dialog import Ui_Form as fin_form
from ui.edit_interval import Ui_Form as editor_form
from ui.tomate_view import Ui_Form as tomate_form
from recipe_model import RecipeModel


class BaseWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.main = app
        self.setupUi(self)
        self.setup_dialog()

    def setup_dialog(self):
        pass


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
    def __init__(self, app):
        super().__init__(app)
        self.recipe = None
        self.tomates = []

    def setup_dialog(self):
        self.button_save.clicked.connect(self.save_recipe)
        self.lineEdit.textChanged.connect(self.on_recipe_change)

    def on_up(self, tomate_id):
        self.tomate_swap(tomate_id, up=True)

    def on_down(self, tomate_id):
        self.tomate_swap(tomate_id, up=False)

    def on_minute_change(self, tomate_id, minute):
        _, tomate = self.find_tomat_by_id(tomate_id)

        cur_delay = tomate.delay
        second = cur_delay % MINUTE

        tomate.delay = minute * MINUTE + second

    def on_second_change(self, tomate_id, second):
        _, tomate = self.find_tomat_by_id(tomate_id)

        cur_delay = tomate.delay
        minute = cur_delay // MINUTE

        tomate.delay = minute * MINUTE + second

    def on_name_change(self, tomate_id, name):
        _, tomate = self.find_tomat_by_id(tomate_id)
        tomate.name = name

    def on_recipe_change(self, name):
        self.recipe.name = name
        self.lineEdit.setText(self.recipe.name)

    def render_recipe(self, recipe_name):
        self.clear_editor()
        self.tomates = []

        self.recipe = RecipeModel.recipe_by_name(recipe_name)
        self.lineEdit.setText(self.recipe.name)

        tomates = self.sort_tomates(self.recipe.tomates())

        for tomate in tomates:
            self.tomates.append(tomate)
            self.add_tomate(tomate)

    @staticmethod
    def sort_tomates(tomates):
        return sorted(tomates, key=lambda t: t.tomate_order)

    def find_tomat_by_id(self, tomate_id):
        index = None
        finded_tomate = None
        for i, tomate in enumerate(self.tomates):
            if tomate.id_ == tomate_id:
                index = i
                finded_tomate = tomate

        if index is None:
            raise Exception('в эдиторе нет томата с id_={}'.format(tomate_id))

        return index, finded_tomate

    def rerender_recipe(self):
        self.clear_editor()
        for tomate in self.tomates:
            self.add_tomate(tomate)

    def clear_editor(self):
        layout = self.verticalLayout_2
        while layout.count() > 1:
            item = layout.takeAt(0)
            if not item:
                continue

            widg = item.widget()
            if widg:
                widg.deleteLater()

    def add_tomate(self, tomate):
        tomate_view = TomateView(self, tomate)
        tomate_view.tomat_name.setText(tomate.name)

        minute = tomate.delay // MINUTE
        second = tomate.delay - (minute * MINUTE)

        tomate_view.spin_minute.setValue(minute)
        tomate_view.spin_second.setValue(second)

        position = self.verticalLayout_2.count() - 1
        self.verticalLayout_2.insertWidget(position, tomate_view)
        tomate_view.up_signal.connect(self.on_up)
        tomate_view.down_signal.connect(self.on_down)
        tomate_view.minute_signal.connect(self.on_minute_change)
        tomate_view.second_signal.connect(self.on_second_change)
        tomate_view.name_signal.connect(self.on_name_change)

    def save_recipe(self):
        for tomate in self.tomates:
            tomate.update()
        self.recipe.update()
        self.hide()
        self.main.setDisabled(False)
        self.main.fill()

    def tomate_swap(self, tomate_id, up):
        shift = -1 if up else 1

        first_index, _ = self.find_tomat_by_id(tomate_id)

        second_index = first_index + shift
        if second_index < 0 or second_index >= len(self.tomates):
            return

        first_tomate = self.tomates[first_index]
        second_tomate = self.tomates[second_index]

        first_tomate.tomate_order, second_tomate.tomate_order = \
            second_tomate.tomate_order, first_tomate.tomate_order

        self.tomates = self.sort_tomates(self.tomates)
        self.rerender_recipe()


class TomateView(QWidget, tomate_form):
    up_signal = pyqtSignal(int)
    down_signal = pyqtSignal(int)
    minute_signal = pyqtSignal(int, int)
    second_signal = pyqtSignal(int, int)
    name_signal = pyqtSignal(int, str)

    def __init__(self, app, tomate):
        super().__init__(app)
        self.app = app
        self.main = app
        self.tomate = tomate

        self.setupUi(self)
        self.setup_dialog()

    def setup_dialog(self):
        self.up.clicked.connect(self.on_up)
        self.down.clicked.connect(self.on_down)
        self.spin_minute.valueChanged.connect(self.on_minute_change)
        self.spin_second.valueChanged.connect(self.on_second_change)
        self.tomat_name.textChanged.connect(self.on_name_change)

    def on_up(self):
        self.up_signal.emit(self.tomate.id_)

    def on_down(self):
        self.down_signal.emit(self.tomate.id_)

    def on_minute_change(self, minute):
        self.minute_signal.emit(self.tomate.id_, minute)

    def on_second_change(self, second):
        self.second_signal.emit(self.tomate.id_, second)

    def on_name_change(self, name):
        self.name_signal.emit(self.tomate.id_, name)

