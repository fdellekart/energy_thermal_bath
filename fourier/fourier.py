import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from numpy.fft import fft, fftfreq
from math import pi

from thermal_bath import LoadCurve

output_file("fourier_gesamt.html")

load_curve = LoadCurve("properties.yaml")

#fourier transform
fft_gesamt = np.abs(fft(load_curve.data["gesamt"].to_numpy()))
freq = fftfreq(load_curve.data["gesamt"].to_numpy().size, d=2*pi/30)
freq = freq #* 30


p = figure(title="Fourier Transform of thermal bath load", tools="box_zoom,crosshair,pan,reset")

p.line(freq, fft_gesamt, line_width=2)

show(p)



