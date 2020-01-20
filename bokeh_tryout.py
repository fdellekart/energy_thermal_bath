from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
from thermal_bath import LoadCurve
from datetime import datetime
from pandas import Timestamp

DATA_SOURCE = "load_curve_thermal_bath.csv"
TIME_KEY = "times"

load_curve = LoadCurve()
load_curve.load_data(DATA_SOURCE, "W")
load_curve.time_to_datetime(TIME_KEY)
load_curve.time_to_index(TIME_KEY)
load_curve.set_unit("kW")
load_curve.moving_average("sauna", 3)

source = ColumnDataSource(load_curve.get_data())

output_file("load_curve.html")

sauna = figure(title="Sauna",
    x_axis_label="Date",
    y_axis_label="Load [kW]",
    x_axis_type="datetime",
    plot_width=1000,
    plot_height=300,)

sauna.line(x="times",
    y="sauna",
    line_color="red",
    line_width=1,
    source=source)

# p.circle(x="times",
#     y="gesamt",
#     legend_label="Gesamt",
#     fill_color="white",
#     line_color="red",
#     line_width=1,
#     source=source)

sauna_sma = figure(title="SMA Sauna",
    x_axis_label="Date",
    y_axis_label= "Load [kW]",
    x_axis_type="datetime",
    plot_width=1000,
    plot_height=300) 

sauna_sma.line(x="times",
    y="SMA sauna",
    line_color="black",
    line_width=1,
    source=source)

p = gridplot([[sauna],[sauna_sma]])

show(p)

