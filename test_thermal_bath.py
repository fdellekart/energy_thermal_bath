from thermal_bath import LoadCurve
from pandas import DataFrame
import pytest
from datetime import datetime

load_curve = LoadCurve("load_curve_thermal_bath.csv", "W", "times")


def test_load_data():
    assert isinstance(load_curve.get_data(), DataFrame)
    assert load_curve._unit == "W"
    assert load_curve._time_key == "times"


def test_get_date_time():
    dt_string = "05-10-2020 17:34:12"
    dt = load_curve._get_date_time(dt_string)
    assert isinstance(dt, datetime)
    assert dt == datetime(2020, 10, 5, 17, 34, 12)


def test_time_to_index():
    index = load_curve.get_data().index
    is_datetime = [isinstance(el, datetime) for el in index]
    assert all(is_datetime)


def test_set_unit():
    with pytest.raises(Exception):
        load_curve.set_unit("wrong_unit")

    factor_dict = load_curve._factor_dict

    data = load_curve.get_data()

    for unit in factor_dict:
        load_curve.set_unit(unit)
        bool_frame = abs(data - load_curve.get_data()*factor_dict[unit]) < 0.1
        assert bool_frame.all(axis=None)


def test_moving_average():
    for key in load_curve.get_data().keys():
        load_curve.moving_average(key, 5)
        assert "SMA_{}".format(key) in load_curve.get_data().keys()

    load_curve.remove_average()

    for key in load_curve.get_data().keys():
        assert key[:3] != "SMA_"


def test_unit():
    assert load_curve.get_unit() in load_curve._factor_dict
    
    