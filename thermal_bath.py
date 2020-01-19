import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from datetime import datetime

DATA_SOURCE = "load_curve_thermal_bath.csv"

class LoadCurve:
    def __init__(self):
        self.data = None

    def load_data(self, src_path):
        with open(src_path, 'r') as f:
            self.data = pd.read_csv(f)


def get_date_time(datetime_string):
    """datetime_string: str formated as 'dd-mm-yyyy hh:mm:ss'
    Returns datetime object representing input"""
    day_int = int(datetime_string[0:2])
    month_int = int(datetime_string[3:5])
    year_int = int(datetime_string[6:10])
    hour_int = int(datetime_string[11:13])
    minute_int = int(datetime_string[14:16])
    second_int = int(datetime_string[17:19])
    return datetime(year_int, month_int, day_int, hour_int, minute_int, second_int)


def string_series_to_datetime(series):
    """series: pd.Series object consisting of str formated as 'dd-mm-yyyy hh:mm:ss' 
    Returns series with all elements as datetime objects"""
    return series.apply(get_date_time)


def df_str_times_to_timestamp_index(dataframe,time_key):
    """dataframe: pd.DataFrame object
    time_key: key of collumn that holds str formated as 'dd-mm-yyyy hh:mm:ss'
    returns dataframe with all elements of time column changed to datetime object
    timestamps as index"""
    dataframe[time_key] = string_series_to_datetime(dataframe[time_key])
    dataframe = dataframe.set_index(time_key)
    return dataframe

def plot_load_curve(df,data_key):
    source = ColumnDataSource(df)    
    output_file("load_curve.html")
    p = figure(title="load_curve", x_axis_type='datetime', x_axis_label='Time',
        y_axis_label='Load')
    p.vline_stack(['sauna', 'lüftung'], x='times', color=['blue','red'],source=source)
    p.line('times','gesamt',source=source,color='green')
    show(p)

data = df_str_times_to_timestamp_index(data, 'times')
plot_load_curve(data, 'gesamt')