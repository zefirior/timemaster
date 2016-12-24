from .Model import Model
from .Controller import Controller
from .router import Router


class Recorder(object):
    def __init__(self):
        self.router = Router()

    def fill(self):
        elements = [Model, Controller]
        for element in elements:
            case_name = '_case{}'.format(element._type)
            if hasattr(self.router, case_name):
                getattr(self.router, case_name).append(element)
            else:
                setattr(self.router, case_name, [element, ])
        self.router.load_controller()

        # self.router._caseController.append(Controller)
        # self.router._caseModel.append(Model)
