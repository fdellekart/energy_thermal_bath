import sys
import pandas as pd
import numpy as np
from math import pi
from bokeh.plotting import figure, output_file, show
from numpy.fft import fft, fftfreq

sys.path.append(r"C:\Users\f.dellekart\OneDrive - MPD-Innovations\Dokumente\Programming\energy_thermal_bath")

from thermal_bath import LoadCurve

output_file(r"C:\Users\f.dellekart\OneDrive - MPD-Innovations\Dokumente\Programming\energy_thermal_bath\visualization\fourier_gesamt.html")

load_curve = LoadCurve("properties.yaml")

gesamt_signal = load_curve.data["gesamt"]

freq = fftfreq(gesamt_signal.size, 1/96)
fft_gesamt = abs(fft(gesamt_signal))

p = figure(title="Fourier Transform of thermal bath load", tools="box_zoom,crosshair,pan,reset")

p.line(freq, fft_gesamt, line_width=2)

show(p)



