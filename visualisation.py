# 1-Graph in GUI
# 2-Linking data to graphs
# 3-Refreshing graphs
import tkinter as tk
from pandas import DataFrame
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
from sqlite3 import Error
import datetime as dt

try:
    con = sqlite3.connect("./IoT_DataBase.db")
except Error as e:
    print(e)

# Load the data into a DataFrame
temp_df = pd.read_sql_query("SELECT * from Temperature_Data", con)
humy_df = pd.read_sql_query("SELECT * from Humidity_Data", con)
accel_df = pd.read_sql_query("SELECT * from Acceleration_Data", con,parse_dates=False)

# print(temp_df.columns)
df01 = DataFrame(temp_df,columns=['Temperature','TemperatureLevel'])

df02 = DataFrame(humy_df,columns=['Humidity','HumidityLevel'])

df03 = DataFrame(accel_df,columns=['Date_Time','accX','accY','accZ'])

# print(type(df02[['HumidityLevel','Humidity']].groupby('HumidityLevel').sum()))
fig2 = df02[['HumidityLevel','Humidity']].groupby('HumidityLevel').mean().to_dict()
print(fig2)
# print(fig2['Humidity'].keys())

# fig3 = df03.groupby(df03['Date_Time'].dt.date)
# print(pd.to_datetime(df03['Date_Time']))

root= tk.Tk() 
root.wm_iconbitmap('Royal-sun.ico')
root.wm_title('IoT Sensors')

figure1 = plt.Figure(figsize=(5,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT)
df01 = df01[['Temperature','TemperatureLevel']].groupby('TemperatureLevel').mean()
df01.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Average of temperature')

figure2 = plt.Figure(figsize=(5,5), dpi=100) 
subplot2 = figure2.add_subplot(111) 
labels2 = fig2['Humidity'].keys() 
pieSizes = fig2['Humidity'].values()
my_colors2 = ["#48f3db", "#51c4e9", "#6150c1"]
explode2 = (0.1, 0.1, 0.1)  
subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) 
subplot2.axis('equal')  
subplot2.set_title('Pie Chart of Humidity')
pie2 = FigureCanvasTkAgg(figure2, root)
pie2.get_tk_widget().pack(side=tk.RIGHT)

# fig3 = df03.to_dict()
# # fig3['accX'].values()
# print(df03)
# print(np.average(list(fig3['accX'].values())))
# print(np.average(list(fig3['accY'].values())))
# print(np.average(list(fig3['accZ'].values())))

# figure3 = plt.Figure(figsize=(5,4), dpi=100)
# ax3 = figure3.add_subplot(111)
# ax3.scatter(df03['accX','accY','accZ'], color = 'g')
# scatter3 = FigureCanvasTkAgg(figure3, root) 
# scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# ax3.legend(['Stock_Index_Price']) 
# ax3.set_xlabel('Interest Rate')
# ax3.set_title(' Accelator Values ')

root.mainloop()
