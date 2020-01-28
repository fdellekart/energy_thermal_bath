import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from numpy.fft import fft, fftfreq

from thermal_bath import LoadCurve

output_file("fourier_gesamt.html")

load_curve = LoadCurve("properties.yaml")

#fourier transform
fft_gesamt = np.abs(fft(load_curve.data["gesamt"].to_numpy()))
freq = fftfreq(len(load_curve.data["gesamt"].to_numpy()))
freq = freq*0.25

print(fft_gesamt)
for i in freq:
    print(i)

p = figure(title="Fourier Transform of thermal bath load")

p.line(freq, fft_gesamt, line_width=2)

show(p)



