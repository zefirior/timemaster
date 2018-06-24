import os
import sys

MINUTE = 60
TIC_PER_SECOND = 5

BASE_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
SQLITE_PATH = os.path.join(BASE_DIR, 'db', 'masterModel.db')
DB_URL = 'sqlite:///{}'.format(SQLITE_PATH)
