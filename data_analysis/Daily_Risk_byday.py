import pandas as pd
from WindPy import *
import time
from data_analysis.Annualized_Return import annualized_return
from data_analysis.MaxDrawdown import Cal_MaxDrawdown
from data_analysis.Sharpe_Ratio import Cal_Sharpe
from data_analysis.DB_query import db_query
from data_analysis.Average_Increase import average_increase
from data_analysis.Probability_of_UP import probs_up
from data_analysis.Volatility import volatility
from data_analysis.cal_beta import cal_beta
from data_analysis.cal_info_rate import cal_info_rate
from data_analysis.DB_insert import db_insert


def cal_risk_all(p, d, b):
    df_nav = db_query(p, d, d, "nav")
    df_nav_increase = db_query(p, d, d, "nav_increase")
    # print(df_nav)
    # print(df_nav_increase)
    df_temp = pd.merge(df_nav, df_nav_increase, how='outer')
    # print(df_temp)
    w.start()
    bmk_wind_data1 = w.wsd(b, "close", d, d, "")
    w.close()
    # print(bmk_wind_data1.Data[0])
    df_temp['Benchmark'] = bmk_wind_data1.Data[0]
    # print(df_temp)
    # -----> | date | nav | nav_increase | benchmark | product
    df_temp['Product_ID'] = p
    # print(df_temp)

    startdate_nav = '2017-01-18'
    # ave
    df_temp["Average Increase"] = average_increase(p, startdate_nav, d)
    # probs up
    df_temp["Probability of UP"] = probs_up(p, startdate_nav, d)
    # an
    df_temp["Annualized Return"] = annualized_return(p, startdate_nav, d)
    # sharpe
    df_temp["Sharpe"] = Cal_Sharpe(p, startdate_nav, d)
    # vol
    df_temp["Volatility"] = volatility(p, startdate_nav, d)
    # beta
    df_temp["Beta"] = cal_beta(p, startdate_nav, d)
    # info rate
    df_temp["Info Rate"] = cal_info_rate(p, startdate_nav, d)
    # mdd
    df_temp["Max Drawdown Rate"] = Cal_MaxDrawdown(p, startdate_nav, d)[0]
    df_temp["Max Drawdown Start Date"] = Cal_MaxDrawdown(p, startdate_nav, d)[1]
    df_temp["Max Drawdown End Date"] = Cal_MaxDrawdown(p, startdate_nav, d)[2]

    # print(df_temp)

    # process NaN inf nan
    df_temp = df_temp.replace(float('inf'), '')    # inf
    # df_temp = df_temp.replace(float('nan'), 'null')
    df_temp = df_temp.replace('nan', '')    #  nan
    df_temp = df_temp.replace('NaN', '')    # NaN (str)
    df_temp = df_temp.fillna('')    # NaN (float)
    # print(df_temp)

    db_insert(df_temp, 'daily_risk_cal')

# test main
# given_date = time.strftime("%Y-%m-%d")
given_date = '2017-04-06'
bmc = "CGB10Y.WI"
product_group = ['GZFB0001', 'GZFB0002']
for product in product_group:
    cal_risk_all(product, given_date, bmc)
