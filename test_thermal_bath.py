from thermal_bath import LoadCurve
from pandas import DataFrame
import pytest
from datetime import datetime


load_curve = LoadCurve("properties.yaml")


def test_load_properties():
    prop_dict = load_curve.load_properties("properties.yaml")
    assert isinstance(prop_dict, dict)
    assert prop_dict["src_path"] == "load_curve_thermal_bath.csv"
    assert prop_dict["time_key"] == "times"
    assert prop_dict["unit"] == "W"


def test_load_data():
    assert isinstance(load_curve.data, DataFrame)
    assert load_curve.unit == "W"
    assert load_curve._time_key == "times"


def test_get_date_time():
    dt_string = "05-10-2020 17:34:12"
    dt = load_curve._get_date_time(dt_string)
    assert isinstance(dt, datetime)
    assert dt == datetime(2020, 10, 5, 17, 34, 12)


def test_time_to_index():
    index = load_curve.data.index
    is_datetime = [isinstance(el, datetime) for el in index]
    assert all(is_datetime)


def test_set_unit():
    with pytest.raises(Warning):
        load_curve.unit = "wrong_unit"

    factor_dict = load_curve._factor_dict

    data = load_curve.data

    for unit in factor_dict:
        load_curve.unit = unit
        bool_frame = abs(data - load_curve.data*factor_dict[unit]) < 0.1
        assert bool_frame.all(axis=None)


def test_moving_average():
    for key in load_curve.data.keys():
        load_curve.moving_average(key, 5)
        assert "SMA_{}".format(key) in load_curve.data.keys()

    load_curve.remove_average()

    for key in load_curve.data.keys():
        assert key[:3] != "SMA_"


def test_unit():
    assert load_curve.unit in load_curve._factor_dict
    
    