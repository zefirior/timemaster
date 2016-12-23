from .Model import Model
from .Controller import Controller

class Recorder(object):
    def __init__(self, router):
        self.router = router

    def fill(self):
        self.router._caseController.append(Controller)
        self.router._caseModel.append(Model)