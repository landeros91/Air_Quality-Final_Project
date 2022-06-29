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


# Create wind roses for Glendora-Laurel Monitoring Station

df_2849_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2849_Wind_dataset.csv')
df_2849_wind.drop(df_2849_wind.columns[[0]], axis=1, inplace=True)
df_2849_wind["dateC"] = pd.to_datetime(df_2849_wind["dateC"])
df_2849_wind = df_2849_wind.sort_values(by=['dateC'])


df_2849_wind['wd'] = df_2849_wind.wd.astype(float)
df_2849_wind['ws'] = df_2849_wind.ws.astype(float)
ws = df_2849_wind["ws"] 
wd = df_2849_wind["wd"]


# seperate into quarters by year
mask_1_2019 = (df_2849_wind['dateC'] > '01-01-2019') & (df_2849_wind['dateC'] <= '03-31-2019')
mask_2_2019 = (df_2849_wind['dateC'] > '04-01-2019') & (df_2849_wind['dateC'] <= '06-30-2019')
mask_3_2019 = (df_2849_wind['dateC'] > '06-01-2019') & (df_2849_wind['dateC'] <= '08-30-2019')
mask_4_2019 = (df_2849_wind['dateC'] > '09-01-2019') & (df_2849_wind['dateC'] <= '12-31-2019')


qrt1_2849_2019 = df_2849_wind.loc[mask_1_2019]
qrt2_2849_2019 = df_2849_wind.loc[mask_2_2019]
qrt3_2849_2019 = df_2849_wind.loc[mask_3_2019]
qrt4_2849_2019 = df_2849_wind.loc[mask_4_2019]


mask_1_2020 = (df_2849_wind['dateC'] > '01-01-2020') & (df_2849_wind['dateC'] <= '03-31-2020')
mask_2_2020 = (df_2849_wind['dateC'] > '04-01-2020') & (df_2849_wind['dateC'] <= '06-30-2020')
mask_3_2020 = (df_2849_wind['dateC'] > '06-01-2020') & (df_2849_wind['dateC'] <= '08-30-2020')
mask_4_2020 = (df_2849_wind['dateC'] > '09-01-2020') & (df_2849_wind['dateC'] <= '12-31-2020')

qrt1_2849_2020 = df_2849_wind.loc[mask_1_2020]
qrt2_2849_2020 = df_2849_wind.loc[mask_2_2020]
qrt3_2849_2020 = df_2849_wind.loc[mask_3_2020]
qrt4_2849_2020 = df_2849_wind.loc[mask_4_2020]

