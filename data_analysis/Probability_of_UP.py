from WindPy import *
import pandas as pd
import matplotlib.pyplot as plt
from Utilities.DB_query_NAV import Query_NAV
from data_analysis.DB_query import db_query
import numpy as np


def probs_up(product_id, startdate, enddate):
    # get nav increase data by day
    # df = Query_NAV(product_id, startdate, enddate)
    df = db_query(product_id, startdate, enddate, "nav_increase")
    # print(df.dtypes)  # DEBUG

    if startdate == enddate:
        return 'NaN'

    df['NAV_Increase'] = df['NAV_Increase'].astype(float)

    df.ix[df['NAV_Increase'] > 0, 'NAV_Increase'] = 1
    df.ix[df['NAV_Increase'] <= 0, 'NAV_Increase'] = 0

    count = df['NAV_Increase'].value_counts()
    p_up = count.loc[1] / len(df.index)

    return "%.4f" % p_up


# test main
# result = probs_up('GZFB0001', '2017-01-18', '2017-01-18')
# print(result)
