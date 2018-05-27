# coding: utf8
from .models import Alarm
from .BaseModel import BaseModel


class PeriodalarmModel(BaseModel):
    table_class = Alarm

    # def filter(self, session):
    #     return session.query(self.table_class).all()

    def all(self):
        res = self.conn.execute('select * from inrval_grp').fetchall()
        return res
