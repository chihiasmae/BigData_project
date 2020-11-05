import tkinter as tk
from pandas import DataFrame
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
from sqlite3 import Error
import datetime as dt
import time
from threading import Timer

try:
    con = sqlite3.connect("./IoT_DataBase.db")
except Error as e:
    print(e)

# Load the data into a DataFrame
temp_df = pd.read_sql_query("SELECT * from Temperature_Data", con)
humy_df = pd.read_sql_query("SELECT * from Humidity_Data", con)
accel_df = pd.read_sql_query("SELECT * from Acceleration_Data", con,parse_dates=False)

# data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
#          'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
#         }
df03 = DataFrame(accel_df,columns=['Date_Time','accX','accY','accZ'])        
#df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])
print(df03)

#df03 = df03[['Date_Time','accX']].groupby('Date_Time').mean().to_dict()

#print(df2)

root= tk.Tk() 
figure2 = plt.Figure(figsize=(5,5), dpi=100)
ax2 = figure2.add_subplot(111)
my_colors2 = ["#48f3db", "#51c4e9", "#6150c1"]
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df03 = df03[['Date_Time','accX','accY','accZ']].groupby('Date_Time').sum()
#df03.plot(kind='line', legend=True, ax=ax2, color=my_colors2,marker='o', fontsize=10)

t = Timer(5.0, df03.plot(kind='line', legend=True, ax=ax2, color=my_colors2,marker='o', fontsize=10))
t.start()

plt.plot( 'x', 'y1', data=df03, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.legend()
print( range(1,11))
#plt.show()
ax2.set_title('Year Vs. Unemployment Rate')






root.mainloop()