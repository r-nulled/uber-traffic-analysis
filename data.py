# Add data cleaning proccess here

import pandas as pd
import numpy as np

data = pd.read_csv("movement-speeds-hourly-new-york-2020-2.csv") # data downloaded and moved into the same directory

data = data[(data["day"] >= 9) & (data["day"] <= 15)] # filter for the dates we want
data = data[["day", "hour", "osm_way_id", "osm_start_node_id", "osm_end_node_id", "speed_mph_mean", "speed_mph_stddev"]] # remove redudant columns
data.dropna() # drop null rows
data.reset_index(drop=True, inplace=True)  # reset indices
data.to_csv("Feb9-Feb15_data") # write to csv, has about 6 million rows
print(data.head()) # shows the first couple of rows 
