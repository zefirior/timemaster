from .infaceModel import InfModel
from .infaceController import InfController

class Recorder(object):
    def __init__(self, router):
        self.router = router

    def fill(self):
        self.router._caseController.append(InfController)
        self.router._caseModel.append(InfModel)