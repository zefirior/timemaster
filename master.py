import config
from src.core import Router
from src import core


rout = Router()
print(rout._bindDict)
# print(rout._caseController)
# print(rout.controllers)
print(rout.call_methods('InfController', 'preview_model'))