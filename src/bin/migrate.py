# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import DB_URL
from core.connector import Connector

connector = Connector(DB_URL)
conn = connector.connect()
# cur = conn.cursor()

# con = sqlite3.connect(DBASE_NAME)

# with con:

conn.execute('DROP TABLE IF EXISTS tomate')
conn.execute('DROP TABLE IF EXISTS recipe')

conn.execute('''CREATE TABLE recipe (
    ID integer PRIMARY KEY AUTOINCREMENT,
    NAME text,
    CONTROL_FLAG integer
)''')

conn.execute('''CREATE TABLE tomate (
    ID integer PRIMARY KEY AUTOINCREMENT,
    RECIPE_ID integer,
    DELAY integer,
    NAME text,
    TOMATE_ORDER integer,
    FOREIGN KEY (RECIPE_ID) REFERENCES recipe(ID)
)''')

conn.execute('''
    INSERT INTO recipe (NAME, CONTROL_FLAG) VALUES
        ('первый рецепт', 0)
        ,('мой будильник', 1)
    ''')

conn.execute('''
    INSERT INTO tomate (RECIPE_ID, DELAY, NAME, TOMATE_ORDER) VALUES
         (1, 3, 'tomate 1', '1')
        ,(1, 4, 'tomate 2', '2')
        ,(2, 2, 'my tomate 1', '1')
        ,(2, 4, 'my tomate 2', '2')
    ''')

conn.close()

