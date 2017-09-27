# coding: utf-8
from .DBError import DBError
from sqlalchemy import create_engine


class Connector:
    def __init__(self, uri):
        self.engine = None
        if uri is None:
            raise DBError('connector error: not url')
        self._uri = uri

    def connect(self):
        self.engine = create_engine(self._uri)
