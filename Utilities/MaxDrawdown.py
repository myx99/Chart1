from WindPy import *
import pandas as pd
import matplotlib.pyplot as plt
from Utilities.DB_query_NAV import Query_NAV
import numpy as np


def Cal_MaxDrawdown(product_id, startdate, enddate):
    # get nav increase data by day
    df = Query_NAV(product_id, startdate, enddate)
    # print(df.dtypes)  # DEBUG

    df['NAV'] = df['NAV'].astype(float)
    df['Date'] = df['Date'].astype(date)

    df['max2here'] = pd.expanding_max(df['NAV'])
    df['dd2here'] = df['NAV'] / df['max2here'] - 1

    # print(df)

    temp = df.sort_values(by='dd2here').iloc[0][['Date', 'dd2here']]
    max_dd = temp['dd2here']
    end_date = temp['Date']

    df2 = df[df['Date'] <= end_date]
    start_date = df2.sort_values(by='NAV', ascending=False).iloc[0]['Date']

    print("MaxDrawdown : %f,  Start from : %s,  End at : %s" % (max_dd, start_date, end_date))

# test main
Cal_MaxDrawdown('GZFB0001', '2017-01-18', '2017-02-28')
