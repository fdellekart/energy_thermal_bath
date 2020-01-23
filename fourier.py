import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from numpy.fft import fft

#data loading and preparation
TIME_KEY = "times"
SRC_PATH = "load_curve_thermal_bath.csv"

sns.set()

load_curve = LoadCurve()
load_curve.load_data(SRC_PATH, "W")
load_curve.time_to_datetime(TIME_KEY)
load_curve.time_to_index(TIME_KEY)
load_curve.set_unit("kW")

fft_gesamt = fft(load_curve.get_data["gesamt"])

