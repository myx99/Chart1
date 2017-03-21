from WindPy import *
import pandas as pd
import matplotlib.pyplot as plt
from Utilities.DB_query_NAV import Query_NAV
from data_analysis.DB_query import db_query
import numpy as np


def average_increase(product_id, startdate, enddate):
    # get nav increase data by day
    # df = Query_NAV(product_id, startdate, enddate)
    df = db_query(product_id, startdate, enddate, "nav_increase")
    # print(df.dtypes)  # DEBUG

    df['NAV_Increase'] = df['NAV_Increase'].astype(float)
    ave = df['NAV_Increase'].mean()

    return "%.4f" % ave


# test main
# an = annualized_return('GZFB0001', '2017-01-18', '2017-02-28')
# print(an)
