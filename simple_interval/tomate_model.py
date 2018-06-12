from core.base_model import BaseModel


class TomateModel(BaseModel):

    def __init__(self, id_, recipe, delay, name, tomate_order):
        self.id_ = id_
        self.recipe = recipe
        self.delay = delay
        self.name = name
        self.tomate_order = tomate_order

    def __str__(self):
        return (
            "<{cls}: "
            "id_='{id_}', "
            "recipe='{recipe}', "
            "delay='{delay}', "
            "name='{name}', "
            "tomate_order='{tomate_order}', "
            ">"
        ).format(
            cls=self.__class__.__name__,
            id_=self.id_,
            recipe=self.recipe.id_,
            delay=self.delay,
            name=self.name,
            tomate_order=self.tomate_order,
        )

    def __repr__(self):
        return repr(self.__str__())

    @classmethod
    def tomate_by_recipe(cls, recipe):
        data = cls.conn.execute(
            'select id, delay, name, tomate_order from tomate where recipe_id = ?',
            [recipe.id_]
        ).fetchall()
        return [
            cls(id_, recipe, delay, name, tomate_order)
                for
            id_, delay, name, tomate_order
                in
            data
        ]
