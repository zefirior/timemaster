# coding: utf8
from aspirin.base import Connector


class Configurator(object):
    def __init__(self, conf_data):
        self._conf_data = conf_data
        self.configure()

    def configure(self):
        self.connector = Connector(self._conf_data['db_url'])
        self.connection = self.connector.connection()
        self.session = self.connector.session(bind=self.connection)


class Scoper(object):
    _instance = None

    def __init__(self, scopes):
        default_set = scopes.pop('__scope_set_defaults')
        self.scopes_settings = {}
        self.scopes = list(scopes.keys())
        for scope in self.scopes:
            combin_sett = dict(default_set)
            combin_sett.update(scopes[scope])
            self.scopes_settings[scope] = Configurator(combin_sett)

    @classmethod
    def get_instance(cls, scopes):
        if cls._instance is None:
            cls._instance = Scoper(scopes)
        return cls._instance

