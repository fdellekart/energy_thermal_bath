import numpy as np
from math import pi
from numpy.fft import fft, fftfreq
from bokeh.plotting import figure, output_file, show, gridplot

output_file(r"plots\fourier_basic.html")

t = np.linspace(0, 2*np.pi, 1000, endpoint=True)
f = 3.0 # Frequency in Hz
A = 100.0 # Amplitude in Unit
y = A * np.sin(2*np.pi*f*t) # Signal

freq = fftfreq(y.size, 0.01)
fourier = fft(y)

p = figure(title="Sine Wave", tools="pan,box_zoom,reset")

p.line(np.arange(0, y.size),y, line_width=2)

f = figure(title="Fourier Transform", tools="pan,box_zoom,reset")

f.line(np.arange(0, y.size), abs(fourier), line_width=2)

gp = gridplot([[p],[f]])

show(gp)
