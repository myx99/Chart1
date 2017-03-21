from WindPy import *
import pandas as pd
import matplotlib.pyplot as plt
from Utilities.Query_data_from_MySQL import Query_MySQL
from data_analysis.DB_query import db_query

import numpy as np


def Cal_Sharpe(product_id, startdate, enddate, product_type=None):
    # get nav increase data by day
    # df = Query_MySQL(product_id, startdate, enddate)
    df = db_query(product_id, startdate, enddate, "nav_increase")
    # print(df.dtypes)  # DEBUG

    # format data, column 1 = Date, Column 2 = NAV_Increase
    df['NAV_Increase'] = df['NAV_Increase'].astype(float)
    df['Date'] = df['Date'].astype(date)

    # for plot use
    # df_index = df.set_index('Date')
    # df_index['NAV_Increase'].plot()
    # plt.show()   # display plot

    # calculate mean and std
    nav_mean_daily = df['NAV_Increase'].mean()
    nav_std_daily = df['NAV_Increase'].std()

    # use different benchmark rate for different types of products
    if product_type == "EQ":
        benchmark_stock = "M1001654"
    elif product_type == "FI":
        benchmark_stock = "M1001648"
    elif product_type is None:
        # print("No designated product type, will set as Equity product....")
        benchmark_stock = "M1001654"
    else:
        # print("Unsupported product type, will set as Equity product....")
        benchmark_stock = "M1001654"
    bmr_daily = Cal_Benchmark_Rate(benchmark_stock, startdate, enddate)
    if product_type == "ZB":
        bmr_daily = 0
    sharpe_value = sharpe_formula(nav_mean_daily, nav_std_daily, bmr_daily)
    # print(sharpe_value)  # DEBUG
    return sharpe_value


# get return rate as benchmark(non-risk) return rate
def Cal_Benchmark_Rate(bond, startdate, enddate):
    w.start()
    data = w.wsd(bond, "close", startdate, enddate, "Fill=Previous")
    # print(data)  # DEBUG
    brr = data.Data[0]
    brr_yearly = np.mean(brr)
    brr_daily = brr_yearly / 360
    w.close
    # print(brr)  # DEBUG
    # print(brr_yearly, brr_daily)  # DEBUG
    return brr_daily


# formula to calculate sharpe value
def sharpe_formula(mean_value, std_value, bmr):
    # if std_value == 0:
    #     return 100
    return ((mean_value - bmr) / std_value) * np.sqrt(250)


# test main
# x = Cal_Sharpe('GZFB0001', '2017-01-19', '2017-02-28')
# print(x)
