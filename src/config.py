# -*- coding: utf-8 -*-

import os
import configparser


BASE_DIR = os.path.dirname(__file__)
CONF_FILE = os.environ.get('TM_CONF_FILE', os.path.join(BASE_DIR, '../config.ini'))

conf = configparser.ConfigParser()
conf.read(CONF_FILE)
