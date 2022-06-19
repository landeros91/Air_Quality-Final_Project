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

#PM10 data monitoring location # 2849
df_2849_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2849_PM_dataset.csv')
df_2849_PM.drop(df_2849_PM.columns[[0]], axis=1, inplace=True)
df_2849_PM["dataC"] = pd.to_datetime(df_2849_PM["dateC"])
df_2849_PM = df_2849_PM.sort_values(by=['dateC'])


#df_2849_PM.plot(kind="scatter", x='dateC', y="value", linestyle='solid', figsize=(15,10))
df_2849_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - LA County - Glendora-Laurel Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/PM10_2849.png")

#PM10 data monitoring location # 2948
df_2948_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2948_PM_dataset.csv')
df_2948_PM.drop(df_2948_PM.columns[[0]], axis=1, inplace=True)
df_2948_PM["dataC"] = pd.to_datetime(df_2948_PM["dateC"])
df_2948_PM = df_2948_PM.sort_values(by=['dateC'])


#df_2948_PM.plot(kind="scatter", x='dateC', y="value", linestyle='solid', figsize=(15,10))
df_2948_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - El Dorado County - South Lake Tahoe-Sandy Way Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/PM10_2948.png")

#PM10 data monitoring location # 2955
df_2955_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2955_PM_dataset.csv')
df_2955_PM.drop(df_2955_PM.columns[[0]], axis=1, inplace=True)
df_2955_PM["dataC"] = pd.to_datetime(df_2955_PM["dateC"])
df_2955_PM = df_2955_PM.sort_values(by=['dateC'])

#df_2955_PM.plot(kind="scatter", x='dateC', y="value", linestyle='solid', figsize=(15,10))
df_2955_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - San Luis Obispo County - Paso Robles-Santa Fe Avenue Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/PM10_2955.png")

#PM10 data monitoring location # 2956
df_2956_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_2956_PM_dataset.csv')
df_2956_PM.drop(df_2956_PM.columns[[0]], axis=1, inplace=True)
df_2956_PM["dataC"] = pd.to_datetime(df_2956_PM["dateC"])
df_2956_PM = df_2956_PM.sort_values(by=['dateC'])

#df_2956_PM.plot(kind="scatter", x='dateC', y="value", linestyle='solid', figsize=(15,10))
df_2956_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - Placer County - Roseville-N Sunrise Blvd Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/PM10_2956.png")

#PM10 data monitoring location # 3011
df_3011_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_3011_PM_dataset.csv')
df_3011_PM.drop(df_3011_PM.columns[[0]], axis=1, inplace=True)
df_3011_PM["dataC"] = pd.to_datetime(df_3011_PM["dateC"])
df_3011_PM = df_3011_PM.sort_values(by=['dateC'])

#df_3011_PM.plot(kind="scatter", x='dateC', y="value", linestyle='solid', figsize=(15,10))
df_3011_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - Sacramento County - Sacramento-T Street Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/PM10_3011.png")

#PM10 data monitoring location # 3026
df_3026_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_3026_PM_dataset.csv')
df_3026_PM.drop(df_3026_PM.columns[[0]], axis=1, inplace=True)
df_3026_PM["dataC"] = pd.to_datetime(df_3026_PM["dateC"])
df_3026_PM = df_3026_PM.sort_values(by=['dateC'])

#df_3026_PM.plot(kind="scatter", x='dateC', y="value", linestyle='solid', figsize=(15,10))
df_3026_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - Fresno County - Clovis-N Villa Avenue Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/PM10_3026.png")

#PM10 data monitoring location # 3154
df_3154_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_3154_PM_dataset.csv')
df_3154_PM.drop(df_3154_PM.columns[[0]], axis=1, inplace=True)
df_3154_PM["dataC"] = pd.to_datetime(df_3154_PM["dateC"])
df_3154_PM = df_3154_PM.sort_values(by=['dateC'])

#df_3154_PM.plot(kind="scatter", x='dateC', y="value", linestyle='solid', figsize=(15,10))
df_3154_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - Inyo County - Keeler-Cerro Gordo Road Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/PM10_3154.png")

#PM10 data monitoring location # 3658
df_3658_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_3658_PM_dataset.csv')
df_3658_PM.drop(df_3658_PM.columns[[0]], axis=1, inplace=True)
df_3658_PM["dataC"] = pd.to_datetime(df_3658_PM["dateC"])
df_3658_PM = df_3658_PM.sort_values(by=['dateC'])

#df_3658_PM.plot(kind="scatter", x='dateC', y="value", linestyle='solid', figsize=(15,10))
df_3658_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - LA County - Lancaster-43301 Division Street Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/PM10_3658.png")

#PM10 data monitoring location # 3762
df_3762_PM = pd.read_csv(r'//Users/robertvanderweele/git/Air_Quality-Final_Project/Cleaned_data/Site_3762_PM_dataset.csv')
df_3762_PM.drop(df_3762_PM.columns[[0]], axis=1, inplace=True)
df_3762_PM["dataC"] = pd.to_datetime(df_3762_PM["dateC"])
df_3762_PM = df_3762_PM.sort_values(by=['dateC'])

#df_3762_PM.plot(kind="scatter", x='dateC', y="value", linestyle='solid', figsize=(15,10))
df_3762_PM.plot(x='dateC', y="value", linestyle='-', marker='o', figsize=(15,10))
plt.ylabel("PM10 - ug/m3",fontsize=12, fontweight="bold")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.title("PM10 Data - San Luis Obispo County - Arroyo Grande-2391 Willow Road Monitoring Station",fontsize=18, fontweight="bold")
lgnd = plt.legend(title_fontsize='11', mode="Expanded",
         scatterpoints=1, loc="best", title="PM10")
plt.tight_layout()
plt.legend
plt.savefig("/Users/robertvanderweele/git/Air_Quality-Final_Project/Plots/PM10_3762.png")