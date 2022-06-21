#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:50:21 2022

@author: robertvanderweele
"""


import pandas as pd
from windrose import WindroseAxes
import windrose
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
# Create wind speed and direction variables

df_2849_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2849_Wind_dataset.csv')
df_2849_wind.drop(df_2849_wind.columns[[0]], axis=1, inplace=True)
df_2849_wind["dateC"] = pd.to_datetime(df_2849_wind["dateC"])
df_2849_wind = df_2849_wind.sort_values(by=['dateC'])

#df['Date1'] = pd.to_datetime(df[['date','start_hour']])
#df = txt_df.drop(["year", "month", "day", "hour", "minute"], axis=1)
#df['DateC'] = txt_df['Date']
#df['DateC'] = pd.to_timedelta(txt_df.DateC).dt.total_seconds().astype(int)
#df.set_index("Date", inplace = True) 

df_2849_wind['wd'] = df_2849_wind.wd.astype(float)
df_2849_wind['ws'] = df_2849_wind.ws.astype(float)
ws = df_2849_wind["ws"] 
wd = df_2849_wind["wd"]

mask_1_2019 = (df_2849_wind['dateC'] > '01-01-2019') & (df_2849_wind['dateC'] <= '03-31-2019')
mask_2_2019 = (df_2849_wind['dateC'] > '04-01-2019') & (df_2849_wind['dateC'] <= '06-30-2019')
mask_3_2019 = (df_2849_wind['dateC'] > '06-01-2019') & (df_2849_wind['dateC'] <= '08-30-2019')
mask_4_2019 = (df_2849_wind['dateC'] > '09-01-2019') & (df_2849_wind['dateC'] <= '12-31-2019')



qrt1_2849_2019 = df_2849_wind.loc[mask_1_2019]
qrt2_2849_2019 = df_2849_wind.loc[mask_2_2019]
qrt3_2849_2019 = df_2849_wind.loc[mask_3_2019]
qrt4_2849_2019 = df_2849_wind.loc[mask_4_2019]


fig = plt.figure(figsize=(15,15))
fig.text(0.25, 1, 'Glendora-Laurel Monitoring Station - LA County', fontsize=24)
fig.suptitle('2019 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
#new_labels = ["90°", "45°", "0", "315°", "270°", "225°", "180°", "135°"]
#ax1 = WindroseAxes.from_ax(theta_labels=new_labels)
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2849_2019['wd'], qrt1_2849_2019['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")


ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2849_2019['wd'], qrt2_2849_2019['ws'],normed=True, bins=8) 
ax2.set_radii_angle()



ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2849_2019['wd'], qrt3_2849_2019['ws'],normed=True, bins=8) 
ax3.set_radii_angle()


ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2849_2019['wd'], qrt4_2849_2019['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Glendora-Laurel_2019_wind.png',dpi=300, bbox_inches = "tight")


