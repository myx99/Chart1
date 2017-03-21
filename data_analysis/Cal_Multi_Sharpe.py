import matplotlib.pyplot as plt
import pandas as pd
from WindPy import *

from data_analysis.Sharpe_Ratio import Cal_Sharpe

# set date
startdate = '2017-01-19'
enddate = '2017-02-28'

# get date list
w.start()
date_list = w.tdays(startdate, enddate, "").Times
w.close()
# print(date_list)

# format date list
dates = []
for i in date_list:
    dates.append(i.isoformat()[:10])
# print(dates)
date_count = dates.__len__()

# get sharpe list
sharpes_eq = []
sharpes_zb = []
date_x = []
for i in range(3, date_count+1):
    x = '%s' % dates[i-1]
    # print(x)
    date_x.append(x)
    s_eq = Cal_Sharpe('GZFB0001', startdate, x, "EQ")
    s_zb = Cal_Sharpe('GZFB0001', startdate, x, "ZB")
    sharpes_eq.append(s_eq)
    sharpes_zb.append(s_zb)
# print(sharpes)

# create dateframe
df = pd.DataFrame()
# df['Date'] = pd.Series(dates[2:])
df['Date'] = pd.Series(date_x)
df['Date'] = df['Date'].astype(date)

column_name1 = 'Sharpe_Rf_is_10Ybond_return'
column_name2 = 'Sharpe_Rf_is_0'

df[column_name1] = pd.Series(sharpes_eq)
df[column_name2] = pd.Series(sharpes_zb)
df[column_name1] = df[column_name1].astype(float)
df[column_name2] = df[column_name2].astype(float)
# print(df)

df = df.set_index('Date')
df.plot()
plt.show()
