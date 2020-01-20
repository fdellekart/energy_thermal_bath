import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from datetime import datetime


class LoadCurve:
    def __init__(self):
        self.data = None


    def load_data(self, src_path):
        """loads data from csv at src_path
        puts it into self.data as pd.DataFrame"""
        with open(src_path, 'r') as f:
            self.data = pd.read_csv(f)


    def get_date_time(self,datetime_string):
        """datetime_string: str formated as 'dd-mm-yyyy hh:mm:ss'
        Returns datetime object representing input"""
        day_int = int(datetime_string[0:2])
        month_int = int(datetime_string[3:5])
        year_int = int(datetime_string[6:10])
        hour_int = int(datetime_string[11:13])
        minute_int = int(datetime_string[14:16])
        second_int = int(datetime_string[17:19])
        return datetime(year_int, month_int, day_int, hour_int, minute_int, second_int)


    def string_series_to_datetime(self, time_key):
        """series: pd.Series object consisting of str formated as 'dd-mm-yyyy hh:mm:ss' 
        Returns series with all elements as datetime objects"""
        self.data[time_key] = self.data[time_key].apply(self.get_date_time)


    def times_to_index(self,time_key):
        """time_key: key of collumn that holds Timestamps
        sets index "time_key" column to index"""
        self.data.set_index(time_key, inplace=True)

    def to_kilowatts(self):
        for key in self.data:
            self.data[key].apply(lambda x: x/1000)
        