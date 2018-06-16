# coding: utf8


class BaseModel(object):
    table_class = None
    conf = None
    conn = None
    session = None

    def __init__(self):
        pass

    def all(self):
        res = self.conn.execute('select * from alarm').fetchall()
        return res
        # return self._session.query(self.table_class).all()
