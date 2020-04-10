import numpy as np
import pandas as pd
import datetime
import json
import os
import folium

# df = pd.read_pickle('data/geo_requests_2018_pickled_df')
#df_n = df[['Agency', 'NBHD_NAME', 'Response_Value']].groupby(['NBHD_NAME']).describe()
#df_n.to_csv('data/neighborhood_vals', encoding ='utf-8')


# rt= pd.read_csv('data/neighborhood_vals')
# df_an = df[['Agency', 'NBHD_NAME', 'Response_Value']].groupby(['Agency', 'NBHD_NAME']).describe()
# df_an.to_csv('data/neighborhood_agency_vals', encoding ='utf-8')

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
                    name='Number of Requests All Agencies',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to All Agencies',
                    highlight=True).add_to(denver_map)

# create Choropleth for each agency
folium.Choropleth(geo_data=nbh_data, data=rta_pr,
                    name='Number of Requests to Parks & Recreation',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='YlOrBr', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to Parks & Recreation',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_ea,
                    name='Number of Requests to External Agency',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='OrRd', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to External Agency',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_pw,
                    name='Number of Requests to Public Works',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='PuRd', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to Public Works',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_eh,
                    name='Number of Requests Environmental Health',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='RdPu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests Environmental Health',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_sf,
                    name='Number of Requests to Safety',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='BuPu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to Safety',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_cd,
                    name='Number of Requests to Community Planning & Development',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='PuBu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to Community Planning & Development',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_el,
                    name='Number of Requests to Excise & License',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='PuBuGn', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to Excise & License',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_if,
                    name='Number of Requests to 311',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='BuGn', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to 311',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_fi,
                    name='Number of Requests to Finance',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='GnBu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to Finance',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_mo,
                    name='Number of Requests to Mayor',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to Mayor',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_cc,
                    name='Number of Requests to City Council',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to City Council',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_cr,
                    name='Number of Requests to Clerk & Recorder',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='PuOr', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to Clerk & Recorder',
                    show = False,
                    highlight=True).add_to(denver_map)

folium.Choropleth(geo_data=nbh_data, data=rta_ts,
                    name='Number of Requests to Tech Services',
                    columns=['NBHD_NAME', 'count'],
                    key_on= 'properties.NBHD_NAME',
                    nan_fill_color='white',
                    fill_color='RdGy', fill_opacity=0.7, line_opacity=0.2, 
                    legend_name='Number of Requests to Tech Services',
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
denver_map.save('folium_mapped_requests.html')


