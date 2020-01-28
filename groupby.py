import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

from thermal_bath import LoadCurve

output_file("mean_over_weekdays.html")

load_curve = LoadCurve("properties.yaml")


data = load_curve.data

data["weekday"] = data.index.weekday

groupedby_weekdays = data.groupby(["weekday"]).mean()

source = ColumnDataSource(groupedby_weekdays)

p = figure(title="Mean power load over weekdays",
    x_axis_label="Weekday",
    y_axis_label="Load [kW]",
    x_axis_type="datetime")

p.line(x="weekday",
    y="lüftung",
    line_color="red",
    line_width=1,
    legend_label="Lüftung",
    source=source)

p.line(x="weekday",
    y="sauna",
    line_color="green",
    line_width=1,
    legend_label="Sauna",
    source=source)

p.line(x="weekday",
    y="gastronomie",
    line_color="blue",
    line_width=1,
    legend_label="Gastronomie",
    source=source)

p.line(x="weekday",
    y="gesundheitspark",
    line_color="orange",
    line_width=1,
    legend_label="Gesundheitspark",
    source=source)

p.line(x="weekday",
    y="technik",
    line_color="grey",
    line_width=1,
    legend_label="Technik",
    source=source)

p.line(x="weekday",
    y="gesamt",
    line_color="black",
    line_width=1,
    legend_label="Gesamt",
    source=source)

show(p)