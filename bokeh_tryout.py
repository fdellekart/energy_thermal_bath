from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
from thermal_bath import LoadCurve
from datetime import datetime
from pandas import Timestamp

DATA_SOURCE = "load_curve_thermal_bath.csv"

load_curve = LoadCurve()
load_curve.load_data(DATA_SOURCE)
load_curve.data_times_to_timestamp_index("times")
load_curve.to_kilowatts()

source = ColumnDataSource(load_curve.data)

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

p = gridplot([[sauna],[gesamt]], toolbar_location=None)


show(p)

