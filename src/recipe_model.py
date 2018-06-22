from itertools import count
from core.base_model import BaseModel
from tomate_model import TomateModel


class RecipeModel(BaseModel):
    counter = count()

    def __init__(self, id_, name, control_flag):
        self._self_id = next(self.counter)
        self.id_ = id_
        self.name = name
        self.control_flag = control_flag

    def __str__(self):
        return (
            "<{cls}: "
            "id_='{id_}', "
            "name='{name}', "
            "control_flag='{control_flag}', "
            ">"
        ).format(
            cls=self.__class__.__name__,
            id_=self.id_,
            name=self.name,
            control_flag=self.control_flag,
        )

    def __repr__(self):
        return repr(self.__str__())

    @classmethod
    def recipe_all(cls):
        data = cls.conn.execute('select id, name, control_flag from recipe').fetchall()
        return [cls(id_, name, control_flag) for id_, name, control_flag in data]

    @classmethod
    def recipe_by_id(cls, id_):
        id_, name, control_flag = cls.conn.execute(
            'select id, name, control_flag from recipe where id = ?',
            [id_]
        ).fetchone()
        return cls(id_, name, control_flag)

    @classmethod
    def recipe_by_name(cls, name):
        if name is None:
            return
        res = cls.conn.execute(
            'select id, name, control_flag from recipe where name = ?',
            [name]
        ).fetchone()
        if res is None:
            return
        return cls(*res)

    def tomates(self):
        return TomateModel.tomate_by_recipe(self)

    def _update(self):
        self.conn.execute(
            """
            update recipe
            set control_flag = ?,
                name = ?
            where id = ?
            """,
            [
                self.control_flag,
                self.name,
                self.id_,
            ]
        )

    def _insert(self):
        self.conn.execute(
            """
            insert into recipe (
                control_flag,
                name
            ) VALUES (?, ?)
            """,
            [
                self.control_flag,
                self.name,
            ]
        )
        self.id_ = self.conn.execute('SELECT last_insert_rowid()').fetchone()[0]

    def _delete(self):
        self.conn.execute(
            """
            delete from recipe where id = ?
            """,
            [
                self.id_,
            ]
        )

    def update(self):
        if self.id_ is None:
            self._insert()
        else:
            self._update()

    def delete(self):
        tomates = TomateModel.tomate_by_recipe(self)
        for tomate in tomates:
            tomate.drop_flag = True
            tomate.update()
        self._delete()