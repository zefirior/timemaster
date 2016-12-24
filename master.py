import config
from src.core import Recorder
from src import core
import inspect


app = Recorder()
app.fill()
print(app.router._bindDict)
# print(rout._caseController)
# print(rout.controllers)
print(app.router.call_methods('Controller', 'preview_model'))
