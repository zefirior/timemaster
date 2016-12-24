from .router import Router
from .fossil import Fossil


class Model(object):
    define = 'Model'
    _type = 'Model'

    def __init__(self, parent):
        self._router = Router()
        self._parent = parent

    def preview(self):
        print(self.define)
        return 'I\'m main model'
