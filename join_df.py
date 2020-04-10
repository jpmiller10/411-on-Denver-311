from shapely.geometry import Point, Polygon, MultiPolygon
import numpy as np
import pandas as pd
import geopandas
import datetime
import json
import os
from pandas.io.json import json_normalize

def to_join(df, nbh_df):
    df.crs = nbh_df.crs 
    gdf_nbh = geopandas.sjoin(df, nbh_df, how="inner", op='intersects')
    return gdf_nbh
    
    # clean_nbh = gdf_nbh.drop(['index_right', 'NBHD_ID', 'TYPOLOGY', 'NOTES'], index = 1)
    # return clean_nbh


if __name__ == '__main__':

    nbh_df = geopandas.read_file('data/statistical_neighborhoods.json')     

    df1 = pd.read_pickle('data/pickled_df_')
    df1_drop = df1.drop(['Case Status', 'Case Source', 'Case Closed dttm', 'First Call Resolution','Neighborhood'], axis =1)
    df1_drop_more = df1_drop.dropna(subset=['Longitude', 'Latitude']) 
    gdf = geopandas.GeoDataFrame(df1_drop_more, geometry=geopandas.points_from_xy(df1_drop_more.Longitude, df1_drop_more.Latitude))
