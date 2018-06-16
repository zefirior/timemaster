# coding: utf8
from .BaseModel import BaseModel


class IntervalGrpModel(BaseModel):

    def all(self):
        res = self.conn.execute('select * from inrval_grp').fetchall()
        return res

