import numpy as np
import pandas as pd
import datetime
import json
import os
from pandas.io.json import json_normalize


def select_cols(df, cols):
    '''
    Returns df with specified columns
    
    ARGS:
        df - pd.dataFrame
        cols - list of columns
    '''
    columns_to_drop = []
    for i in df.columns:
        if i not in columns_to_keep:
            columns_to_drop.append(i)
    df.drop(columns_to_drop, inplace=True, axis=1)
    return df

def to_datetime(df,cols):
    '''
    Converts 'col' to datetime     
    Arguments:
        df: dataframe
        cols: a list of columns
    Returns:
        df: dataframe
    '''
    for col in cols:
        df[col] = pd.to_datetime(df[col])
    # time_range_filter = (df[col] > start) & (df[col] < end)
    # df = df[time_range_filter].copy()
    return df

def to_numeric(df, cols):
    '''
    Arguments:
        df: dataframe
        cols: a list of columns
    Retrun:
        df: dataframe
    '''
    for c in cols:
        df[c] = df[c].apply(lambda x: pd.to_numeric(x, errors='coerce'))
    return df


def to_categorical(df, cols):
    '''
    Arguments:
        df: dataframe
        cols: a list of columns
    Retrun:
        df: dataframe
    ''' 
    for c in cols:
        df[c] = df[c].astype("category")
    return df

def response_time(df, col1, col2):
    '''
    Arguments:
        col1: start time
        col2: completion time
    Retrun:
        df: dataframe
    ''' 
    df['Response Time']= df[col2] - df[col1] 
    return df
    
def save_pickle(df):
    df.to_pickle('data/pickled_df_')

def save_csv(df):
    df.to_csv('data/saved_df.csv', encoding ='utf-8')


if __name__ == '__main__':
    df_311 = pd.read_csv('data/311_service_data_2018.csv', dtype=str, encoding = "ISO-8859-1")

    numeric_columns=['Longitude', 'Latitude']
    category_columns = ['Case Status', 'Case Source', 'Agency', 'Neighborhood']
    columns_to_keep = ['Case Summary', 'Case Status', 'Case Source', 'Case Created dttm',
       'Case Closed dttm', 'First Call Resolution', 'Longitude', 'Latitude',
       'Agency', 'Neighborhood', 'Response Time']
    
    
    df_311 = to_numeric(df_311, numeric_columns)
    df_311 = to_datetime(df_311, ['Case Created dttm','Case Closed dttm'])
    df_311 = to_categorical(df_311, category_columns)
    df_311 = response_time(df_311, 'Case Created dttm', 'Case Closed dttm')
    df_311 = select_cols(df_311, columns_to_keep)
    save(df_311)
    print(df_311.columns)