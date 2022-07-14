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

#PM10 data
df_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/small_PM_dataset.csv')
df_PM.drop(df_PM.columns[[0]], axis=1, inplace=True)
df_PM["dateC"] = pd.to_datetime(df_PM["dateC"])
df_PM = df_PM.sort_values(by=['dateC'])


# full data set statisitics
df_PM_names = df_PM['name'].unique()
df_PM_sites = df_PM['site'].unique()
df_PM_mean = df_PM.groupby(["site"]).mean()["value"]
df_PM_min = df_PM.groupby(["site"]).min()["value"]
df_PM_max = df_PM.groupby(["site"]).max()["value"]
monitoring_loc_data_counts = df_PM["site"].value_counts()

# Create a full data set stats DataFrame
stats_summary_df = pd.DataFrame({
    "Mean": df_PM_mean,
    "Max": df_PM_max,
    "Min": df_PM_min,
    "Data_Points": monitoring_loc_data_counts})

#Statistics dataset
stats_summary_df.to_csv('Cleaned_data/Stats_dataset.csv')



#grouping data by year - PM data

PM_mask_2019 = (df_PM['dateC'] > '01-01-2019') & (df_PM['dateC'] <= '12-31-2019')
PM_mask_2020 = (df_PM['dateC'] > '01-01-2020') & (df_PM['dateC'] <= '12-31-2020')

PM_2019 = df_PM.loc[PM_mask_2019]
PM_2020 = df_PM.loc[PM_mask_2020]


# 2019 data set statisitics
df_PM2019_name = PM_2019.groupby(["name"])
df_PM2019_mean = PM_2019.groupby(["site"]).mean()["value"]
df_PM2019_min = PM_2019.groupby(["site"]).min()["value"]
df_PM2019_max = PM_2019.groupby(["site"]).max()["value"]
monitoring_loc_2019_data_counts = PM_2019["site"].value_counts()

# Create a full data set stats DataFrame
stats_summary_2019_df = pd.DataFrame({
    "Mean": df_PM2019_mean,
    "Max": df_PM2019_max,
    "Min": df_PM2019_min,
    "Data_Points": monitoring_loc_2019_data_counts})

#Statistics dataset
#stats_summary_2019_df.to_csv('Cleaned_data/Stats_2019_dataset.csv')

# 2020 data set statisitics
df_PM2020_names = PM_2020['name'].unique()
df_PM2020_sites = PM_2020['site'].unique()
df_PM2020_mean = PM_2020.groupby(["site"]).mean()["value"]
df_PM2020_min = PM_2020.groupby(["site"]).min()["value"]
df_PM2020_max = PM_2020.groupby(["site"]).max()["value"]
monitoring_loc_2020_data_counts = PM_2020["site"].value_counts()

# Create a full data set stats DataFrame
stats_summary_2020_df = pd.DataFrame({
    "Mean": df_PM2020_mean,
    "Max": df_PM2020_max,
    "Min": df_PM2020_min,
    "Data_Points": monitoring_loc_2020_data_counts})

#Statistics dataset
#stats_summary_2020_df.to_csv('Cleaned_data/Stats_2020_dataset.csv')