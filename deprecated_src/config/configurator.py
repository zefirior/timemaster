# coding: utf8
from db.connector import Connector


class Configurator(object):
    def __init__(self, conf_data):
        self._conf_data = conf_data
        self.configure()

    def configure(self):
        self.connector = Connector(self._conf_data['db_url'])
        self.connection = self.connector.connect()
        self.session = self.connector.session()
