import os

MINUTE = 60
TIC_PER_SECOND = 5

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLITE_PATH = os.path.join(BASE_DIR, 'db/masterModel.db')
DB_URL = 'sqlite:///{}'.format(SQLITE_PATH)
