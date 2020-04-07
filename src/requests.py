import numpy as np
import pandas as pd
import datetime
import json
import os

df = pd.read_csv('data/service_requests.csv', dtype=str, encoding = "ISO-8859-1")