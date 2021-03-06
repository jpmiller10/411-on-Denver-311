import numpy as np
import pandas as pd
import datetime
import json
import os
import folium


# Import saved df
rt= pd.read_csv('data/neighborhood_vals')
rta= pd.read_csv('data/neighborhood_agency_vals')
f = open('data/nbh_stats.json',) 
nbh_data = json.load(f) 

#create a ToolTip for Neighborhood: 
nbhtt= folium.GeoJsonTooltip(fields=('NBHD_NAME',), labels=False, sticky=False)

# Create dataframes for each agency
rta_pr = rta[rta['Agency'] == 'Parks & Recreation']
rta_ea = rta[rta['Agency'] == 'External Agency']
rta_pw = rta[rta['Agency'] == 'Public Works']
rta_eh = rta[rta['Agency'] == 'Environmental Health']
rta_sf = rta[rta['Agency'] == 'Safety']
rta_cd = rta[rta['Agency'] == 'Community Planning & Development']
rta_el = rta[rta['Agency'] == 'Excise & License']
rta_if = rta[rta['Agency'] == '311']
rta_fi = rta[rta['Agency'] == 'Finance']
rta_mo = rta[rta['Agency'] == "Mayor's Office"]
rta_cc = rta[rta['Agency'] == 'City Council']
rta_cr = rta[rta['Agency'] == 'Clerk & Recorder']
rta_ts = rta[rta['Agency'] == 'Tech Services']





# Create Folium basemap
denver_map = folium.Map(location=[39.80782,-104.831338],
                        zoom_start=11,
                        tiles="Stamen Toner")

# create Choropleth for all agency requests
folium.Choropleth(geo_data=nbh_data, data=rt,
                    name='Mean Response Time of All Agencies',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of All Agencies',
                    highlight=True).add_to(denver_map)

# create Choropleth for each agency
folium.Choropleth(geo_data=nbh_data, data=rta_pr,
                    name='Mean Response Time of Parks & Recreation',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='YlOrBr', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of Parks & Recreation',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_ea,
                    name='Mean Response Time of External Agency',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='OrRd', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of External Agency',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_pw,
                    name='Mean Response Time of Public Works',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='PuRd', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of Public Works',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_eh,
                    name='Number of Requests Environmental Health',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='RdPu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests Environmental Health',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_sf,
                    name='Mean Response Time of Safety',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='BuPu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of Safety',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_cd,
                    name='Mean Response Time of Community Planning & Development',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='PuBu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of Community Planning & Development',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_el,
                    name='Mean Response Time of Excise & License',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='PuBuGn', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of Excise & License',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_if,
                    name='Mean Response Time of 311',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='BuGn', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of 311',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_fi,
                    name='Mean Response Time of Finance',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='GnBu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of Finance',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_mo,
                    name='Mean Response Time of Mayor',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of Mayor',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_cc,
                    name='Mean Response Time of City Council',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of City Council',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_cr,
                    name='Mean Response Time of Clerk & Recorder',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='PuOr', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of Clerk & Recorder',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_ts,
                    name='Mean Response Time of Tech Services',
                    columns=['NBHD_NAME', 'mean'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='RdGy', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Mean Response Time of Tech Services',
                    show = False,
                    highlight=True).add_to(denver_map)

#create neighborhood layer
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

#add layer toggle button
folium.LayerControl().add_to(denver_map)
#save
denver_map.save('folium_mapped_means.html')
