#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
from migrate import DataMigrate
from PyQt5.QtWidgets import QApplication, QMainWindow
from widgets.main_setuper import Ui_MainWindow
from config import MINUTE
from widgets import ContinueDialog, FinishDialog, RecipeEditorView, TomateView
from delay_thread import DelayThread
from scheduler import Scheduler


class TimeLauncher(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.continue_dialog = ContinueDialog(self)
        self.finish_dialog = FinishDialog(self)
        self.recipe_editor = RecipeEditorView(self)

        self.recipe_editor.hide()

        self.delay_thread = None
        self.work_state = False
        self.scheduler = Scheduler()

        self.fill()

        self.pause_word = {
            False: 'Пауза',
            True: 'Продолжить',
        }

        # connections block
        self.begin_button.clicked.connect(self.scheduler_begin)
        self.pause_button.clicked.connect(self.on_pause)
        self.reset_button.clicked.connect(self.on_reset)
        self.recipe_list_box.currentIndexChanged.connect(self.on_recipe_chenge)
        self.change_recipe_button.clicked.connect(self.on_edit_recipe)
        self.add_recipe_button.clicked.connect(self.on_add_recipe)
        self.button_remove_recipe.clicked.connect(self.on_remove_recipe)
        # connections block

    def fill(self):
        self.recipe_list_box.clear()
        for recipe in self.scheduler.all_recipe():
            self.recipe_list_box.addItem(recipe.name)
        self.recipe_list_box.setCurrentIndex(0)
        self.on_recipe_chenge()

    def run_task(self):
        if self.scheduler.cur_tomate is None:
            raise Exception
        tomate = self.scheduler.cur_tomate

        self.continue_dialog.display_alarm_name(tomate.name)

        self.delay_thread = DelayThread(tomate.delay)
        self.delay_thread.alarm_timeout.connect(self.on_timeout)
        self.delay_thread.alarm_tic.connect(self.on_tik)
        self.delay_thread.start()

    def on_timeout(self):
        if self.scheduler.get_next_tomate():
            self.continue_dialog.show()
            self.setDisabled(True)
        else:
            self.finish_dialog.show()
            self.setDisabled(True)

    def on_pause(self):
        if self.work_state:
            new_state = not self.delay_thread.pause
            self.pause_button.setText(self.pause_word[new_state])
            self.delay_thread.pause = new_state

    def on_tik(self, number):
        minute_num = number // MINUTE
        second_num = number - minute_num * MINUTE
        self.lcd_minute.display(minute_num)
        self.lcd_second.display(second_num)

    def on_recipe_chenge(self, *arg):
        self.clear_tomate_list()
        recipe_name = self.recipe_list_box.currentText()
        if recipe_name == '':
            return

        self.recipe_editor.render_recipe(recipe_name)

        self.scheduler.select_recipe(recipe_name)
        self.scheduler.select_tomate(None)
        self.render_recipe()

    def on_edit_recipe(self):
        recipe_name = self.recipe_list_box.currentText()
        if recipe_name == '':
            return
        self.recipe_editor.show()
        self.setDisabled(True)

    def on_add_recipe(self):
        self.recipe_editor.render_new_recipe()
        self.recipe_editor.show()
        self.setDisabled(True)

    def on_remove_recipe(self):
        recipe = self.scheduler.cur_recipe
        if recipe is None:
            return
        recipe.delete()
        self.fill()

    def on_reset(self):
        self.delay_thread.terminate()
        self.schedule_stop()

    def scheduler_begin(self):
        if self.work_state:
            return
        self.work_state = True
        self.recipe_list_box.setDisabled(True)
        first_tomate = self.scheduler.get_next_tomate()
        self.scheduler.select_tomate(first_tomate)
        self.run_task()

    def schedule_continue(self):
        logging.info('main continue')
        self.continue_dialog.hide()
        self.finish_dialog.hide()
        next_tomate = self.scheduler.get_next_tomate()
        self.scheduler.select_tomate(next_tomate)
        self.run_task()

    def schedule_stop(self):
        logging.info('main stop')
        self.continue_dialog.hide()
        self.finish_dialog.hide()
        self.work_state = False
        self.lcd_second.display(0)
        self.lcd_minute.display(0)
        self.recipe_list_box.setDisabled(False)

        pause_state = self.delay_thread.pause
        self.pause_button.setText(self.pause_word[pause_state])

        self.on_recipe_chenge()

    def add_tomate(self, tomate):
        tomate_view = TomateView(self, tomate)

        position = self.verticalLayout_2.count() - 1
        self.verticalLayout_2.insertWidget(position, tomate_view)

    def clear_tomate_list(self):
        layout = self.verticalLayout_2
        while layout.count() > 1:
            item = layout.takeAt(0)
            if not item:
                continue

            widg = item.widget()
            if widg:
                widg.deleteLater()

    def render_recipe(self):
        self.clear_tomate_list()
        tomates = self.scheduler.all_tomate()
        for tomate in tomates:
            self.add_tomate(tomate)


if __name__ == '__main__':

    # logging.basicConfig(level=logging.INFO)

    migrator = DataMigrate()
    migrator.migrate()

    app = QApplication(sys.argv)

    window = TimeLauncher()
    window.show()

    sys.exit(app.exec_())
