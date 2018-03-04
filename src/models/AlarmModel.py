from .BaseModel import BaseModel


class AlarmModel(BaseModel):

    def __init__(self, id, type_id, name, desc, time):
        super().__init__()
        self._id = id
        self.alarm_type_id = type_id
        self.alarm_name = name
        self.alarm_desc = desc
        self.alarm_time = time

    def __repr__(self):
        return 'id: {}. type: {}. name: {}. desc: {}. time: {}'.format(
            self._id,
            self.alarm_type_id,
            self.alarm_name,
            self.alarm_desc,
            self.alarm_time
        )

    @classmethod
    def get_obj_by_id(cls, alarm_id):
        res = cls.conn.execute('select * from alarm where id = ?', [alarm_id]).fetchone()
        if res:
            return cls(*res)

    @classmethod
    def get_obj_by_name(cls, name):
        res = cls.conn.execute('select * from alarm where alarm_name = ?', [name]).fetchone()
        if res:
            return cls(*res)

    def save(self):
        stmt = '''
            update alarm
                set alarm_type_id = ?,
                    alarm_name = ?,
                    alarm_desc = ?,
                    alarm_time = ?
                where id = ?
            '''
        self.conn.execute(stmt, [
            self.alarm_type_id,
            self.alarm_name,
            self.alarm_desc,
            self.alarm_time,
            self._id,
        ])
