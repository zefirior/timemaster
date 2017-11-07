from widgets import MenuBuilder


def test_get_data():
    mb = MenuBuilder('general')
    data = mb.get_menu_date()
    assert data