# 2019 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.25, 1, 'Glendora-Laurel Monitoring Station - LA County', fontsize=24)
fig.suptitle('2019 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
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


# 2020 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.25, 1, 'Glendora-Laurel Monitoring Station - LA County', fontsize=24)
fig.suptitle('2020 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2849_2020['wd'], qrt1_2849_2020['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2849_2020['wd'], qrt2_2849_2020['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2849_2020['wd'], qrt3_2849_2020['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2849_2020['wd'], qrt4_2849_2020['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Glendora-Laurel_2020_wind.png',dpi=300, bbox_inches = "tight")


# Create wind roses for Sacramento-T Street

df_3011_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_3011_Wind_dataset.csv')
df_3011_wind.drop(df_3011_wind.columns[[0]], axis=1, inplace=True)
df_3011_wind["dateC"] = pd.to_datetime(df_3011_wind["dateC"])
df_3011_wind = df_3011_wind.sort_values(by=['dateC'])


df_3011_wind['wd'] = df_3011_wind.wd.astype(float)
df_3011_wind['ws'] = df_3011_wind.ws.astype(float)
ws = df_3011_wind["ws"] 
wd = df_3011_wind["wd"]


# seperate into quarters by year
mask_1_2019 = (df_3011_wind['dateC'] > '01-01-2019') & (df_3011_wind['dateC'] <= '03-31-2019')
mask_2_2019 = (df_3011_wind['dateC'] > '04-01-2019') & (df_3011_wind['dateC'] <= '06-30-2019')
mask_3_2019 = (df_3011_wind['dateC'] > '06-01-2019') & (df_3011_wind['dateC'] <= '08-30-2019')
mask_4_2019 = (df_3011_wind['dateC'] > '09-01-2019') & (df_3011_wind['dateC'] <= '12-31-2019')


qrt1_3011_2019 = df_3011_wind.loc[mask_1_2019]
qrt2_3011_2019 = df_3011_wind.loc[mask_2_2019]
qrt3_3011_2019 = df_3011_wind.loc[mask_3_2019]
qrt4_3011_2019 = df_3011_wind.loc[mask_4_2019]


mask_1_2020 = (df_3011_wind['dateC'] > '01-01-2020') & (df_3011_wind['dateC'] <= '03-31-2020')
mask_2_2020 = (df_3011_wind['dateC'] > '04-01-2020') & (df_3011_wind['dateC'] <= '06-30-2020')
mask_3_2020 = (df_3011_wind['dateC'] > '06-01-2020') & (df_3011_wind['dateC'] <= '08-30-2020')
mask_4_2020 = (df_3011_wind['dateC'] > '09-01-2020') & (df_3011_wind['dateC'] <= '12-31-2020')

qrt1_3011_2020 = df_3011_wind.loc[mask_1_2020]
qrt2_3011_2020 = df_3011_wind.loc[mask_2_2020]
qrt3_3011_2020 = df_3011_wind.loc[mask_3_2020]
qrt4_3011_2020 = df_3011_wind.loc[mask_4_2020]

# 2019 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.17, 1, 'Sacramento-T Street Monitoring Station - Sacramento County', fontsize=24)
fig.suptitle('2019 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_3011_2019['wd'], qrt1_3011_2019['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_3011_2019['wd'], qrt2_3011_2019['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_3011_2019['wd'], qrt3_3011_2019['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_3011_2019['wd'], qrt4_3011_2019['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Sacramento-T_Street_2019_wind.png',dpi=300, bbox_inches = "tight")


# 2020 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.17, 1, 'Sacramento-T Street Monitoring Station - Sacramento County', fontsize=24)
fig.suptitle('2020 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_3011_2020['wd'], qrt1_3011_2020['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_3011_2020['wd'], qrt2_3011_2020['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_3011_2020['wd'], qrt3_3011_2020['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_3011_2020['wd'], qrt4_3011_2020['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Sacramento-T_Street_2020_wind.png',dpi=300, bbox_inches = "tight")



# Create wind roses for Lancaster-43301 Division Street

df_3658_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_3658_Wind_dataset.csv')
df_3658_wind.drop(df_3658_wind.columns[[0]], axis=1, inplace=True)
df_3658_wind["dateC"] = pd.to_datetime(df_3658_wind["dateC"])
df_3658_wind = df_3658_wind.sort_values(by=['dateC'])


df_3658_wind['wd'] = df_3658_wind.wd.astype(float)
df_3658_wind['ws'] = df_3658_wind.ws.astype(float)
ws = df_3658_wind["ws"] 
wd = df_3658_wind["wd"]


# seperate into quarters by year
mask_1_2019 = (df_3658_wind['dateC'] > '01-01-2019') & (df_3658_wind['dateC'] <= '03-31-2019')
mask_2_2019 = (df_3658_wind['dateC'] > '04-01-2019') & (df_3658_wind['dateC'] <= '06-30-2019')
mask_3_2019 = (df_3658_wind['dateC'] > '06-01-2019') & (df_3658_wind['dateC'] <= '08-30-2019')
mask_4_2019 = (df_3658_wind['dateC'] > '09-01-2019') & (df_3658_wind['dateC'] <= '12-31-2019')


qrt1_3658_2019 = df_3658_wind.loc[mask_1_2019]
qrt2_3658_2019 = df_3658_wind.loc[mask_2_2019]
qrt3_3658_2019 = df_3658_wind.loc[mask_3_2019]
qrt4_3658_2019 = df_3658_wind.loc[mask_4_2019]


mask_1_2020 = (df_3658_wind['dateC'] > '01-01-2020') & (df_3658_wind['dateC'] <= '03-31-2020')
mask_2_2020 = (df_3658_wind['dateC'] > '04-01-2020') & (df_3658_wind['dateC'] <= '06-30-2020')
mask_3_2020 = (df_3658_wind['dateC'] > '06-01-2020') & (df_3658_wind['dateC'] <= '08-30-2020')
mask_4_2020 = (df_3658_wind['dateC'] > '09-01-2020') & (df_3658_wind['dateC'] <= '12-31-2020')

qrt1_3658_2020 = df_3658_wind.loc[mask_1_2020]
qrt2_3658_2020 = df_3658_wind.loc[mask_2_2020]
qrt3_3658_2020 = df_3658_wind.loc[mask_3_2020]
qrt4_3658_2020 = df_3658_wind.loc[mask_4_2020]

# 2019 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.17, 1, 'Lancaster-43301 Division Street Monitoring Station - LA County', fontsize=24)
fig.suptitle('2019 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_3658_2019['wd'], qrt1_3658_2019['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_3658_2019['wd'], qrt2_3658_2019['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_3658_2019['wd'], qrt3_3658_2019['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_3658_2019['wd'], qrt4_3658_2019['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Lancaster-43301_Division_Street_2019_wind.png',dpi=300, bbox_inches = "tight")


# 2020 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.17, 1, 'Lancaster-43301 Division Street Monitoring Station - LA County', fontsize=24)
fig.suptitle('2020 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_3658_2020['wd'], qrt1_3658_2020['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_3658_2020['wd'], qrt2_3658_2020['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_3658_2020['wd'], qrt3_3658_2020['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_3658_2020['wd'], qrt4_3658_2020['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Lancaster-43301_Division_Street_2020_wind.png',dpi=300, bbox_inches = "tight")

# Create wind roses for Los Angeles-North Main Street

df_2899_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2899_Wind_dataset.csv')
df_2899_wind.drop(df_2899_wind.columns[[0]], axis=1, inplace=True)
df_2899_wind["dateC"] = pd.to_datetime(df_2899_wind["dateC"])
df_2899_wind = df_2899_wind.sort_values(by=['dateC'])


df_2899_wind['wd'] = df_2899_wind.wd.astype(float)
df_2899_wind['ws'] = df_2899_wind.ws.astype(float)
ws = df_2899_wind["ws"] 
wd = df_2899_wind["wd"]


# seperate into quarters by year
mask_1_2019 = (df_2899_wind['dateC'] > '01-01-2019') & (df_2899_wind['dateC'] <= '03-31-2019')
mask_2_2019 = (df_2899_wind['dateC'] > '04-01-2019') & (df_2899_wind['dateC'] <= '06-30-2019')
mask_3_2019 = (df_2899_wind['dateC'] > '06-01-2019') & (df_2899_wind['dateC'] <= '08-30-2019')
mask_4_2019 = (df_2899_wind['dateC'] > '09-01-2019') & (df_2899_wind['dateC'] <= '12-31-2019')


qrt1_2899_2019 = df_2899_wind.loc[mask_1_2019]
qrt2_2899_2019 = df_2899_wind.loc[mask_2_2019]
qrt3_2899_2019 = df_2899_wind.loc[mask_3_2019]
qrt4_2899_2019 = df_2899_wind.loc[mask_4_2019]


mask_1_2020 = (df_2899_wind['dateC'] > '01-01-2020') & (df_2899_wind['dateC'] <= '03-31-2020')
mask_2_2020 = (df_2899_wind['dateC'] > '04-01-2020') & (df_2899_wind['dateC'] <= '06-30-2020')
mask_3_2020 = (df_2899_wind['dateC'] > '06-01-2020') & (df_2899_wind['dateC'] <= '08-30-2020')
mask_4_2020 = (df_2899_wind['dateC'] > '09-01-2020') & (df_2899_wind['dateC'] <= '12-31-2020')

qrt1_2899_2020 = df_2899_wind.loc[mask_1_2020]
qrt2_2899_2020 = df_2899_wind.loc[mask_2_2020]
qrt3_2899_2020 = df_2899_wind.loc[mask_3_2020]
qrt4_2899_2020 = df_2899_wind.loc[mask_4_2020]

# 2019 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.20, 1, 'Los Angeles-North Main Street Monitoring Station - LA County', fontsize=24)
fig.suptitle('2019 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2899_2019['wd'], qrt1_2899_2019['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2899_2019['wd'], qrt2_2899_2019['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2899_2019['wd'], qrt3_2899_2019['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2899_2019['wd'], qrt4_2899_2019['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Los Angeles-North Main Street_2019_wind.png',dpi=300, bbox_inches = "tight")


# 2020 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.20, 1, 'Los Angeles-North Main Street Monitoring Station - LA County', fontsize=24)
fig.suptitle('2020 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2899_2020['wd'], qrt1_2899_2020['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2899_2020['wd'], qrt2_2899_2020['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2899_2020['wd'], qrt3_2899_2020['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2899_2020['wd'], qrt4_2899_2020['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Los Angeles-North Main Street_2020_wind.png',dpi=300, bbox_inches = "tight")

# Create wind roses for Clovis-N Villa Avenue

df_3026_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_3026_Wind_dataset.csv')
df_3026_wind.drop(df_3026_wind.columns[[0]], axis=1, inplace=True)
df_3026_wind["dateC"] = pd.to_datetime(df_3026_wind["dateC"])
df_3026_wind = df_3026_wind.sort_values(by=['dateC'])


df_3026_wind['wd'] = df_3026_wind.wd.astype(float)
df_3026_wind['ws'] = df_3026_wind.ws.astype(float)
ws = df_3026_wind["ws"] 
wd = df_3026_wind["wd"]


# seperate into quarters by year
mask_1_2019 = (df_3026_wind['dateC'] > '01-01-2019') & (df_3026_wind['dateC'] <= '03-31-2019')
mask_2_2019 = (df_3026_wind['dateC'] > '04-01-2019') & (df_3026_wind['dateC'] <= '06-30-2019')
mask_3_2019 = (df_3026_wind['dateC'] > '06-01-2019') & (df_3026_wind['dateC'] <= '08-30-2019')
mask_4_2019 = (df_3026_wind['dateC'] > '09-01-2019') & (df_3026_wind['dateC'] <= '12-31-2019')


qrt1_3026_2019 = df_3026_wind.loc[mask_1_2019]
qrt2_3026_2019 = df_3026_wind.loc[mask_2_2019]
qrt3_3026_2019 = df_3026_wind.loc[mask_3_2019]
qrt4_3026_2019 = df_3026_wind.loc[mask_4_2019]


mask_1_2020 = (df_3026_wind['dateC'] > '01-01-2020') & (df_3026_wind['dateC'] <= '03-31-2020')
mask_2_2020 = (df_3026_wind['dateC'] > '04-01-2020') & (df_3026_wind['dateC'] <= '06-30-2020')
mask_3_2020 = (df_3026_wind['dateC'] > '06-01-2020') & (df_3026_wind['dateC'] <= '08-30-2020')
mask_4_2020 = (df_3026_wind['dateC'] > '09-01-2020') & (df_3026_wind['dateC'] <= '12-31-2020')

qrt1_3026_2020 = df_3026_wind.loc[mask_1_2020]
qrt2_3026_2020 = df_3026_wind.loc[mask_2_2020]
qrt3_3026_2020 = df_3026_wind.loc[mask_3_2020]
qrt4_3026_2020 = df_3026_wind.loc[mask_4_2020]

# 2019 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.22, 1, 'Clovis-N Villa Avenue Monitoring Station - Fresno County', fontsize=24)
fig.suptitle('2019 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_3026_2019['wd'], qrt1_3026_2019['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_3026_2019['wd'], qrt2_3026_2019['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_3026_2019['wd'], qrt3_3026_2019['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_3026_2019['wd'], qrt4_3026_2019['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Clovis-N Villa Avenue-Fresno County_2019_wind.png',dpi=300, bbox_inches = "tight")


# 2020 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.22, 1, 'Clovis-N Villa Avenue Monitoring Station - Fresno County', fontsize=24)
fig.suptitle('2020 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_3026_2020['wd'], qrt1_3026_2020['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_3026_2020['wd'], qrt2_3026_2020['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_3026_2020['wd'], qrt3_3026_2020['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_3026_2020['wd'], qrt4_3026_2020['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Clovis-N Villa Avenue-Fresno County_2020_wind.png',dpi=300, bbox_inches = "tight")

# Create wind roses for Paso Robles-Santa Fe Avenue

df_2955_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2955_Wind_dataset.csv')
df_2955_wind.drop(df_2955_wind.columns[[0]], axis=1, inplace=True)
df_2955_wind["dateC"] = pd.to_datetime(df_2955_wind["dateC"])
df_2955_wind = df_2955_wind.sort_values(by=['dateC'])


df_2955_wind['wd'] = df_2955_wind.wd.astype(float)
df_2955_wind['ws'] = df_2955_wind.ws.astype(float)
ws = df_2955_wind["ws"] 
wd = df_2955_wind["wd"]


# seperate into quarters by year
mask_1_2019 = (df_2955_wind['dateC'] > '01-01-2019') & (df_2955_wind['dateC'] <= '03-31-2019')
mask_2_2019 = (df_2955_wind['dateC'] > '04-01-2019') & (df_2955_wind['dateC'] <= '06-30-2019')
mask_3_2019 = (df_2955_wind['dateC'] > '06-01-2019') & (df_2955_wind['dateC'] <= '08-30-2019')
mask_4_2019 = (df_2955_wind['dateC'] > '09-01-2019') & (df_2955_wind['dateC'] <= '12-31-2019')


qrt1_2955_2019 = df_2955_wind.loc[mask_1_2019]
qrt2_2955_2019 = df_2955_wind.loc[mask_2_2019]
qrt3_2955_2019 = df_2955_wind.loc[mask_3_2019]
qrt4_2955_2019 = df_2955_wind.loc[mask_4_2019]


mask_1_2020 = (df_2955_wind['dateC'] > '01-01-2020') & (df_2955_wind['dateC'] <= '03-31-2020')
mask_2_2020 = (df_2955_wind['dateC'] > '04-01-2020') & (df_2955_wind['dateC'] <= '06-30-2020')
mask_3_2020 = (df_2955_wind['dateC'] > '06-01-2020') & (df_2955_wind['dateC'] <= '08-30-2020')
mask_4_2020 = (df_2955_wind['dateC'] > '09-01-2020') & (df_2955_wind['dateC'] <= '12-31-2020')

qrt1_2955_2020 = df_2955_wind.loc[mask_1_2020]
qrt2_2955_2020 = df_2955_wind.loc[mask_2_2020]
qrt3_2955_2020 = df_2955_wind.loc[mask_3_2020]
qrt4_2955_2020 = df_2955_wind.loc[mask_4_2020]

# 2019 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.1, 1, 'Paso Robles-Santa Fe Avenue Monitoring Station - San Luis Obispo County', fontsize=24)
fig.suptitle('2019 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2955_2019['wd'], qrt1_2955_2019['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2955_2019['wd'], qrt2_2955_2019['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2955_2019['wd'], qrt3_2955_2019['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2955_2019['wd'], qrt4_2955_2019['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Paso Robles-Santa Fe Avenue_2019_wind.png',dpi=300, bbox_inches = "tight")


# 2020 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.1, 1, 'Paso Robles-Santa Fe Avenue Monitoring Station - San Luis Obispo County', fontsize=24)
fig.suptitle('2020 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2955_2020['wd'], qrt1_2955_2020['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2955_2020['wd'], qrt2_2955_2020['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2955_2020['wd'], qrt3_2955_2020['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2955_2020['wd'], qrt4_2955_2020['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Paso Robles-Santa Fe Avenue_2020_wind.png',dpi=300, bbox_inches = "tight")

# Create wind roses for Roseville-N Sunrise Blvd

df_2956_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2956_Wind_dataset.csv')
df_2956_wind.drop(df_2956_wind.columns[[0]], axis=1, inplace=True)
df_2956_wind["dateC"] = pd.to_datetime(df_2956_wind["dateC"])
df_2956_wind = df_2956_wind.sort_values(by=['dateC'])


df_2956_wind['wd'] = df_2956_wind.wd.astype(float)
df_2956_wind['ws'] = df_2956_wind.ws.astype(float)
ws = df_2956_wind["ws"] 
wd = df_2956_wind["wd"]


# seperate into quarters by year
mask_1_2019 = (df_2956_wind['dateC'] > '01-01-2019') & (df_2956_wind['dateC'] <= '03-31-2019')
mask_2_2019 = (df_2956_wind['dateC'] > '04-01-2019') & (df_2956_wind['dateC'] <= '06-30-2019')
mask_3_2019 = (df_2956_wind['dateC'] > '06-01-2019') & (df_2956_wind['dateC'] <= '08-30-2019')
mask_4_2019 = (df_2956_wind['dateC'] > '09-01-2019') & (df_2956_wind['dateC'] <= '12-31-2019')


qrt1_2956_2019 = df_2956_wind.loc[mask_1_2019]
qrt2_2956_2019 = df_2956_wind.loc[mask_2_2019]
qrt3_2956_2019 = df_2956_wind.loc[mask_3_2019]
qrt4_2956_2019 = df_2956_wind.loc[mask_4_2019]


mask_1_2020 = (df_2956_wind['dateC'] > '01-01-2020') & (df_2956_wind['dateC'] <= '03-31-2020')
mask_2_2020 = (df_2956_wind['dateC'] > '04-01-2020') & (df_2956_wind['dateC'] <= '06-30-2020')
mask_3_2020 = (df_2956_wind['dateC'] > '06-01-2020') & (df_2956_wind['dateC'] <= '08-30-2020')
mask_4_2020 = (df_2956_wind['dateC'] > '09-01-2020') & (df_2956_wind['dateC'] <= '12-31-2020')

qrt1_2956_2020 = df_2956_wind.loc[mask_1_2020]
qrt2_2956_2020 = df_2956_wind.loc[mask_2_2020]
qrt3_2956_2020 = df_2956_wind.loc[mask_3_2020]
qrt4_2956_2020 = df_2956_wind.loc[mask_4_2020]

# 2019 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.20, 1, 'Roseville-N Sunrise Blvd Monitoring Station - Placer County', fontsize=24)
fig.suptitle('2019 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2956_2019['wd'], qrt1_2956_2019['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2956_2019['wd'], qrt2_2956_2019['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2956_2019['wd'], qrt3_2956_2019['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2956_2019['wd'], qrt4_2956_2019['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Roseville-N Sunrise Blvd_2019_wind.png',dpi=300, bbox_inches = "tight")


# 2020 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.20, 1, 'Roseville-N Sunrise Blvd Monitoring Station - Placer County', fontsize=24)
fig.suptitle('2020 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2956_2020['wd'], qrt1_2956_2020['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2956_2020['wd'], qrt2_2956_2020['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2956_2020['wd'], qrt3_2956_2020['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2956_2020['wd'], qrt4_2956_2020['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Roseville-N Sunrise Blvd_2020_wind.png',dpi=300, bbox_inches = "tight")

# Create wind roses for South Lake Tahoe-Sandy Way

df_2948_wind = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2948_Wind_dataset.csv')
df_2948_wind.drop(df_2948_wind.columns[[0]], axis=1, inplace=True)
df_2948_wind["dateC"] = pd.to_datetime(df_2948_wind["dateC"])
df_2948_wind = df_2948_wind.sort_values(by=['dateC'])


df_2948_wind['wd'] = df_2948_wind.wd.astype(float)
df_2948_wind['ws'] = df_2948_wind.ws.astype(float)
ws = df_2948_wind["ws"] 
wd = df_2948_wind["wd"]


# seperate into quarters by year
mask_1_2019 = (df_2948_wind['dateC'] > '01-01-2019') & (df_2948_wind['dateC'] <= '03-31-2019')
mask_2_2019 = (df_2948_wind['dateC'] > '04-01-2019') & (df_2948_wind['dateC'] <= '06-30-2019')
mask_3_2019 = (df_2948_wind['dateC'] > '06-01-2019') & (df_2948_wind['dateC'] <= '08-30-2019')
mask_4_2019 = (df_2948_wind['dateC'] > '09-01-2019') & (df_2948_wind['dateC'] <= '12-31-2019')


qrt1_2948_2019 = df_2948_wind.loc[mask_1_2019]
qrt2_2948_2019 = df_2948_wind.loc[mask_2_2019]
qrt3_2948_2019 = df_2948_wind.loc[mask_3_2019]
qrt4_2948_2019 = df_2948_wind.loc[mask_4_2019]


mask_1_2020 = (df_2948_wind['dateC'] > '01-01-2020') & (df_2948_wind['dateC'] <= '03-31-2020')
mask_2_2020 = (df_2948_wind['dateC'] > '04-01-2020') & (df_2948_wind['dateC'] <= '06-30-2020')
mask_3_2020 = (df_2948_wind['dateC'] > '06-01-2020') & (df_2948_wind['dateC'] <= '08-30-2020')
mask_4_2020 = (df_2948_wind['dateC'] > '09-01-2020') & (df_2948_wind['dateC'] <= '12-31-2020')

qrt1_2948_2020 = df_2948_wind.loc[mask_1_2020]
qrt2_2948_2020 = df_2948_wind.loc[mask_2_2020]
qrt3_2948_2020 = df_2948_wind.loc[mask_3_2020]
qrt4_2948_2020 = df_2948_wind.loc[mask_4_2020]

# 2019 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.1, 1, 'South Lake Tahoe-Sandy Way Monitoring Station - El Dorado County', fontsize=24)
fig.suptitle('2019 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2948_2019['wd'], qrt1_2948_2019['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2948_2019['wd'], qrt2_2948_2019['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2948_2019['wd'], qrt3_2948_2019['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2948_2019['wd'], qrt4_2948_2019['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/outh Lake Tahoe-Sandy Way_2019_wind.png',dpi=300, bbox_inches = "tight")


# 2020 plots
fig = plt.figure(figsize=(15,15))
fig.text(0.1, 1, 'South Lake Tahoe-Sandy Way Monitoring Station - El Dorado County', fontsize=24)
fig.suptitle('2020 by Quarter', fontsize=20)

#rect=[4,4,4,4] 
ax1 = fig.add_subplot(221, projection="windrose")
ax1.set_title('First Quarter', fontsize=18)
ax1.bar(qrt1_2948_2020['wd'], qrt1_2948_2020['ws'], normed=True, bins=8) 
ax1.set_radii_angle()
ax1.set_legend(bbox_to_anchor=(0.95 , -0.2), title="Wind Speed", units="MPH")

ax2 = fig.add_subplot(222, projection="windrose")
ax2.set_title('Second Quarter', fontsize=18)
ax2.bar(qrt2_2948_2020['wd'], qrt2_2948_2020['ws'],normed=True, bins=8) 
ax2.set_radii_angle()

ax3 = fig.add_subplot(223, projection="windrose")
ax3.set_title('Third Quarter', fontsize=18)
ax3.bar(qrt3_2948_2020['wd'], qrt3_2948_2020['ws'],normed=True, bins=8) 
ax3.set_radii_angle()

ax4 = fig.add_subplot(224, projection="windrose")
ax4.set_title('Fourth Quarter', fontsize=18)
ax4.bar(qrt4_2948_2020['wd'], qrt4_2948_2020['ws'],normed=True, bins=8) 
ax4.set_radii_angle()
#plt.show()
plt.savefig('/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/Routh Lake Tahoe-Sandy Way_2020_wind.png',dpi=300, bbox_inches = "tight")