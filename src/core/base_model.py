# coding: utf8
from config import DB_URL
from .connector import Connector


class BaseModel(object):
    _connector = Connector(DB_URL)
    conn = _connector.connect()
    session = _connector.session()
