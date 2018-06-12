from core.base_model import BaseModel


class RecipeModel(BaseModel):

    def __init__(self, id_, name, control_flag):
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
        id_, name, control_flag = cls.conn.execute(
            'select id, name, control_flag from recipe where name = ?',
            [name]
        ).fetchone()
        return cls(id_, name, control_flag)

