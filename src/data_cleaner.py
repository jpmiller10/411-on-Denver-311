import numpy as np
import pandas as pd
import geopandas
import datetime
import json
import os
from pandas.io.json import json_normalize

def read_nbh_data(file_path):
    '''
    Creates a geopandas dataframe for Denver Statistical Neighborhoods found at: 
    https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-statistical-neighborhoods
    --Shapefiles can be converted to .geojson files with https://mapshaper.org/    
    Arguments:
        file_path: filepath for the .json file as a str i.e. 'data/nbh_stats.json'
    Returns:
        gdf: geopandas dataframe
    '''
    gdf_nbh = geopandas.read_file(file_path)  
    return gdf_nbh

def read_311_year(file_path):
    '''
    Creates dataframe for cleaning from Denver 311 info found at: 
    https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-311-service-requests-2007-to-current    
    Arguments:
        file_path: filepath for the .csv file as a str i.e. 'data/311_service_data_2018.csv'
        df_year: df_{year of the data} i.e. 2018 > df_2018
    Returns:
        df: dataframe
    '''
    df= pd.read_csv(file_path, dtype=str, encoding = "ISO-8859-1")
    return df

def keep_cols(df, cols):
    '''
    Returns df with specified columns
    
    ARGS:
        df - pd.dataFrame
        cols - list of columns
    '''
    columns_to_drop = []
    for i in df.columns:
        if i not in cols:
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
        col1: str of start time column name
        col2: str of completion time column name
    Retrun:
        df: dataframe
    ''' 
    df['Response_Time']= df[col2] - df[col1]
    df['Response_Value'] = df['Response_Time'].dt.total_seconds()/84600 
    return df

def drop_to_lat_long(df, col1, col2):
    '''
    Arguments:
        col1: str of latitude column name
        col2: str of longitude column name
    Retrun:
        df: dataframe
    ''' 
    df= df.dropna(subset=[col1, col2]) 
    return df

def convert_df_to_gdf(df):
    gdf_data = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
    return gdf_data

def to_join(gdf_data, gdf_nbh):
    gdf_data.crs = gdf_nbh.crs 
    gdf_data_nbh = geopandas.sjoin(gdf_data, gdf_nbh, how="inner", op='intersects')
    return gdf_data_nbh

def save_pickle(df, saved_name):
    df.to_pickle('data/{}_pickled_df'.format(saved_name))

def save_csv(df, saved_name):
    df.to_csv('data/{}.csv'.format(saved_name), encoding ='utf-8')


if __name__ == "__main__":

    gdf_nbh = read_nbh_data('data/nbh_stats.json')
    nbh_columns_to_keep = ['NBHD_NAME', 'geometry']
    gdf_nbh = keep_cols(gdf_nbh, nbh_columns_to_keep)


    df_2018 = read_311_year('data/311_service_data_2018.csv')
    columns_to_keep_data = ['Case Summary', 'Case Created dttm', 'Case Closed dttm',
       'Longitude', 'Latitude', 'Agency'] 
    df_2018 = keep_cols(df_2018, columns_to_keep_data)

    numeric_columns=['Longitude', 'Latitude']
    category_columns = ['Agency']
    df_2018 = to_numeric(df_2018, numeric_columns)
    df_2018 = to_datetime(df_2018, ['Case Created dttm','Case Closed dttm'])
    df_2018 = to_categorical(df_2018, category_columns)

    df_2018 = response_time(df_2018, 'Case Created dttm', 'Case Closed dttm')
    df_2018 = df_2018.rename(columns = {'Case Summary':'Case_Summary', 'Case Created dttm':'Case_Created_dttm', 'Case Closed dttm':'Case_Closed_dttm'}) 
    save_csv(df_2018, 'all_requests_2018')
    save_pickle(df_2018, 'all_requests_2018')  
    drop_to_lat_long(df_2018, 'Longitude', 'Latitude')
    gdf_data = convert_df_to_gdf(df_2018)
    gdf_data_nbh = to_join(gdf_data, gdf_nbh)
    save_csv(gdf_data_nbh, 'geo_requests_2018')
    save_pickle(gdf_data_nbh, 'geo_requests_2018') 