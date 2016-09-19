import sqlite3

DBASE_NAME = 'db/masterModel.db'

con = sqlite3.connect(DBASE_NAME)
cur = con.cursor()

cur.execute('SELECT * FROM user')
data = cur.fetchone()
print(data)
