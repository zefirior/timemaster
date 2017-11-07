# coding: utf8


class Scoper(object):
    _instance = None

    def __init__(self, scopes):
        default_set = scopes.pop('__scope_set_defaults')
        self.scopes_settings = {}
        self.scopes = list(scopes.keys())
        for scope, setting in scopes.items():
            combine_sett = dict(default_set)
            combine_sett.update(setting)
            conf_class = combine_sett['class']
            self.scopes_settings[scope] = conf_class(combine_sett)

    @classmethod
    def get_instance(cls, scopes):
        if cls._instance is None:
            cls._instance = Scoper(scopes)
        return cls._instance

    def __call__(self, scope_name):
        return self.scopes_settings[scope_name]

