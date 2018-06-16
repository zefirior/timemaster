import os
from config import BASE_DIR


class Iconer:
    def __init__(self):
        self.root = BASE_DIR
        self._icon_path = {
            'up': "content/icon-up.png",
            'down': "content/icon-down.png",
            'add': "content/plus.png",
            'remove': "content/delete.png",
        }

    def __getattr__(self, item):
        path_from_root = self._icon_path[item]
        return os.path.join(self.root, path_from_root)
icons = Iconer()
