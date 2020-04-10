import numpy as np
import pandas as pd
import datetime
import json
import os
from pandas.io.json import json_normalize

df_nbh_stats = pd.read_json('data/nbh_stats.json')
df_nbh = json_normalize(df_nbh_stats["features"])
#remove all unnecessary data - NBHD_NAME, shape, and coordinates will remain
df_nbh_shapes = df_nbh.drop(['type', 'properties.NBHD_ID', 'properties.TYPOLOGY', 'properties.NOTES'], axis =1)