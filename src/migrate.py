# -*- coding: utf-8 -*-
from config import DB_URL
from core.connector import Connector


class DataMigrate:

    def __init__(self):
        self.connector = Connector(DB_URL)
        self.conn = self.connector.connect()

    def migrate(self):

        self.conn.execute('''CREATE TABLE IF NOT EXISTS recipe (
            ID integer PRIMARY KEY AUTOINCREMENT,
            NAME text,
            CONTROL_FLAG integer
        )''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS tomate (
            ID integer PRIMARY KEY AUTOINCREMENT,
            RECIPE_ID integer,
            DELAY integer,
            NAME text,
            TOMATE_ORDER integer,
            FOREIGN KEY (RECIPE_ID) REFERENCES recipe(ID)
        )''')

        self.conn.close()

