from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
from thermal_bath import LoadCurve
from datetime import datetime
from pandas import Timestamp

SRC_PATH = "load_curve_thermal_bath.csv"
TIME_KEY = "times"

load_curve = LoadCurve(SRC_PATH, "W", TIME_KEY)

source = ColumnDataSource(load_curve.get_data())

output_file("plots\load_curve.html")

lueftung = figure(title="Sauna",
    x_axis_label="Date",
    y_axis_label="Load [kW]",
    x_axis_type="datetime",
    plot_width=1000,
    plot_height=300,)

lueftung.line(x="times",
    y="lüftung",
    line_color="red",
    line_width=1,
    source=source)

gesamt = figure(title="Gesamt",
    x_axis_label="Date",
    y_axis_label= "Load [kW]",
    x_axis_type="datetime",
    plot_width=1000,
    plot_height=300) 

gesamt.line(x="times",
    y="gesamt",
    line_color="black",
    line_width=1,
    source=source)

p = gridplot([[lueftung],[gesamt]])

show(p)

