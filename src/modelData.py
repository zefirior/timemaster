# -*- coding: utf-8 -*-

import sqlite3
# import uuid

class TMaster(object):

    DBASE_NAME = 'db/masterModel.db'

    # con = sqlite3.connect(tm.DBASE_NAME)
    # cur = con.cursor()
    #
    # cur.execute('SELECT * FROM user')
    # data = cur.fetchone()
    # print(data)

    # @staticmethod
    def get_conection(func):
        def wrap(*args, **kwargs):
            con_db = sqlite3.connect(TMaster.DBASE_NAME)
            con_db.row_factory = sqlite3.Row
            _largs = list(args)
            _largs.insert(1, con_db)
            res = func(*_largs, **kwargs)
            print('конект подставлен успешно')
            return res
        return wrap
        # try:
        #     con = sqlite3.connect(self.DBASE_NAME)
        # return sqlite3.connect(self.DBASE_NAME)

    @get_conection  #  .__func__
    def get_alarms(self, con_db, session):
        cur = con_db.cursor()
        cur.execute('''SELECT * FROM alarm WHERE USER_ID = ?''', (session.user_id,))
        sqlist = cur.fetchall()
        header = sqlist[0].keys()  # вытаскиваем шапку по первой строке
        con_db.commit()
        cur.close()
        return {a['ALARM_ID']: {column: a[column] for column in header if column != 'ALARM_ID'} for a in sqlist}

    @get_conection
    def create_alarm(self, con_db, session, alname, aldesc, altime, ring_id):
        cur = con_db.cursor()
        cur.execute('''
                    INSERT INTO alarm (AL_NAME, AL_DESC, AL_TIME, USER_ID, RING_ID)
                        VALUES (:alname, :aldesc, :altime, :user_id, :ring_id)
                    ''',
                    {'alname': alname,
                        'aldesc': aldesc,
                        'altime': altime,
                        'user_id': session.user_id,
                        'ring_id': ring_id})
        con_db.commit()
        cur.close()

    @get_conection
    def update_alarm(self, con_db, session, alid, alname, aldesc, altime, ring_id):
        cur = con_db.cursor()
        cur.execute('''
                        UPDATE alarm
                            SET AL_NAME = :alname,
                                AL_DESC = :aldesc,
                                AL_TIME = :altime,
                                USER_ID = :user_id,
                                RING_ID = :ring_id
                            WHERE ALARM_ID = :alid
                        ''',
                    {'alname': alname,
                     'aldesc': aldesc,
                     'altime': altime,
                     'user_id': session.user_id,
                     'ring_id': ring_id,
                     'alid': alid})
        con_db.commit()
        cur.close()

    @get_conection
    def delete_alarm(self, con_db, alid):
        cur = con_db.cursor()
        cur.execute("DELETE AL FROM alarm AL WHERE ALARM_ID = ?", (alid,))
        con_db.commit()
        cur.close()

    @get_conection
    def create_user(self, con_db, bday, login, passwd, name, sname):
        cur = con_db.cursor()
        cur.execute("""INSERT INTO user (
                            USER_BIRTHDAY,
                            USER_LOGIN,
                            USER_PASSWD,
                            USER_NAME,
                            USER_SNAME
                        ) VALUES (
                            :bday,
                            :login,
                            :passwd,
                            :name,
                            :sname
                        )""",
                    {
                        'bday': bday,
                        'login': login,
                        'passwd': passwd,
                        'name': name,
                        'sname': sname
                    })
        con_db.commit()
        cur.close()

    @get_conection
    def get_user(self, con_db, login, passwd):
        con_db.row_factory = sqlite3.Row
        cur = con_db.cursor()
        cur.execute("SELECT * FROM user WHERE USER_LOGIN = ? AND USER_PASSWD = ?", (login, passwd))
        user_row = cur.fetchone()
        if not user_row:
            print('no user')
            return
        header = user_row.keys()  # вытаскиваем шапку по строке
        return user_row['USER_ID'], {column: user_row[column] for column in header if column != 'USER_ID'}


# session = uuid.uuid4()
class session(object):
    pass

tm = TMaster()

s = session()
s.user_id = 1
print(tm.get_alarms(s))

tm.create_user(u'1994-07-16', u'ksusarova', u'38153987', u'Ксения', u'Сусарова')
print(tm.get_user('ksusarova', '38153987'))
con = sqlite3.connect(tm.DBASE_NAME)
cur = con.cursor()
cur.execute('select * from USER')
a = cur.fetchall()
print(a)
