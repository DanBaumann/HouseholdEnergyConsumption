
import pandas as pd
import numpy as np 

def read_csv(filename):
    """
    Arguments
    filename: string of filename in csv or txt
    """
    df = pd.read_csv(filename, sep=';', header=0, low_memory=False,
                    infer_datetime_format=True, parse_dates={'datetime':[0,1]}, 
                    index_col=['datetime'])
    return df

def col_names(df, column_names):
    """
    Arguments
    df: dataframe
    column_names : column names in list format
    """
    df.columns = column_names
    return df

def drop_na(df):
    """
    Arguments
    df: dataframe
    """
    df['global_active_power'] = pd.to_numeric(df['global_active_power'], errors='coerce')
    df = df.dropna(subset=['global_active_power'])
    return df

def feature_engineering(df):
    """
    Arguments
    df: dataframe
    """
    df.reset_index(drop=False, inplace=True)
    df['year'] = df['datetime'].apply(lambda x: x.year)
    df['quarter'] = df['datetime'].apply(lambda x: x.quarter)
    df['month'] = df['datetime'].apply(lambda x: x.month)
    df['day'] = df['datetime'].apply(lambda x: x.day)
    df['weekday']= df.apply(lambda row: row["datetime"].weekday(),axis=1)
    df['weekday'] = (df['weekday'] < 5).astype(int)
    # Predictive power of other variables is questionable
    # much more likely to be predicted by seasonal, yearly, monthly and daily status
    df = df.loc[:,['datetime', 'global_active_power', 'voltage', 'year', 'quarter', 'month', 'day']]
    df.sort_values('datetime', inplace=True, ascending=True)
    return df

def read_weather_data(filename):
    """
    Arguments
    filename: string of filename in csv format
    """
    temperature_df = pd.read_csv(filename, index_col=0)
    temperature_df.columns = ['temperature']
    return temperature_df

def repeat_weather(temperature_df):
    """
    Arguments
    temprature_df: dataframe of temperatures
    """
    repeated_df = pd.DataFrame(np.repeat(temperature_df.values, 60, axis=0))
    repeated_df.columns = ['temperature'] 
    return repeated_df

def merge_dataframes(df, temperature_df):
    """
    Arguments
    df: dataframe
    temprature_df: dataframe of temperatures
    """
    df = df[(df.datetime >= '2006-12-18') & (df.datetime < '2010-11-13')]
    df = df.reset_index(drop=True)
    df = df.merge(temperature_df, how ='left', left_index=True, right_index=True)
    return df

def save_cleaned_df(df):
    """
    Arguments
    df: dataframe
    """
    df.set_index('datetime', inplace=True)
    df.index = pd.to_datetime(df.index)
    df = df[(df.index>='2007-01-01')]
    df = df.astype({'year': int, 'quarter': int, 'month': int, 'day': int, 'weekday':int})
    df.to_csv('final_df.csv')

def weekday(df):
    df["weekday"]= df.apply(lambda row: row["datetime"].weekday(),axis=1)
    df["weekday"] = (df["weekday"] < 5).astype(int)
    return df

def hourly_csv(df):
    data_hourly = df.resample('H').sum()
    data_hourly = data_hourly.drop(columns=data_hourly.columns[1:], axis=1)
    data_hourly.to_csv('final_hourly.csv')



