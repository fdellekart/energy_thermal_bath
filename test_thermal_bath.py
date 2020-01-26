from thermal_bath import LoadCurve
from pandas import DataFrame
import pytest
from datetime import datetime

load_curve = LoadCurve()

def test_loading():
    with pytest.raises(Exception):
        load_curve.load_data("load_curve_thermal_bath.csv", "Wrong_Unit")
    load_curve.load_data("load_curve_thermal_bath.csv", "W")
    assert isinstance(load_curve.get_data(), DataFrame)
    assert load_curve._unit == "W"

def test_time_to_datetime():
    load_curve.time_to_datetime("times")
    times = load_curve.get_data()["times"]
    is_datetime = [isinstance(el, datetime) for el in times]
    assert all(is_datetime)
    
def test_time_to_index():
    load_curve.time_to_index("times")
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
    
    