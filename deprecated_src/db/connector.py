# coding: utf-8
from .DBError import DBError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connector:
    def __init__(self, uri, engine_isolation_level='READ UNCOMMITTED'):
        if uri is None:
            raise DBError('connector error: not url')
        self._uri = uri
        self._engine = create_engine(self._uri, isolation_level=engine_isolation_level, echo=True)
        self._smaker = sessionmaker(bind=self._engine, autocommit=True)
        self._conn = None
        self._session = None

    def connect(self):
        self._conn = self._engine.connect()
        return self._conn

    def session(self):
        self._session = self._smaker()
        return self._session
