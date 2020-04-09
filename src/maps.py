import numpy as np
import pandas as pd
import datetime
import geopandas
import json
import os
import folium
from folium.plugins import HeatMap
from pandas.io.json import json_normalize
from branca.colormap import linear

# #Load the pickeled dataframe
# df = pd.read_pickle('data/pickled_df_')
# df = df.dropna()

#Create a map object
denver_map = folium.Map(location=[39.75782,-104.831338],
                        zoom_start=11,
                        tiles="Stamen Toner")

#Create a neighboorhood layer by adding a GeoJson file that has polygon shapes in Lat/Long. 
f = open('data/nbh_stats.json',) 
nbh_data = json.load(f) 
nbhtt= folium.GeoJsonTooltip(fields=('NBHD_NAME',), labels=False, sticky=False)

#rt = pd.read_csv('data/Neighborhood Response Times.csv')
rt = pd.read_csv('data/response_grouped_NBHD')

folium.Choropleth(geo_data=nbh_data, data=rt,
                    name='Number of Requests',
                    columns=['NBHD_NAME', 'Response_valcount'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests',
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rt,
                    name='Mean Response Time',
                    columns=['NBHD_NAME', 'Response_valmean'],
                    key_on= 'properties.NBHD_NAME',
                    fill_color='PuBuGn', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time in Days',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rt,
                    name='Max Response Time',
                    columns=['NBHD_NAME', 'Response_valmax'],
                    key_on= 'properties.NBHD_NAME',
                    fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Max Response Time in Days',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rt,
                    name='75% Response Time',
                    columns=['NBHD_NAME', 'Response_val75%'],
                    key_on= 'properties.NBHD_NAME',
                    fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='75% Response Time in Days',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rt,
                    name='Median Response Time',
                    columns=['NBHD_NAME', 'Response_val50%'],
                    key_on= 'properties.NBHD_NAME',
                    fill_color='PuBu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Median Response Time in Days',
                    show = False,
                    highlight=True).add_to(denver_map)


# YlGn
# YlGnBu
# GnBu
# BuGn
# PuBuGn
# PuBu
# BuPu
# RdPu
# PuRd
# OrRd
# YlOrRd
# YlOrBr




# folium.LayerControl().add_to(denver_map)
# denver_map.save('folium_nbh.html')

rt = pd.read_csv('data/response_grouped_Agency_NBHD')
rt_pw = rt[rt['Agency']== 'Public Works']

folium.Choropleth(geo_data=nbh_data, data=rt_pw,
                    name='Number of Requests',
                    columns=['NBHD_NAME', 'Response_valmean'],
                    key_on= 'properties.NBHD_NAME',
                    fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time in Days Pub Works',
                    show = False,
                    highlight=True).add_to(denver_map)

# rt = pd.read_csv('data/Neighborhood Response Times.csv')

# df_nbh_stats = pd.read_json('data/nbh_stats.json')
# df_nbh = json_normalize(df_nbh_stats["features"])

# color_map = folium.Map(location=[39.75782,-104.831338],
#                         zoom_start=11)

# denver_map.choropleth(
#  geo_data=df_nbh,
#  name='Number of Requests',
#  data=rt,
#  columns=['NBHD_NAME', 'count'],
#  key_on='properties.NBHD_NAME',
#  fill_color='YlGn',
#  fill_opacity=0.7,
#  line_opacity=0.2,
#  legend_name='Number of Requests'
# )
# folium.Choropleth(geo_data=nbh_data, data=rt,
#                     name='Number of Requests',
#                     columns=['NBHD_NAME', 'count'],
#                     key_on= 'properties.NBHD_NAME',
#                     nan_fill_color='white',
#                     fill_color='YlOrRd', fill_opacity=0.4, line_opacity=0.2, 
#                     legend_name='Number of Requests',
#                     highlight=True).add_to(denver_map)


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


'''
def plotDot(point, 'name', color):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    folium.CircleMarker(location=[point.Latitude, point.Longitude],
                        radius=2,
                        weight=0,#remove outline
                        popup = str('Case Summary: ' + str(point.Case_Summary) \
                                        + '\nAgency: ' + str(point.Agency) \
                                        + '\nCase Opened: ' + str(point.Case_Created_dttm) \
                                        + '\nResponse Time: '+ str(point.Response_Time) 
                                        ),
                        fill_color='#222222').add_to(denver_map)

#use df.apply(,axis=1) to iterate through every row in your dataframe
df1.apply(plotDot, axis = 1)


#Add a layer for all accidents involving cyclists
bike_map = folium.FeatureGroup(name = 'bike_map')
bike_df = df[df['BICYCLE_IND'] > 0]
map_plotter(bike_df, bike_map, "#e32522") #red dots
denver_map.add_child(bike_map)

#Add a layer for all accidents involving pedestrians 
pedestrian_map = folium.FeatureGroup(name = 'pedestrian_map')
pedestrian_df = df[df['PEDESTRIAN_IND'] > 0]
map_plotter(pedestrian_df, pedestrian_map, "#00a550") #green dots
denver_map.add_child(pedestrian_map)

#Add a layer for all accidents involving a DUI  
dui_map = folium.FeatureGroup(name = 'dui_map')
dui_df = df[df['TU1_DRIVER_HUMANCONTRIBFACTOR'] == 'DUI/DWAI/DUID']
map_plotter(dui_df, dui_map, '#e38f22') #orange dots
denver_map.add_child(dui_map)

#Add a layer for all accidents resulting in at least one fatality
fatalities_map = folium.FeatureGroup(name = 'fatalities_map')
fatalities_df = df[df['FATALITIES'] > 0]
map_plotter(fatalities_df, fatalities_map, "#7612ce") #purple dots
denver_map.add_child(fatalities_map)

Add toggle buttons for layers
folium.LayerControl().add_to(denver_map) #Add layer control to toggle on/off
denver_map.save('folium_heat.html')
'''

folium.LayerControl().add_to(denver_map)
denver_map.save('folium_color.html')