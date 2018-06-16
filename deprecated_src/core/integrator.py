# -*- coding: utf-8 -*-

import os
import sys
from core.DBContext import DBContext
from operator import attrgetter
from config.config import BASE_DIR


class Integrator(object):

    def __init__(self, control_path):
        self.control_path = control_path

    def load_model(self, scope):
        ctx = DBContext(scope)
        obj = getattr(ctx, self.control_path + 'Model')()
        return obj

    def load_view(self, vname, parent=None):
        if not hasattr(sys.modules, 'view'):
            import view

        breadcrumbs = self.control_path.split('/')
        obj = view
        # print(obj)
        for crumb in breadcrumbs:
            obj = getattr(obj, crumb.lower(), None)
            # print (obj, crumb.lower())
        #  add postfix
        vname = vname.capitalize() + 'View'
        # print(obj, vname)
        obj = getattr(obj, vname, None)(parent=parent)
        return obj

