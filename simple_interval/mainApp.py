#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import warnings
from ui.interval_view import Ui_MainWindow
from config import MINUTE
from widgets import ContinueDialog, FinishDialog, RecipeEditorView, TomateView
from delay_thread import DelayThread
from PyQt5.QtWidgets import QApplication, QMainWindow
from recipe_model import RecipeModel
from tomate_model import TomateModel


class Scheduler:
    def __init__(self):
        self.cur_recipe = None
        self.cur_tomate = None

    @staticmethod
    def all_recipe():
        return RecipeModel.recipe_all()

    def select_recipe(self, name):
        recipe = RecipeModel.recipe_by_name(name)
        self.cur_recipe = recipe
        logging.info(self.cur_recipe)

    def select_tomate(self, tomate):
        self.cur_tomate = tomate

    def get_next_tomate(self):
        if self.cur_recipe is None:
            raise Exception
        if self.cur_tomate is None:
            cur_tomate_order = 0
        else:
            cur_tomate_order = self.cur_tomate.tomate_order
        tomates = TomateModel.tomate_by_recipe(self.cur_recipe)
        tomates = [tomate for tomate in tomates if tomate.tomate_order > cur_tomate_order]
        tomates.sort(key=lambda tomate: tomate.tomate_order)
        if len(tomates) > 0:
            return tomates[0]
        else:
            return


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

        # connections block
        self.begin_button.clicked.connect(self.scheduler_begin)
        self.pause_button.clicked.connect(self.on_pause)
        self.reset_button.clicked.connect(self.on_reset)
        self.recipe_list_box.currentIndexChanged.connect(self.on_recipe_chenge)
        self.change_recipe_button.clicked.connect(self.on_edit)
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
        next_tomate = self.scheduler.get_next_tomate()
        logging.info('run task "{}"'.format(tomate.name))

        self.continue_dialog.display_alarm_name(tomate.name)

        self.cur_tomate_text.setText(tomate.name)
        self.next_tomate_text.setText('')

        if next_tomate:
            self.next_tomate_text.setText(next_tomate.name)

        self.delay_thread = DelayThread(tomate.delay)
        self.delay_thread.alarm_timeout.connect(self.on_timeout)
        self.delay_thread.alarm_tic.connect(self.on_tik)
        self.delay_thread.start()

    def on_timeout(self):
        if self.scheduler.get_next_tomate():
            self.continue_dialog.show()
        else:
            self.finish_dialog.show()

    def on_pause(self):
        if self.work_state:
            new_state = not self.delay_thread.pause
            self.delay_thread.pause = new_state

    def on_tik(self, number):
        minute_num = number // MINUTE
        second_num = number - minute_num * MINUTE
        self.lcd_minute.display(minute_num)
        self.lcd_second.display(second_num)

    def on_recipe_chenge(self, *arg):
        recipe_name = self.recipe_list_box.currentText()
        if recipe_name == '':
            return

        self.recipe_editor.render_recipe(recipe_name)

        self.scheduler.select_recipe(recipe_name)
        self.scheduler.select_tomate(None)
        next_tomate = self.scheduler.get_next_tomate()
        self.next_tomate_text.setText(next_tomate.name)

    def on_edit(self):
        self.recipe_editor.show()
        self.setDisabled(True)

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
        self.cur_tomate_text.setText('')
        self.next_tomate_text.setText('')
        self.recipe_list_box.setDisabled(False)
        self.on_recipe_chenge()

    def on_reset(self):
        self.delay_thread.terminate()
        self.schedule_stop()


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    app = QApplication(sys.argv)

    window = TimeLauncher()
    window.show()

    sys.exit(app.exec_())
