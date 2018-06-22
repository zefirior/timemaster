from core.utils import int_2_time_attr, time_attr_2_int
from .base_widget import BaseWidget
from .recipe_edit_setuper import Ui_Form as recipe_edit_setuper
from .tomate_view import TomateEditView
from recipe_model import RecipeModel
from tomate_model import TomateModel


class RecipeEditorView(BaseWidget, recipe_edit_setuper):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.recipe = None
        self.tomates = []
        self.tomates_for_remove = []

    def setup_dialog(self):
        self.button_save.clicked.connect(self.save_recipe)
        self.recipe_name.textChanged.connect(self.on_recipe_change)

    def closeEvent(self, QCloseEvent):
        self.app.setDisabled(False)
        self.hide()

    def on_up(self, tomate_id):
        self.tomate_swap(tomate_id, up=True)

    def on_down(self, tomate_id):
        self.tomate_swap(tomate_id, up=False)

    def on_minute_change(self, tomate_id, minute):
        _, tomate = self.find_tomat_by_id(tomate_id)

        _, second = int_2_time_attr(tomate.delay)
        tomate.delay = time_attr_2_int(minute, second)

    def on_second_change(self, tomate_id, second):
        _, tomate = self.find_tomat_by_id(tomate_id)

        minute, _ = int_2_time_attr(tomate.delay)
        tomate.delay = time_attr_2_int(minute, second)

    def on_name_change(self, tomate_id, name):
        _, tomate = self.find_tomat_by_id(tomate_id)
        tomate.name = name

    def on_recipe_change(self, name):
        self.recipe.name = name
        self.recipe_name.setText(self.recipe.name)

    def render_recipe(self, recipe_name):
        self.clear_editor()
        self.tomates = []
        self.tomates_for_remove = []

        self.recipe = RecipeModel.recipe_by_name(recipe_name)
        self.recipe_name.setText(self.recipe.name)

        tomates = self.sort_tomates(self.recipe.tomates())

        for tomate in tomates:
            self.tomates.append(tomate)
            self.add_tomate(tomate)

    def render_new_recipe(self):
        self.clear_editor()
        self.tomates = []
        self.tomates_for_remove = []

        self.recipe = RecipeModel(None, '', True)
        self.recipe_name.setText(self.recipe.name)
        new_tomate = TomateModel(None, self.recipe, 0, '', 1)

        self.tomates.append(new_tomate)
        self.add_tomate(new_tomate)

    def rerender_recipe(self):
        self.clear_editor()
        self.tomates = self.sort_tomates(self.tomates)
        for tomate in self.tomates:
            self.add_tomate(tomate)

    @staticmethod
    def sort_tomates(tomates):
        return sorted(tomates, key=lambda t: t.tomate_order)

    def find_tomat_by_id(self, tomate_id):
        if tomate_id is None:
            return None, None

        index = None
        finded_tomate = None
        for i, tomate in enumerate(self.tomates):
            if tomate._self_id == tomate_id:
                index = i
                finded_tomate = tomate

        if index is None:
            raise Exception('в эдиторе нет томата с id_={}'.format(tomate_id))

        return index, finded_tomate

    def clear_editor(self):
        self.notify.setText('')
        layout = self.verticalLayout_2
        while layout.count() > 1:
            item = layout.takeAt(0)
            if not item:
                continue

            widg = item.widget()
            if widg:
                widg.deleteLater()

    def add_tomate(self, tomate):
        tomate_view = TomateEditView(self, tomate)
        tomate_view.tomat_name.setText(tomate.name)

        minute, second = int_2_time_attr(tomate.delay)

        tomate_view.spin_minute.setValue(minute)
        tomate_view.spin_second.setValue(second)

        position = self.verticalLayout_2.count() - 1
        self.verticalLayout_2.insertWidget(position, tomate_view)
        tomate_view.up_signal.connect(self.on_up)
        tomate_view.down_signal.connect(self.on_down)
        tomate_view.minute_signal.connect(self.on_minute_change)
        tomate_view.second_signal.connect(self.on_second_change)
        tomate_view.name_signal.connect(self.on_name_change)
        tomate_view.add_signal.connect(self.new_tomate)
        tomate_view.remove_signal.connect(self.remove_tomate)

    def new_tomate(self, before_tomate_id):
        self.tomates = self.sort_tomates(self.tomates)

        b_index, b_tomate = self.find_tomat_by_id(before_tomate_id)

        if b_index is None:
            index = 0
            new_order = 1
        else:
            index = b_index + 1
            new_order = b_tomate.tomate_order + 1

        new_tomate = TomateModel(None, self.recipe, 0, '', new_order)

        for i, exist_tomate in enumerate(self.tomates[index:]):
            exist_tomate.tomate_order = new_order + i + 1
        self.tomates.insert(index, new_tomate)
        self.rerender_recipe()

    def remove_tomate(self, tomate_id):
        if len(self.tomates) <= 1:
            self.notify.setText('Нельзя удалять последний томат')
            return

        index, tomate = self.find_tomat_by_id(tomate_id)
        tomate.drop_flag = True
        self.tomates_for_remove.append(tomate)
        self.tomates.remove(tomate)

        self.rerender_recipe()

    def save_recipe(self):
        check_msg = self.check_before_save()
        if check_msg:
            self.notify.setText(check_msg)
            return

        self.recipe.update()
        for tomate in self.tomates:
            tomate.update()
        for tomate in self.tomates_for_remove:
            tomate.update()
        self.hide()
        self.main.setDisabled(False)
        self.main.fill()

    def check_before_save(self):
        if self.recipe.name == '':
            return "Название рецепта не может быть пустым"

        recipe_from_db = RecipeModel.recipe_by_name(self.recipe.name)
        if (
            recipe_from_db is not None and
            recipe_from_db.name == self.recipe.name and
            self.recipe.id_ is not None and
            self.recipe.id_ != recipe_from_db.id_
        ):
            return "Такой рецепт уже есть"

        if len(self.tomates) == 0:
            return "Нужен хоть один томат"

        for tomate in self.tomates:
            # names = set()
            if tomate.name == '':
                return "Томат без названия"
            # if tomate.name in names:
            #     return ""

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


