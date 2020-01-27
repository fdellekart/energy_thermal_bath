import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from datetime import datetime


class LoadCurve:
    """LoadCurve class
        data_source: str with csv file path containing load_curve data
        unit: str with unit of load data in csv, all values must be same unit
                W, kW, MW, GW or TW
        time_key: str with collumn key of timestamps in csv
                    must be formatted as 'dd-mm-yyyy hh:mm:ss'
                    time collumn will be turned into datetime objects and set as index of pd.df"""
    def __init__(self, data_source, unit, time_key):
        
        self._data = None
        self._factor_dict = {'W' : 10**0,
                            'kW' : 10**3,
                            'MW' : 10**6,
                            'GW': 10**9,
                            'TW' : 10**12}

        if unit in self._factor_dict:
            self._unit = unit
        else:
            raise Exception("Unit not valid, must be W, kW, MW, GW or TW")

        self._src_path = data_source
        self._time_key = time_key

        self.load_data()
        self.time_to_datetime()
        self.time_to_index()


    def load_data(self):
        """src_path: str path to csv containing load data
            unit: str unit of data in csv
            all data must have same unit W, kW, MW, GW or TW
        loads data from csv at src_path
        puts it into self._data as pd.DataFrame"""
        with open(self._src_path, 'r') as f:
            self._data = pd.read_csv(f)


    @property
    def data(self):
        """Returns pd.DataFrame holding the load_curve data"""
        return self._data


    @property
    def unit(self):
        """Returns str unit W, kW, MW, GW or TW"""
        return self._unit


    @unit.setter
    def unit(self, unit):
        """unit: 'W', 'kW', 'MW', 'GW' or 'TW'
        turns all values in self.data to parsed unit
        sets self.unit to parsed unit
        set times_to_index first"""
        if unit in self._factor_dict.keys():
            curr_factor = self._factor_dict[self._unit]
            new_factor = self._factor_dict[unit]
            self._data = self._data.apply(lambda x: (x * curr_factor) / new_factor)
            self._unit = unit
        else:
            raise Exception("KeyError: Unit not existing. Must be W, kW, MW, GW or TW")


    def _get_date_time(self, datetime_string):
        """datetime_string: str formated as 'dd-mm-yyyy hh:mm:ss'
        Returns datetime object representing input"""
        day_int = int(datetime_string[0:2])
        month_int = int(datetime_string[3:5])
        year_int = int(datetime_string[6:10])
        hour_int = int(datetime_string[11:13])
        minute_int = int(datetime_string[14:16])
        second_int = int(datetime_string[17:19])
        return datetime(year_int, month_int, day_int, hour_int, minute_int, second_int)


    def time_to_datetime(self):
        """time_key: str, collumn holding timestamp information as string
        
        turns all elements in self.data[time_key] from str formated as 'dd-mm-yyyy hh:mm:ss'
            into Timestamp""" 
        self._data[self._time_key] = self._data[self._time_key].apply(self._get_date_time)


    def time_to_index(self):
        """time_key: key of collumn that holds Timestamps
        sets time_key column to index"""
        self._data.set_index(self._time_key, inplace=True)


    def moving_average(self, col_key, window):
        """col_key: str collumn key of collumn that should be averaged.
            window: int window width
            
            Performs moving average on self._data[col_key] and adds new column with values"""
        self._data["SMA_{}".format(col_key)] = self._data[col_key].rolling(window=window).mean()


    def remove_average(self):
        """Drops all columns with keys starting 'SMA_'"""
        dropping_labels = []
        for key in self._data.keys():
            if key[:3] == "SMA_":
                dropping_labels.append(key)
        self._data.drop(dropping_labels, axis=1, inplace=True)
        

