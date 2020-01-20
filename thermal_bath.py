import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from datetime import datetime


class LoadCurve:
    def __init__(self):
        self.data = None
        self.unit = None


    def load_data(self, src_path, unit):
        """src_path: str path to csv containing load data
            unit: str unit of data in csv
            all data must have same unit W, kW, MW, GW or TW
        loads data from csv at src_path
        puts it into self.data as pd.DataFrame"""
        self.unit = unit
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


    def time_to_datetime(self, time_key):
        """time_key: str, collumn holding timestamp information as string
        
        turns all elements in self.data[time_key] from str formated as 'dd-mm-yyyy hh:mm:ss'
            into Timestamp""" 
        self.data[time_key] = self.data[time_key].apply(self.get_date_time)


    def time_to_index(self,time_key):
        """time_key: key of collumn that holds Timestamps
        sets time_key column to index"""
        self.data.set_index(time_key, inplace=True)


    def set_unit(self, unit):
        """unit: 'W', 'kW', 'MW', 'GW' or 'TW'
        turns all values in self.data to parsed unit
        sets self.unit to parsed unit
        set times_to_index first"""
        factor_dict = {'W' : 10**0, 'kW' : 10**3, 'MW' : 10**6, 'GW': 10**9, 'TW' : 10**12}
        if unit in factor_dict.keys():
            for key in self.data:
               self.data[key] = self.data[key].apply(lambda x: (x * factor_dict[self.unit]) / factor_dict[unit])
            self.unit = unit
        else:
            raise Exception("KeyError: Unit not existing. Must be W, kW, MW, GW or TW")