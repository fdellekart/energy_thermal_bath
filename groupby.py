import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from numpy.fft import fft, fftfreq

from thermal_bath import LoadCurve

output_file("fourier_gesamt.html")

#data loading and preparation
TIME_KEY = "times"
SRC_PATH = "load_curve_thermal_bath.csv"

load_curve = LoadCurve()
load_curve.load_data(SRC_PATH, "W")
load_curve.time_to_datetime(TIME_KEY)
load_curve.time_to_index(TIME_KEY)
load_curve.set_unit("kW")
