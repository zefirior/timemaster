from .inface import Inface


class InfModel(Inface):
    define = 'InfModel'

    def __init__(self, router):
        super().__init__(router)

    def preview(self):
        print(self.define)
        return 'I\'m main model'
