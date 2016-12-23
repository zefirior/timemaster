class Fossil(object):
    define = 'default'

    def __init__(self, router, parent):
        self._router = router
        self._parent = parent


class ParentFossil(object):
    define = 'default'

    def __init__(self, router):
        self._router = router
