import os
from config import BASE_DIR


class ContentPath:
    def __init__(self):
        self.content_dir = os.path.join(BASE_DIR, 'content')
        self._icon_path = {
            'up':     ["icon-up.png"],
            'down':   ["icon-down.png"],
            'add':    ["plus.png"],
            'remove': ["delete.png"],
            'ring':   ["hozier-take-me-to-church.wav"],
        }

    def __getattr__(self, item):
        path_from_root = self._icon_path[item]
        return os.path.join(self.content_dir, *path_from_root)

cont_path = ContentPath()
