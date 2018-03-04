# coding: utf8
from config.config import scoper
import models


# class _Modeller(object):
#     def __init__(self, conf):
#         self.conf = conf
#
#     def __getattr__(self, item):
#         cls = getattr(models, item)
#
#         class Model(cls):
#             conf = self.conf
#             conn = self.conf.connection
#             session = self.conf.session
#
#         return Model


class DBContext:

    def __init__(self, scope='general'):
        self._scope = scope
        self.conf = scoper(scope)

    def __getattr__(self, item):
        cls = getattr(models, item)

        class Model(cls):
            conf = self.conf
            conn = self.conf.connection
            session = self.conf.session

        return Model

    def __repr__(self):
        return 'DB context {}'.format(self._scope)
