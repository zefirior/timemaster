# -*- coding:utf-8 -*-

import os
# from inspect import getmembers
# from .recorder import Recorder

# пока не подключу конфиг
PACKAGE_DIR = os.getcwd()
SRC_DIR = PACKAGE_DIR + '/src'

class RouterBinder(object):
    def __init__(self, parent_name, obj_name, iamparent):
        self._parent_name = parent_name
        self._obj_name = obj_name

    def __getattr__(self, item):
        pass


class Router(object):
    _instance = None
    _isExists = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        # рабочий отсек. отрабатывает каждый раз

        if not self._isExists:  # инициализирующий отсек. отрабатывает первый раз
            self.initialized()
            # self._caseView = []
            # self._caseModel = []
            # self._caseController = []
            self._bindDict = {}
            self.controllers = {}
            # self.recorder = Recorder()
            # self.recorder.fill()
            # self.load_controller()

    @classmethod
    def initialized(cls):
        cls._isExists = True

    def find_in_case(self, obj_name, case):
        for obj in case:
            if obj_name == obj.define:
                return obj
        raise Exception('Not obj {} in case {}'.format(obj_name, case))

    def load_controller(self, name_controller=None):
        objs = []
        if name_controller:
            objs.append(self.find_in_case(name_controller, self._caseController)())
        elif name_controller is None:
            objs = [control() for control in self._caseController]
        for obj in objs:
            if obj.define not in self.controllers:
                self.controllers[obj.define] = obj
                self._bindDict[obj.define] = {}
            else:
                del self.controllers[obj.define]
                self.controllers[obj.define] = obj
                self._bindDict[obj.define] = {}

    def bind_model(self, controller, model_name):
        model = self.find_in_case(model_name, self._caseModel)
        self._bindDict[controller.define]['model'] = model(controller)

    def get_model(self, controller, model_name):
        cname = controller.define
        if (cname in self._bindDict
                and 'model' in self._bindDict[cname]
                and self._bindDict[cname]['model'].define == model_name):
            return self._bindDict[cname]['model']
        else:
            return

    def call_methods(self, cont_def, method, *arg, **kw):
        for control in self.controllers:
            if cont_def == control and hasattr(self.controllers[control], method):
                return getattr(self.controllers[control], method)(*arg, **kw)

    # def get_methods(self):
    #     methods = {}
    #     for control in self.controllers:
    #         methods[control] = getmembers(self.controllers[control])
    #     return methods