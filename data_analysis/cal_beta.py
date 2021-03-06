from WindPy import *
import pandas as pd
import matplotlib.pyplot as plt
from Utilities.DB_query_NAV import Query_NAV
from data_analysis.DB_query import db_query
import numpy as np


def cal_beta(product_id, startdate, enddate):
    # get nav increase data by day
    df = db_query(product_id, startdate, enddate, "nav_increase")

    df['Date'] = df['Date'].astype(str)
    df['NAV_Increase'] = df['NAV_Increase'].astype(float)

    w.start()
    bmk_wind_data1 = w.wsd("M1001654", "close", startdate, enddate, "Fill=Previous")
    w.close()
    date_raw = bmk_wind_data1.Times
    date_count = bmk_wind_data1.Times.__len__()
    index_dates = []
    for i in range(date_count):
        date_format = str(date_raw[i])[:10]
        index_dates.append(date_format)

    df_bm = pd.DataFrame()
    df_bm['Date'] = index_dates
    df_bm['Benchmark'] = bmk_wind_data1.Data[0]
    df_bm['Benchmark'] = df_bm['Benchmark'].astype(float)

    df_temp = pd.merge(df_bm, df, how='left', on='Date')
    # df_temp = df_temp.fillna(0)

    bt = df_temp['NAV_Increase'].cov(df_temp['Benchmark']) / df_temp['Benchmark'].var()

    return "%.4f" % bt

# test main
# result = cal_beta('GZFB0001', '2017-01-18', '2017-01-19')
# print(result)
