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

CSV_file_PM10 = (r'/Users/robertvanderweele/git/Air_Q-project raw data/PM10/*.csv')

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

CSV_file_wind = (r'/Users/robertvanderweele/git/Air_Q-project raw data/Wind/*.csv')

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
Wind_DATA_df.drop(Wind_DATA_df.columns[[9]], axis=1, inplace=True)

#drop rows with NANs wind data
Wind_DATA_df = Wind_DATA_df.dropna(how='any')

#combine date and start hour to datetime64[ns] in a new column - Wind Data
Wind_DATA_df['start_hour'] = Wind_DATA_df['start_hour'].astype(int)
Wind_DATA_df['dateC'] = pd.to_datetime(Wind_DATA_df.date) + Wind_DATA_df.start_hour.astype('timedelta64[h]')

#create a copy of the cleaned wind dataframe
Wind_DATA_df2 = Wind_DATA_df


Wind_DATA_df2.drop(Wind_DATA_df2.columns[[11]], axis=1, inplace=True)
Wind_DATA_df2.drop(Wind_DATA_df2.columns[[10]], axis=1, inplace=True)
Wind_DATA_df2.drop(Wind_DATA_df2.columns[[9]], axis=1, inplace=True)
Wind_DATA_df2.drop(Wind_DATA_df2.columns[[8]], axis=1, inplace=True)
Wind_DATA_df2.drop(Wind_DATA_df2.columns[[7]], axis=1, inplace=True)
Wind_DATA_df2.drop(Wind_DATA_df2.columns[[5]], axis=1, inplace=True)
Wind_DATA_df2.drop(Wind_DATA_df2.columns[[2]], axis=1, inplace=True)
Wind_DATA_df2.drop(Wind_DATA_df2.columns[[1]], axis=1, inplace=True)


#grouping data by quarter - Wind data

Wind_mask_1 = (Wind_DATA_df2['dateC'] > '01-01-2019') & (Wind_DATA_df2['dateC'] <= '03-31-2019')
Wind_mask_2 = (Wind_DATA_df2['dateC'] > '04-01-2019') & (Wind_DATA_df2['dateC'] <= '06-30-2019')
Wind_mask_3 = (Wind_DATA_df2['dateC'] > '06-01-2019') & (Wind_DATA_df2['dateC'] <= '08-30-2019')
Wind_mask_4 = (Wind_DATA_df2['dateC'] > '09-01-2019') & (Wind_DATA_df2['dateC'] <= '12-31-2019')

Wind_mask_5 = (Wind_DATA_df2['dateC'] > '01-01-2020') & (Wind_DATA_df2['dateC'] <= '03-31-2020')
Wind_mask_6 = (Wind_DATA_df2['dateC'] > '04-01-2020') & (Wind_DATA_df2['dateC'] <= '06-30-2020')
Wind_mask_7 = (Wind_DATA_df2['dateC'] > '06-01-2020') & (Wind_DATA_df2['dateC'] <= '08-30-2020')
Wind_mask_8 = (Wind_DATA_df2['dateC'] > '09-01-2020') & (Wind_DATA_df2['dateC'] <= '12-31-2020')

Wind_qrt_1_2019 = Wind_DATA_df2.loc[Wind_mask_1]
Wind_qrt_2_2019 = Wind_DATA_df2.loc[Wind_mask_2]
Wind_qrt_3_2019 = Wind_DATA_df2.loc[Wind_mask_3]
Wind_qrt_4_2019 = Wind_DATA_df2.loc[Wind_mask_4]

Wind_qrt_1_2020 = Wind_DATA_df2.loc[Wind_mask_5]
Wind_qrt_2_2020 = Wind_DATA_df2.loc[Wind_mask_6]
Wind_qrt_3_2020 = Wind_DATA_df2.loc[Wind_mask_7]
Wind_qrt_4_2020 = Wind_DATA_df2.loc[Wind_mask_8]


#drop columns with no data - PM data
PM10_DATA_df.drop('monitoring_id', axis=1, inplace=True)
PM10_DATA_df.drop(PM10_DATA_df.columns[[12]], axis=1, inplace=True)

#drop rows with NANs PM data
PM10_DATA_df = PM10_DATA_df.dropna(how='any')


#combine date and start hour to datetime64[ns] in a new column - PM Data
PM10_DATA_df['start_hour'] = PM10_DATA_df['start_hour'].astype(int)
PM10_DATA_df['dateC'] = pd.to_datetime(PM10_DATA_df.date) + PM10_DATA_df.start_hour.astype('timedelta64[h]')

#create a copy of the cleaned PM dataframe
PM10_DATA_df2 = PM10_DATA_df


PM10_DATA_df2.drop(PM10_DATA_df2.columns[[11]], axis=1, inplace=True)
PM10_DATA_df2.drop(PM10_DATA_df2.columns[[7]], axis=1, inplace=True)
PM10_DATA_df2.drop(PM10_DATA_df2.columns[[6]], axis=1, inplace=True)
PM10_DATA_df2.drop(PM10_DATA_df2.columns[[4]], axis=1, inplace=True)
PM10_DATA_df2.drop(PM10_DATA_df2.columns[[2]], axis=1, inplace=True)
PM10_DATA_df2.drop(PM10_DATA_df2.columns[[1]], axis=1, inplace=True)


#grouping data by quarter - PM data

PM_mask_1 = (PM10_DATA_df2['dateC'] > '01-01-2019') & (PM10_DATA_df2['dateC'] <= '03-31-2019')
PM_mask_2 = (PM10_DATA_df2['dateC'] > '04-01-2019') & (PM10_DATA_df2['dateC'] <= '06-30-2019')
PM_mask_3 = (PM10_DATA_df2['dateC'] > '06-01-2019') & (PM10_DATA_df2['dateC'] <= '08-30-2019')
PM_mask_4 = (PM10_DATA_df2['dateC'] > '09-01-2019') & (PM10_DATA_df2['dateC'] <= '12-31-2019')

