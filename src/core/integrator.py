# -*- coding: utf-8 -*-

import os
import sys
from operator import attrgetter
from config.config import BASE_DIR


class Integrator(object):

    def __init__(self, control_path):
        self.control_path = control_path

    def load_model(self, scope):
        if not hasattr(sys.modules, 'models'):
            import models
        breadcrumbs = self.control_path.split('/')
        obj = models
        for crumb in breadcrumbs[:-1]:
            obj = getattr(obj, crumb.lower(), None)
        #  add postfix
        mname = breadcrumbs[-1].capitalize() + 'Model'
        obj = getattr(obj, mname, None)(scope)
        return obj

    def load_view(self, vname, parent=None):
        if not hasattr(sys.modules, 'view'):
            import view

        breadcrumbs = self.control_path.split('/')
        obj = view
        print(obj)
        for crumb in breadcrumbs:
            obj = getattr(obj, crumb.lower(), None)
            print (obj, crumb.lower())
        #  add postfix
        vname = vname.capitalize() + 'View'
        print(obj, vname)
        obj = getattr(obj, vname, None)(parent=parent)
        return obj

