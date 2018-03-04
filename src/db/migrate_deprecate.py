# -*- coding: utf-8 -*-
from config.config import scoper

cur = scoper('general').connection

# con = sqlite3.connect(DBASE_NAME)

# with con:

cur.execute('DROP TABLE IF EXISTS alarm')
cur.execute('DROP TABLE IF EXISTS one_alarm')
cur.execute('DROP TABLE IF EXISTS ring')
cur.execute('DROP TABLE IF EXISTS user')

cur.execute('''CREATE TABLE menu (
    MENU_ID integer PRIMARY KEY AUTOINCREMENT,
    MENU_PARENT_ID integer,
    MENU_PATH text,
    MENU_ABBR text,
    MENU_ORDER text
)''')

cur.execute('''CREATE TABLE user (
    USER_ID integer PRIMARY KEY AUTOINCREMENT,
    USER_BIRTHDAY text,
    USER_LOGIN text,
    USER_PASSWD text,
    USER_NAME text,
    USER_SNAME text
)''')

cur.execute('''CREATE TABLE ring (
    RING_ID integer PRIMARY KEY AUTOINCREMENT,
    SOME_OPTION text,
    RING_PATH text
)''')

cur.execute('''CREATE TABLE one_alarm (
    ID integer PRIMARY KEY AUTOINCREMENT,
    ONE_ALARM_NAME text,
    ONE_ALARM_DESC text,
    ONE_ALARM_TIME text,
    USER_ID integer,
    RING_ID integer,
    FOREIGN KEY (RING_ID) REFERENCES ring(RING_ID),
    FOREIGN KEY (USER_ID) REFERENCES user(USER_ID)
)''')

cur.execute('''CREATE TABLE alarm (
    ID integer PRIMARY KEY AUTOINCREMENT,
    ALARM_NAME text,
    ALARM_DESC text,
    ALARM_SECOND INT,
    ALARM_MINUTE INT,
    ALARM_HOUR INT,
    ALARM_DAY INT,
    USER_ID integer,
    RING_ID integer,
    FOREIGN KEY (RING_ID) REFERENCES ring(RING_ID),
    FOREIGN KEY (USER_ID) REFERENCES user(USER_ID)
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

cur.execute('''INSERT INTO ring (
    SOME_OPTION,
    RING_PATH
    ) VALUES (
        'qwerty',
        'qwe/rty'
)''')

cur.execute('''
    INSERT INTO one_alarm (ONE_ALARM_NAME, ONE_ALARM_DESC, ONE_ALARM_TIME, USER_ID, RING_ID)
        VALUES ('first alarm', 'my alarm', '2017-09-24 01:23:23', 1, 1)
    ''')

cur.execute('''
    INSERT INTO alarm (ALARM_NAME, ALARM_DESC, ALARM_SECOND, ALARM_MINUTE, ALARM_HOUR, ALARM_DAY, USER_ID, RING_ID)
        VALUES ('first alarm', 'my alarm', 10, NULL, NULL, NULL, 1, 1)
    ''')

cur.close()
