import numpy as np
import pandas as pd
import datetime
import geopandas
import json
import os
import folium
from folium.plugins import HeatMap

def read_map_df(file_path):
    '''
    Creates dataframe for mapping created in data_cleaner.py:   
    Arguments:
        file_path: filepath for the .csv file as a str i.e. 'data/geo_requests_2018_pickled_df'
        df_year: df_{year of the data} i.e. 2018 > df_2018
    Returns:
        df: dataframe
    '''
    df= pd.read_pickle(file_path)
    return df

def create_map(map_name, latitude, longitude, style = "Stamen Toner", zoom = 11):
    '''
    Creates basemap based on location:   
    Arguments:
        map_name: name of map in str
        latitude: int of latitude of starting point
        longitude: int of longitude of starting point
        style: str of style of folium basemap
        zoom: int of starting zoom for basemap
    Returns:
        none
    '''
    map_name = folium.Map(location=[latitude,longitude],
                        zoom_start=zoom,
                        tiles=style)
    return map_name

# def plot_requests(df, feature_map, color):
#     '''
#     Plots coordinates on interactive map
#     Arguments:
#         df -> Filtered dataframe only containing relevant datapoints
#         feature_map -> the Feature group the points will be added to
#         color -> color of dots    
#     Return:
#         none
#     '''
#     for index, row in df.iterrows():
#         folium.CircleMarker(location=(row['Latitude'], row['Longitude']),
#                                     radius=.75,
#                                     color=color,
#                                     popup = str('Case Summary: ' + str(row['Case Summary']) \
#                                         + '\nAgency: ' + str(row['Agency']) \
#                                         + '\nCase Opened: ' + str(row['Case Created dttm']) \
#                                         + '\nResponse Time: '+ str(row['Response Time'])
#                                              ),
#                                     fill=True).add_to(feature_map)
def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    folium.CircleMarker(location=[point.Latitude, point.Longitude],
                    radius=2,
                    weight=0,#remove outline
                    popup = str('Agency: ' + str(point.Agency)),
                    fill_color='#222222').add_to(denver_map)

if __name__ == "__main__":
    geodf = read_map_df('data/geo_requests_2018_pickled_df')
    denver_map = create_map('denver_map', 39.75782, -104.831338)

    f = open('data/nbh_stats.json',) 
    nbh_data = json.load(f) 
    nbhtt= folium.GeoJsonTooltip(fields=('NBHD_NAME',), labels=False, sticky=False)

    folium.GeoJson(
        nbh_data,
        style_function=lambda feature: {
            'fillColor': '#82e7bc',
            'color': 'black',
            'weight': 2,
            'dashArray': '5, 5'
        },
        name='Neighborhood Boundries', 
        tooltip= nbhtt
    ).add_to(denver_map)

    folium.LayerControl().add_to(denver_map)
    denver_map.save('folium_nbh.html')

    '''
    #'Parks & Recreation'
    pr_map = folium.FeatureGroup(name = 'Parks & Recreation')
    pr_df = geodf.groupby('Agency').get_group('Parks & Recreation')
    plot_requests(pr_df, pr_map, "#709b00") 
    denver_map.add_child(pr_map) 
    # 'External Agency' 
    ea_map = folium.FeatureGroup(name = 'External Agency')
    ea_df = geodf.groupby('Agency').get_group('External Agency')
    plot_requests(ea_df, ea_map, "#bc329c") 
    denver_map.add_child(ea_map) 
    # 'Public Works' 
    pw_map = folium.FeatureGroup(name = 'Public Works')
    pw_df = geodf.groupby('Agency').get_group('Public Works')
    plot_requests(pw_df, pw_map, "#00e3ae") 
    denver_map.add_child(pw_map) 
    # 'Environmental Health' 
    eh_map = folium.FeatureGroup(name = 'Environmental Health')
    eh_df = geodf.groupby('Agency').get_group('Environmental Health')
    plot_requests(eh_df, eh_map, "#eb3c6c")
    denver_map.add_child(eh_map) 
    # 'Safety' 
    sf_map = folium.FeatureGroup(name = 'Safety')
    sf_df = geodf.groupby('Agency').get_group('Safety')
    plot_requests(sf_df, sf_map, "#007726")
    denver_map.add_child(sf_map) 
    # 'Community Planning & Development'
    cd_map = folium.FeatureGroup(name = 'Community Planning & Development')
    cd_df = geodf.groupby('Agency').get_group('Community Planning & Development')
    plot_requests(cd_df, cd_map, "#430553")
    denver_map.add_child(cd_map)  
    # 'Excise & License' 
    el_map = folium.FeatureGroup(name = 'Excise & License')
    el_df = geodf.groupby('Agency').get_group('Excise & License')
    plot_requests(el_df, el_map, "#b8e27a")
    denver_map.add_child(el_map) 
    # '311' 
    if_map = folium.FeatureGroup(name = '311')
    if_df = geodf.groupby('Agency').get_group('311')
    plot_requests(if_df, if_map, "#b81429")
    denver_map.add_child(if_map) 
    # 'Finance' 
    fi_map = folium.FeatureGroup(name = 'Finance')
    fi_df = geodf.groupby('Agency').get_group('Finance')
    plot_requests(fi_df, fi_map, "#2bafff")
    denver_map.add_child(fi_map) 
    # "Mayor's Office"
    mo_map = folium.FeatureGroup(name = "Mayor's Office")
    mo_df = geodf.groupby('Agency').get_group("Mayor's Office")
    plot_requests(mo_df, mo_map, "#660017")
    denver_map.add_child(mo_map) 
    # 'City Council' 
    cc_map = folium.FeatureGroup(name = 'City Council')
    cc_df = geodf.groupby('Agency').get_group('City Council')
    plot_requests(cc_df, cc_map, "#ade296")
    denver_map.add_child(cc_map) 
    # 'Clerk & Recorder'
    cr_map = folium.FeatureGroup(name = 'Clerk & Recorder')
    cr_df = geodf.groupby('Agency').get_group('Clerk & Recorder')
    plot_requests(cr_df, cr_map, "#d06814")
    denver_map.add_child(cr_map) 
    # 'Tech Services'
    ts_map = folium.FeatureGroup(name = 'Tech Services')
    ts_df = geodf.groupby('Agency').get_group('Tech Services')
    plot_requests(ts_df, ts_map, "#005c24")
    denver_map.add_child(ts_map) 
    '''


#use df.apply(,axis=1) to iterate through every row in your dataframe
    # geodf.apply(plotDot, axis = 1)
    
    denver_map.save('folium_311_2018_points.html')