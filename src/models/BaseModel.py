# coding: utf8
from config import scoper


class BaseModel(object):
    table_class = None

    def __init__(self, scope):
        self.conf = scoper(scope)
        self._connection = self.conf.connection
        self._session = self.conf.session

    def all(self):
        return self._session.query(self.table_class).all()
