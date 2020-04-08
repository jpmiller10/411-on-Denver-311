import numpy as np
import pandas as pd
import datetime
import json
import os
import folium
from folium.plugins import HeatMap

# #Load the pickeled dataframe
df = pd.read_pickle('data/pickled_df_')
df = df.dropna()

#Create a map object
denver_map = folium.Map(location=[39.75782,-104.831338],
                        zoom_start=11,
                        tiles="Stamen Toner")

#Create a neighboorhood layer by adding a GeoJson file that has polygon shapes in Lat/Long. 
f = open('data/nbh_stats.json',) 
nbh_data = json.load(f) 
nbhtt= folium.GeoJsonTooltip(fields=('NBHD_NAME',), labels=False, sticky=False)

folium.GeoJson(
    nbh_data,
    style_function=lambda feature: {
        'fillColor': '#ffff00',
        'color': 'black',
        'weight': 2,
        'dashArray': '5, 5'
    },
    name='Neighborhood Boundries', 
    tooltip= nbhtt
).add_to(denver_map)

folium.LayerControl().add_to(denver_map)
denver_map.save('folium_nbh.html')

#Heat_map
heat_map = folium.FeatureGroup(name = 'heat_map')
max_amount = float(60)
heat_map.add_child( HeatMap( list(zip(df['Longitude'].values, df['Latitude'].values)), 
                   min_opacity=0.2,
                   max_val=max_amount,
                   radius=5.5, blur=3.5, 
                   max_zoom=1, 
                 ))
denver_map.add_child(heat_map)


def plotDot(point):
    '''input: series that contains a numeric named latitude and a numeric named longitude
    this function creates a CircleMarker and adds it to your this_map'''
    folium.CircleMarker(location=[point.Latitude, point.Longitude],
                        radius=2,
                        weight=0,#remove outline
                        popup = point.Agency,
                        fill_color='#000000').add_to(denver_map)

#use df.apply(,axis=1) to iterate through every row in your dataframe
df1.apply(plotDot, axis = 1)


# #Add a layer for all accidents involving cyclists
# bike_map = folium.FeatureGroup(name = 'bike_map')
# bike_df = df[df['BICYCLE_IND'] > 0]
# map_plotter(bike_df, bike_map, "#e32522") #red dots
# denver_map.add_child(bike_map)

# #Add a layer for all accidents involving pedestrians 
# pedestrian_map = folium.FeatureGroup(name = 'pedestrian_map')
# pedestrian_df = df[df['PEDESTRIAN_IND'] > 0]
# map_plotter(pedestrian_df, pedestrian_map, "#00a550") #green dots
# denver_map.add_child(pedestrian_map)

# #Add a layer for all accidents involving a DUI  
# dui_map = folium.FeatureGroup(name = 'dui_map')
# dui_df = df[df['TU1_DRIVER_HUMANCONTRIBFACTOR'] == 'DUI/DWAI/DUID']
# map_plotter(dui_df, dui_map, '#e38f22') #orange dots
# denver_map.add_child(dui_map)

# #Add a layer for all accidents resulting in at least one fatality
# fatalities_map = folium.FeatureGroup(name = 'fatalities_map')
# fatalities_df = df[df['FATALITIES'] > 0]
# map_plotter(fatalities_df, fatalities_map, "#7612ce") #purple dots
# denver_map.add_child(fatalities_map)

#Add toggle buttons for layers
# folium.LayerControl().add_to(denver_map) #Add layer control to toggle on/off
# denver_map.save('folium_heat.html')
