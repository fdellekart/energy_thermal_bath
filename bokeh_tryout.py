from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from thermal_bath import LoadCurve
from datetime import datetime
from pandas import Timestamp

DATA_SOURCE = "load_curve_thermal_bath.csv"

load_curve = LoadCurve()
load_curve.load_data(DATA_SOURCE)
load_curve.data_times_to_timestamp_index("times")

source = ColumnDataSource(load_curve.data)

output_file("load_curve.html")

p = figure(title="Bokeh TryOut by Flo",
    x_axis_label="Time",
    y_axis_label="Load",
    x_axis_type="datetime",
    plot_width=1000,
    plot_height=300,
    tools="pan,crosshair,wheel_zoom,box_zoom,reset,box_select,lasso_select,save")

p.line(x="times",
    y="sauna",
    legend_label="Sauna",
    line_width=1,
    source=source)

p.circle(x="times",
    y="gesamt",
    legend_label="Gesamt",
    fill_color="white",
    line_color="red",
    line_width=1,
    source=source)

p.line(x="times",
    y="gesamt",
    legend_label="Gesamt",
    line_color="red",
    line_width=1,
    source=source)


show(p)

