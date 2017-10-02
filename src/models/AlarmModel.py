# coding: utf8
from .models import Alarm
from .BaseModel import BaseModel


class AlarmModel(BaseModel):
    table_class = Alarm

    def __init__(self, scope):
        super().__init__(scope)

    # def filter(self, session):
    #     return session.query(self.table_class).all()
