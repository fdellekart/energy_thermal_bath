import pandas as pd
from datetime import datetime

with open("load_curve_thermal_bath.csv", 'r') as f:
    data = pd.read_csv(f)


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
    returns dataframe with all elements of time column changed to datetime object"""
    dataframe[time_key] = string_series_to_datetime(dataframe[time_key])
    dataframe = dataframe.set_index('time_key')
    return dataframe