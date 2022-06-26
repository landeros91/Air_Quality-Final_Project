#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:00:57 2022

@author: robertvanderweele
"""

import pandas as pd
from windrose import WindroseAxes
import windrose
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np



df_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Full_PM_dataset.csv')
df_PM["county"] = ''


# iterate over xls files
county = []
for value in df_PM["site"]:
    if value == 3154:
        county.append('Inyo')
        
    elif value == 2956:
        county.append("Placer")
        
    elif value == 2955:
        county.append("San Luis Obispo")   
        
    elif value == 2899:
        county.append("Los Angeles")
        
    elif value == 2948:
        county.append("El Dorado County") 
        
    elif value == 3011:
        county.append("Sacramento")
        
    elif value == 3658:
        county.append("Los Angeles")
        
    elif value == 2849:
        county.append("Los Angeles")
        
    elif value == 3026:
        county.append("Fresno")
        
    elif value == 3762:
        county.append("Fresno")
        
    else:
        county.append("None")

df_PM["county"] = county 
print(df_PM)


# small PM dataset
df_PM.to_csv('Cleaned_data/small_PM_dataset.csv')


df_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Full_wind_dataset.csv')
df_wind["county"] = ''


# iterate over xls files
county = []
for value in df_wind["site"]:
    if value == 3154:
        county.append('Inyo')
        
    elif value == 2956:
        county.append("Placer")
        
    elif value == 2955:
        county.append("San Luis Obispo")   
        
    elif value == 2899:
        county.append("Los Angeles")
        
    elif value == 2948:
        county.append("El Dorado County") 
        
    elif value == 3011:
        county.append("Sacramento")
        
    elif value == 3658:
        county.append("Los Angeles")
        
    elif value == 2849:
        county.append("Los Angeles")
        
    elif value == 3026:
        county.append("Fresno")
        
    elif value == 3762:
        county.append("Fresno")
        
    else:
        county.append("None")

df_wind["county"] = county 
print(df_wind)


# small wind dataset
df_wind.to_csv('Cleaned_data/small_wind_dataset.csv')
