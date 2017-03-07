from WindPy import *
import pandas as pd
import matplotlib.pyplot as plt
from Utilities.Query_data_from_MySQL import Query_MySQL
import numpy as np


# get 10Y T-bond return as benchmark(non-risk) return rate
w.start()
data = w.wsd("M1001654", "close", "2017-01-19", "2017-02-27", "Fill=Previous")
# print(data)  # DEBUG
brr = data.Data[0]
brr_yearly = np.mean(brr)
w.close

# get nav increase data by day
fund = 'GZFB0001'
df = Query_MySQL(fund)
# print(df.dtypes)  # DEBUG

# format data
df['NAV_Increase'] = df['NAV_Increase'].astype(float)
df['Date'] = df['Date'].astype(date)
df_index = df.set_index('Date')
df_index['NAV_Increase'].plot()
# plt.show()   # display plot

# calculate sharpe (without using benchmark return)
nav_mean_daily = df['NAV_Increase'].mean()
nav_std_daily = df['NAV_Increase'].std()
sharpe  = (nav_mean_daily / nav_std_daily) * np.sqrt(250)
print(sharpe)

# calculate VaR
