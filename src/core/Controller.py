from .router import Router
from .fossil import ParentFossil


class Controller(object):
    define = 'Controller'
    _type = 'Controller'

    def __init__(self):
        self._router = Router()
        self.mname = 'Model'
        self.model = None
        self.path = None

    def load_model(self):
        self.model = self._router.get_model(self, self.mname)
        if self.model is None:
            self._router.bind_model(self, self.mname)
            self.model = self._router.get_model(self, self.mname)

    def method(self):
        print('hi')

    def preview_model(self):
        self.load_model()
        mess = 'My model say \'{}\''
        model_mess = self.model.preview()
        return mess.format(model_mess)
