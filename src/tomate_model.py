from itertools import count
from core.base_model import BaseModel


class TomateModel(BaseModel):
    counter = count()

    def __init__(self, id_, recipe, delay, name, tomate_order):
        self._self_id = next(self.counter)
        self._droped_flag = False
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

    @property
    def drop_flag(self):
        return self._droped_flag

    @drop_flag.setter
    def drop_flag(self, flag):
        if not isinstance(flag, bool):
            raise Exception('Неверный тип флага')
        self._droped_flag = flag

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

    def _update(self):
        self.conn.execute(
            """
            update tomate
            set delay = ?,
                name = ?,
                tomate_order = ?
            where id = ?
            """,
            [
                self.delay,
                self.name,
                self.tomate_order,
                self.id_,
            ]
        )

    def _insert(self):
        self.conn.execute(
            """
            insert into tomate (
                recipe_id,
                delay,
                name,
                tomate_order
            ) VALUES (?, ?, ?, ?)
            """,
            [
                self.recipe.id_,
                self.delay,
                self.name,
                self.tomate_order,
            ]
        )
        self.id_ = self.conn.execute('SELECT last_insert_rowid()').fetchone()[0]

    def _delete(self):
        if self.id_ is None:
            return

        self.conn.execute(
            """
            delete from tomate where id = ?
            """,
            [
                self.id_,
            ]
        )

    def update(self):
        if self.id_ is None and not self.drop_flag:
            self._insert()
        elif self.id_ is not None and self.drop_flag:
            self._delete()
        else:
            self._update()
