from core.integrator import Integrator


class Test2Controller(object):
    cname = 'test2'

    def __init__(self):
        # TODO: refactor
        assert self.cname is not None

        self.model = None
        self._integrator = Integrator(self.cname)

    def load_model(self):

        self.model = self._integrator.load_model('general')
        return True if self.model else False

    def load_view(self, vname, parent=None):

        view = self._integrator.load_view(vname, parent=parent)
        return view

    def render(self, parent=None):
        self.load_model()
        data = self.model.all()
        view = self.load_view('main', parent=parent)
        view.bind(data=data)
        view.renderView()
        return view



