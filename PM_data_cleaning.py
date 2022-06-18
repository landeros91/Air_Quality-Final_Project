#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 19:13:06 2022

@author: robertvanderweele
"""

import pandas as pd
import numpy as np
import glob
#from pandas import ExcelWriter
#from matplotlib import pyplot as plt
#from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
#import seaborn as sns
#import datetime


#add multiple csv files with PM10 Data

CSV_file_PM10 = (r'/Users/robertvanderweele/git/Air_Quality-Final_Project/rawdata/PM10/*.csv')

CSV_files_PM10 =  glob.glob(CSV_file_PM10)
#empty list
frames = []

# iterate over xls files
for file in CSV_files_PM10:
    #read into dateframe
    df = pd.read_csv((file))
    frames.append(df)

PM10_DATA_df = pd.concat((frames), ignore_index=True)

#add multiple csv files with wind Data

CSV_file_wind = (r'/Users/robertvanderweele/git/Air_Quality-Final_Project/rawdata/Wind/*.csv')

CSV_files_wind =  glob.glob(CSV_file_wind)
#empty list
frames1 = []

# iterate over xls files
for files in CSV_files_wind:
    #read into dateframe
    df = pd.read_csv((files))
    frames1.append(df)

Wind_DATA_df = pd.concat((frames1), ignore_index=True)

#drop columns with no data - wind data
Wind_DATA_df.drop(Wind_DATA_df.columns[[17]], axis=1, inplace=True)
Wind_DATA_df.drop(Wind_DATA_df.columns[[16]], axis=1, inplace=True)



#drop columns with no data - PM data
PM10_DATA_df.drop('monitoring_id', axis=1, inplace=True)
PM10_DATA_df.drop(PM10_DATA_df.columns[[12]], axis=1, inplace=True)

#drop rows with NANs PM data
PM10_DATA_df = PM10_DATA_df.dropna(how='any')


#combine date and start hour to datetime64[ns] in a new column - PM Data
PM10_DATA_df['start_hour'] = PM10_DATA_df['start_hour'].astype(int)
PM10_DATA_df['dateC'] = pd.to_datetime(PM10_DATA_df.date) + PM10_DATA_df.start_hour.astype('timedelta64[h]')


#grouping data by quarter - PM data

PM_mask_1 = (PM10_DATA_df['dateC'] > '01-01-2019') & (PM10_DATA_df['dateC'] <= '03-31-2019')
PM_mask_2 = (PM10_DATA_df['dateC'] > '04-01-2019') & (PM10_DATA_df['dateC'] <= '06-30-2019')
PM_mask_3 = (PM10_DATA_df['dateC'] > '06-01-2019') & (PM10_DATA_df['dateC'] <= '08-30-2019')
PM_mask_4 = (PM10_DATA_df['dateC'] > '09-01-2019') & (PM10_DATA_df['dateC'] <= '12-31-2019')

PM_mask_5 = (PM10_DATA_df['dateC'] > '01-01-2020') & (PM10_DATA_df['dateC'] <= '03-31-2020')
PM_mask_6 = (PM10_DATA_df['dateC'] > '04-01-2020') & (PM10_DATA_df['dateC'] <= '06-30-2020')
PM_mask_7 = (PM10_DATA_df['dateC'] > '06-01-2020') & (PM10_DATA_df['dateC'] <= '08-30-2020')
PM_mask_8 = (PM10_DATA_df['dateC'] > '09-01-2020') & (PM10_DATA_df['dateC'] <= '12-31-2020')

qrt_1_2019 = PM10_DATA_df.loc[PM_mask_1]
qrt_2_2019 = PM10_DATA_df.loc[PM_mask_2]
qrt_3_2019 = PM10_DATA_df.loc[PM_mask_3]
qrt_4_2019 = PM10_DATA_df.loc[PM_mask_4]

qrt_1_2020 = PM10_DATA_df.loc[PM_mask_5]
qrt_2_2020 = PM10_DATA_df.loc[PM_mask_6]
qrt_3_2020 = PM10_DATA_df.loc[PM_mask_7]
qrt_4_2020 = PM10_DATA_df.loc[PM_mask_8]