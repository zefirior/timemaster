# -*- coding: utf-8 -*-
import os
from .scoper import Scoper
from .configurator import Configurator


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CONF_FILE = os.environ.get('TM_CONF_FILE', os.path.join(BASE_DIR, '../config.ini'))
SQLITE_PATH = os.path.join(BASE_DIR, 'db/masterModel.db')
SQLITE_PATH_TEST = os.path.join(BASE_DIR, 'db/testModel.db')

SCOPES = {
    '__scope_set_defaults': {  # настройки по умолчанию. scoper с таким названием не создается
        'class': Configurator,
        'db_url': 'sqlite:///{}'.format(SQLITE_PATH)
    },
    'general': {},
    'test': {
        'db_url': 'sqlite:///{}'.format(SQLITE_PATH_TEST)
    }
}

scoper = Scoper.get_instance(SCOPES)
