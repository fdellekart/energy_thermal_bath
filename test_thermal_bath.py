from thermal_bath import LoadCurve
from pandas import DataFrame
import pytest

load_curve = LoadCurve()

def test_loading():
    with pytest.raises(Exception):
        load_curve.load_data("load_curve_thermal_bath.csv", "Wrong_Unit")
    load_curve.load_data("load_curve_thermal_bath.csv", "W")
    assert isinstance(load_curve.get_data(), DataFrame)
    
    