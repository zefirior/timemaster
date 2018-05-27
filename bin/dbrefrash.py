#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from config import config

cur = config.scoper('general').connection

cur.execute('DROP TABLE IF EXISTS inrval')
cur.execute('DROP TABLE IF EXISTS inrval_type')
cur.execute('DROP TABLE IF EXISTS inrval_grp')
cur.execute('DROP TABLE IF EXISTS inrval_grp_type')
cur.execute('DROP TABLE IF EXISTS alarm')
cur.execute('DROP TABLE IF EXISTS alarm_type')
cur.execute('DROP TABLE IF EXISTS menu')

cur.execute('''CREATE TABLE menu (
    MENU_ID integer PRIMARY KEY AUTOINCREMENT,
    MENU_PARENT_ID integer,
    MENU_PATH text,
    MENU_ABBR text,
    MENU_ORDER text
)''')

cur.execute('''CREATE TABLE alarm_type (
    ID integer PRIMARY KEY AUTOINCREMENT,
    ALARM_TYPE_CODE text,
    ALARM_TYPE_NAME text,
    ALARM_TYPE_DESC text
)''')

cur.execute('''CREATE TABLE alarm (
    ID integer PRIMARY KEY AUTOINCREMENT,
    ALARM_TYPE_ID integer,
    ALARM_NAME text,
    ALARM_DESC text,
    ALARM_TIME text,
    FOREIGN KEY (ALARM_TYPE_ID) REFERENCES alarm_type(ID)
)''')

cur.execute('''CREATE TABLE inrval_grp_type (
    ID integer PRIMARY KEY AUTOINCREMENT,
    INRVAL_GRP_TYPE_CODE text,
    INRVAL_GRP_TYPE_NAME text,
    INRVAL_GRP_TYPE_DESC text
)''')

cur.execute('''CREATE TABLE inrval_grp (
    ID integer PRIMARY KEY AUTOINCREMENT,
    INRVAL_GRP_TYPE_ID integer,
    INRVAL_GRP_ID integer,
    INRVAL_GRP_ORDER integer,
    INRVAL_GRP_NAME text,
    INRVAL_GRP_DESC text,
    FOREIGN KEY (INRVAL_GRP_TYPE_ID) REFERENCES inrval_grp_type(ID),
    FOREIGN KEY (INRVAL_GRP_ID) REFERENCES inrval_grp(ID)
)''')

cur.execute('''CREATE TABLE inrval_type (
    ID integer PRIMARY KEY AUTOINCREMENT,
    INRVAL_TYPE_CODE text,
    INRVAL_TYPE_NAME text,
    INRVAL_TYPE_DESC text
)''')

cur.execute('''CREATE TABLE inrval (
    ID integer PRIMARY KEY AUTOINCREMENT,
    INRVAL_TYPE_ID integer,
    INRVAL_GRP_ID integer,
    INRVAL_GRP_NAME text,
    INRVAL_GRP_DESC text,
    INRVAL_ORDER integer,
    INRVAL_TIME text,
    FOREIGN KEY (INRVAL_GRP_ID) REFERENCES inrval_grp(ID),
    FOREIGN KEY (INRVAL_TYPE_ID) REFERENCES inrval_type(ID)
)''')

cur.execute('''
    INSERT INTO alarm_type (ID, ALARM_TYPE_CODE, ALARM_TYPE_NAME, ALARM_TYPE_DESC)
        VALUES (1, 'test', 'for test', null)
    ''')

cur.execute('''
    INSERT INTO alarm (ALARM_TYPE_ID, ALARM_NAME, ALARM_DESC, ALARM_TIME) VALUES
         (1, 'my alarm', NULL, '2017-01-01 00:00:01')
        ,(1, 'my alarm2', NULL, '2017-01-01 00:00:01')
    ''')

cur.execute('''
    INSERT INTO inrval_grp_type (INRVAL_GRP_TYPE_CODE, INRVAL_GRP_TYPE_NAME, INRVAL_GRP_TYPE_DESC) VALUES
         ('inrval_grp_type', 'inrval_grp_type', 'inrval_grp_type')
    ''')

cur.execute('''
    INSERT INTO inrval_grp (INRVAL_GRP_TYPE_ID, INRVAL_GRP_ID, INRVAL_GRP_ORDER, INRVAL_GRP_NAME, INRVAL_GRP_DESC) VALUES
          (1, null, null, 'inrval_grp', 'inrval_grp')
         ,(1, 1, 2, 'inrval_grp', 'inrval_grp')
    ''')

cur.execute('''
    INSERT INTO inrval_type (INRVAL_TYPE_CODE, INRVAL_TYPE_NAME, INRVAL_TYPE_DESC) VALUES
         ('inrval_type', 'inrval_type', 'inrval_type')
    ''')

cur.execute('''
    INSERT INTO inrval (INRVAL_TYPE_ID, INRVAL_GRP_ID, INRVAL_GRP_NAME, INRVAL_GRP_DESC, INRVAL_ORDER, INRVAL_TIME) VALUES
         (1, 1, 'inrval', null, 1, '00:01:30')
    ''')

cur.close()
