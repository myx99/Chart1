from WindPy import *
import pandas as pd
import matplotlib.pyplot as plt
from Utilities.DB_query_NAV import Query_NAV
from data_analysis.DB_query import db_query
import numpy as np


def cal_beta(product_id, startdate, enddate):
    # get nav increase data by day
    # df = Query_NAV(product_id, startdate, enddate)
    df = db_query(product_id, startdate, enddate, "nav_increase")
    # print(df.dtypes)  # DEBUG

    if startdate == enddate:
        df['NAV_Increase']

    df['NAV_Increase'] = df['NAV_Increase'].astype(float)

    df.replace('Nan', 0)

    w.start()
    bmk_wind_data1 = w.wsd("M1001654", "close", startdate, enddate, "Fill=Previous")
    w.close()
    df['Benchmark'] = bmk_wind_data1.Data[0]
    df['Benchmark'] = df['Benchmark'].astype(float)

    bt = df['NAV_Increase'].cov(df['Benchmark']) / df['Benchmark'].var()

    return "%.4f" % bt


# test main
# result = cal_beta('GZFB0001', '2017-01-18', '2017-01-19')
# print(result)
