from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
import sys


sys.path.append(r"C:\Users\f.dellekart\OneDrive - MPD-Innovations\Dokumente\Programming\energy_thermal_bath")


from thermal_bath import LoadCurve


load_curve = LoadCurve(r"C:\Users\f.dellekart\OneDrive - MPD-Innovations\Dokumente\Programming\energy_thermal_bath\properties.yaml")

source = ColumnDataSource(load_curve.data)

output_file(r"plots\load_curve.html")

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

