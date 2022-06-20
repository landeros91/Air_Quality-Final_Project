#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:54:21 2022

@author: robertvanderweele
"""

# Dependencies and Setup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import csv

plt.style.use('default')

#PM10 data monitoring location # 2849
df_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/small_PM_dataset.csv')
df_PM.drop(df_PM.columns[[0]], axis=1, inplace=True)
df_PM["dataC"] = pd.to_datetime(df_PM["dateC"])
df_PM = df_PM.sort_values(by=['dateC'])


#statisitics
df_PM_names = df_PM['name'].unique()
df_PM_sites = df_PM['site'].unique()
df_PM_mean = df_PM.groupby(["site"]).mean()["value"]
df_PM_min = df_PM.groupby(["site"]).min()["value"]
df_PM_max = df_PM.groupby(["site"]).max()["value"]
monitoring_loc_data_counts = df_PM["site"].value_counts()

# Create a stats DataFrame
stats_summary_df = pd.DataFrame({
    "Monitoring_Location_Name": df_PM_names,
    "Mean": df_PM_mean,
    "Max": df_PM_max,
    "Min": df_PM_min,
    "Data_Points": monitoring_loc_data_counts})

#Statistics dataset
stats_summary_df.to_csv('Cleaned_data/Stats_dataset.csv')