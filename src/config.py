# -*- coding: utf-8 -*-

import os
import configparser


BASE_DIR = os.path.dirname(__file__)
CONF_FILE = os.environ.get('TM_CONF_FILE', os.path.join(BASE_DIR, '../config.ini'))
SQLITE_PATH = os.path.join(BASE_DIR, 'db/data.db')

SCOPES = {
    '__scope_set_defaults': {  # настройки по умолчанию. scoper с таким названием не создается
        'db_url': 'sqlite:///'.format(SQLITE_PATH)
    },
    'general': {
        'db_url': 'sqlite:///'.format(SQLITE_PATH)
    }
}

if __name__ == '__main__':
    pass