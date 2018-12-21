#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:28:33 2018

@author: davecao
"""
# %% 
import pandas as pd
import matplotlib.pyplot as plt

# %% Read passenger data
# data file is yamanote_passenger_2016.csv
data_file = "data/yamanote_passenger_2016.csv"
df = pd.read_csv(data_file, sep=",")

# %% scatterplot
# 
# | -- https://matplotlib.org/tutorials/colors/colormaps.html
#  specify "seismic" 
color_map = plt.cm.get_cmap("seismic")

# circle size
max_size = 200
min_size = 10

# normalization for passengers capacity at a railway station
#     x - min
#   ----------- * (max_size - min_size) + min_size
#    max - min
#  use map() and lambda function
sizes = df["passenger"].map(lambda x: 
        ((x - df["passenger"].min()) / (df["passenger"].max() - df["passenger"].min())) * 
        (max_size - min_size) + min_size
        )

# x: latitude (lat), y: longitude (lon)
x, y = df["lat"].values, df["lon"].values

plt.scatter(x, y, s=sizes, c=df['passenger'], cmap=color_map, alpha=0.5)   
# x label
plt.xlabel("latitude")
# y label 
plt.ylabel("longitude")
plt.show()