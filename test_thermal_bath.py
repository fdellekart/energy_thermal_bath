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
    factor_dict = {'W' : 10**0,
                    'kW' : 10**3,
                    'MW' : 10**6,
                    'GW': 10**9,
                    'TW' : 10**12}
    with pytest.raises(Exception):
        load_curve.set_unit("wrong_unit")
    
    