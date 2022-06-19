#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:32:37 2022

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
df_2849_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2849_PM_dataset.csv')

"""
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

"""

df_2849_PM.plot(kind="scatter", x='dateC', y="value", s=df10_2.value, linestyle='solid', figsize=(15,10))
df_2849_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - San Luis Obispo - Roberto Court Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/Air_Quality/Plots/PM10.png")

"""
df2_5_2.plot(kind="scatter", x='dateC', y="value", s=df2_5_2.value, linestyle='solid', figsize=(15,10))
df2_5_2.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM2.5 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM2.5 Data - San Luis Obispo - Roberto Court Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM2.5")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/Air_Quality/Plots/PM2.5.png")
"""