PM_mask_5 = (PM10_DATA_df2['dateC'] > '01-01-2020') & (PM10_DATA_df2['dateC'] <= '03-31-2020')
PM_mask_6 = (PM10_DATA_df2['dateC'] > '04-01-2020') & (PM10_DATA_df2['dateC'] <= '06-30-2020')
PM_mask_7 = (PM10_DATA_df2['dateC'] > '06-01-2020') & (PM10_DATA_df2['dateC'] <= '08-30-2020')
PM_mask_8 = (PM10_DATA_df2['dateC'] > '09-01-2020') & (PM10_DATA_df2['dateC'] <= '12-31-2020')

PM_qrt_1_2019 = PM10_DATA_df2.loc[PM_mask_1]
PM_qrt_2_2019 = PM10_DATA_df2.loc[PM_mask_2]
PM_qrt_3_2019 = PM10_DATA_df2.loc[PM_mask_3]
PM_qrt_4_2019 = PM10_DATA_df2.loc[PM_mask_4]

PM_qrt_1_2020 = PM10_DATA_df2.loc[PM_mask_5]
PM_qrt_2_2020 = PM10_DATA_df2.loc[PM_mask_6]
PM_qrt_3_2020 = PM10_DATA_df2.loc[PM_mask_7]
PM_qrt_4_2020 = PM10_DATA_df2.loc[PM_mask_8]


#Export cleaned data sets

#full wind dataset
Wind_DATA_df.to_csv('Cleaned_data/Full_wind_dataset.csv')

#full PM dataset
PM10_DATA_df.to_csv('Cleaned_data/Full_PM_dataset.csv')

# small wind dataset
Wind_DATA_df2.to_csv('Cleaned_data/small_wind_dataset.csv')

#full PM dataset
PM10_DATA_df2.to_csv('Cleaned_data/small_PM_dataset.csv')

def extract_PM_sites(site):
    if site == '3154':
        site_3154_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('3154')]
        return site_3154_PM1.to_csv('Cleaned_data/Site_3154_PM_dataset.csv')
    
    elif site == '3011':
        site_3011_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('3011')]
        return site_3011_PM1.to_csv('Cleaned_data/Site_3011_PM_dataset.csv')
    
    elif site == '2899':
        site_2899_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('2899')]
        return site_2899_PM1.to_csv('Cleaned_data/Site_2899_PM_dataset.csv')
    
    elif site == '2955':
        site_2955_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('2955')]
        return site_2955_PM1.to_csv('Cleaned_data/Site_2955_PM_dataset.csv')
    
    elif site == '3762':
        site_3762_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('3762')]
        return site_3762_PM1.to_csv('Cleaned_data/Site_3762_PM_dataset.csv')
    
    elif site == '3658':
        site_3658_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('3658')]
        return site_3658_PM1.to_csv('Cleaned_data/Site_3658_PM_dataset.csv')
    
    elif site == '2956':
        site_2956_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('2956')]
        return site_2956_PM1.to_csv('Cleaned_data/Site_2956_PM_dataset.csv')
         
    elif site == '2948':
        site_2948_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('2948')]
        return site_2948_PM1.to_csv('Cleaned_data/Site_2948_PM_dataset.csv')
    
    elif site == '2849':
        site_2849_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('2849')]
        return site_2849_PM1.to_csv('Cleaned_data/Site_2849_PM_dataset.csv')
    
    elif site == '3026':
        site_3026_PM1 = PM10_DATA_df2[PM10_DATA_df2.site.str.contains('3026')]
        return site_3026_PM1.to_csv('Cleaned_data/Site_3026_PM_dataset.csv')
    
    else:
        print("not found")
    
def extract_Wind_sites(site):
    if site == '3154':
        site_3154_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('3154')]
        return site_3154_Wind1.to_csv('Cleaned_data/Site_3154_Wind_dataset.csv')
    
    elif site == '3011':
        site_3011_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('3011')]
        return site_3011_Wind1.to_csv('Cleaned_data/Site_3011_Wind_dataset.csv')
    
    elif site == '2899':
        site_2899_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('2899')]
        return site_2899_Wind1.to_csv('Cleaned_data/Site_2899_Wind_dataset.csv')
    
    elif site == '2955':
        site_2955_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('2955')]
        return site_2955_Wind1.to_csv('Cleaned_data/Site_2955_Wind_dataset.csv')
    
    elif site == '3762':
        site_3762_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('3762')]
        return site_3762_Wind1.to_csv('Cleaned_data/Site_3762_Wind_dataset.csv')
    
    elif site == '3658':
        site_3658_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('3658')]
        return site_3658_Wind1.to_csv('Cleaned_data/Site_3658_Wind_dataset.csv')
    
    elif site == '2956':
        site_2956_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('2956')]
        return site_2956_Wind1.to_csv('Cleaned_data/Site_2956_Wind_dataset.csv')
         
    elif site == '2948':
        site_2948_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('2948')]
        return site_2948_Wind1.to_csv('Cleaned_data/Site_2948_Wind_dataset.csv')
    
    elif site == '2849':
        site_2849_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('2849')]
        return site_2849_Wind1.to_csv('Cleaned_data/Site_2849_Wind_dataset.csv')
    
    elif site == '3026':
        site_3026_Wind1 = Wind_DATA_df2[Wind_DATA_df2.site.str.contains('3026')]
        return site_3026_Wind1.to_csv('Cleaned_data/Site_3026_Wind_dataset.csv')
    
    else:
        print("not found")













