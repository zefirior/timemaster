from core import DBContext


def test_any():
    cxt = DBContext()

    model = cxt.AlarmModel

    obj = model.get_obj_by_id(1)
    desc = obj.alarm_desc
    obj.alarm_desc = 'description for alarm'
    obj.save()
    obj = model.get_obj_by_id(1)
    assert obj.alarm_desc == 'description for alarm'
    obj.alarm_desc = desc
    obj.save()


def test_cxt_attr():
    cxt = DBContext()

    print(cxt.conf)
    print(cxt._scope)

