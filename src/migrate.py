import sqlite3

DBASE_NAME = 'db/masterModel.db'

con = sqlite3.connect(DBASE_NAME)

with con:
    cur = con.cursor()

    cur.execute('DROP TABLE IF EXISTS alint')
    cur.execute('DROP TABLE IF EXISTS chainint')
    cur.execute('DROP TABLE IF EXISTS alarm')
    cur.execute('DROP TABLE IF EXISTS ring')
    cur.execute('DROP TABLE IF EXISTS ufriend')
    cur.execute('DROP TABLE IF EXISTS friend')
    cur.execute('DROP TABLE IF EXISTS user')

    cur.execute('''CREATE TABLE user (
        USER_ID integer PRIMARY KEY AUTOINCREMENT,
        USER_BIRTHDAY text,
        USER_LOGIN text,
        USER_PASSWD text,
        USER_NAME text,
        USER_SNAME text
    )''')

    cur.execute('''CREATE TABLE friend (
        FRIEND_ID integer PRIMARY KEY AUTOINCREMENT,
        FRIEND_BIRTHDAY text,
        FRIEND_NAME text,
        FRIEND_SNAME text,
        FRIEND_PHONE text
    )''')

    cur.execute('''CREATE TABLE ufriend (
        UFREIEND_ID integer PRIMARY KEY AUTOINCREMENT,
        FRIEND_ID integer,
        USER_ID integer,
        FOREIGN KEY (FRIEND_ID) REFERENCES friend(FRIEND_ID),
        FOREIGN KEY (USER_ID) REFERENCES user(USER_ID)
    )''')

    cur.execute('''CREATE TABLE ring (
        RING_ID integer PRIMARY KEY AUTOINCREMENT,
        SOME_OPTION text,
        RING_PATH text
    )''')

    cur.execute('''CREATE TABLE alarm (
        ALARM_ID integer PRIMARY KEY AUTOINCREMENT,
        SOME_OPTION text,
        RING_ID integer,
        FOREIGN KEY (RING_ID) REFERENCES ring(RING_ID)
    )''')

    cur.execute('''CREATE TABLE chainint (
        CHAININT_ID integer PRIMARY KEY AUTOINCREMENT,
        SOME_OPTION text,
        DEF_RING_ID integer,
        FOREIGN KEY (DEF_RING_ID) REFERENCES ring(RING_ID)
    )''')

    cur.execute('''CREATE TABLE alint (
        ALINT_ID integer PRIMARY KEY AUTOINCREMENT,
        SOME_OPTION text,
        RING_ID integer,
        CHAININT_ID integer,
        FOREIGN KEY (CHAININT_ID) REFERENCES chainint(CHAININT_ID),
        FOREIGN KEY (RING_ID) REFERENCES ring(RING_ID)
    )''')

    cur.execute('''INSERT INTO user (
        USER_BIRTHDAY,
        USER_LOGIN,
        USER_PASSWD,
        USER_NAME,
        USER_SNAME
        ) VALUES (
            '1993-02-02',
            'zefirior',
            'loop',
            'Daniil',
            'Galiev'
    )''')

