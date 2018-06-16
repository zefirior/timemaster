# -*- coding: utf-8 -*-

import logging
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


