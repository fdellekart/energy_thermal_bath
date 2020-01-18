import pandas as pd
from datetime import datetime

with open("load_curve_thermal_bath.csv", 'r') as f:
    data = pd.read_csv(f)

#print(data)

#print(data.loc[0,'times'])


def get_date_time(datetime_string):
    day_int = int(datetime_string[0:2])
    month_int = int(datetime_string[3:5])
    year_int = int(datetime_string[6:10])
    hour_int = int(datetime_string[11:13])
    minute_int = int(datetime_string[14:16])
    second_int = int(datetime_string[17:19])
    return datetime(year_int, month_int, day_int, hour_int, minute_int, second_int)

def string_series_to_datetime(series):
    return series.apply(get_date_time)

def dataframe_str_times_to_timestamp(dataframe, time_key):
    dataframe[time_key] = string_series_to_datetime(dataframe[time_key])
    return dataframe
