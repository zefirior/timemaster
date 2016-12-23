from .fossil import Fossil


class Model(Fossil):
    define = 'Model'

    def __init__(self, router, parent):
        super().__init__(router, parent)

    def preview(self):
        print(self.define)
        return 'I\'m main model'
