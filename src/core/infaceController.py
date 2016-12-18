from .inface import Inface


class InfController(Inface):
    define = 'InfController'

    def __init__(self, router):
        super().__init__(router)
        self.mname = 'InfModel'
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
