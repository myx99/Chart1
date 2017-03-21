import pandas as pd
from WindPy import *
from data_analysis.Annualized_Return import annualized_return
from data_analysis.MaxDrawdown import Cal_MaxDrawdown
from data_analysis.Sharpe_Ratio import Cal_Sharpe
from data_analysis.DB_query import db_query
from data_analysis.Average_Increase import average_increase
from data_analysis.Probability_of_UP import probs_up
from data_analysis.Volatility import volatility
from data_analysis.cal_beta import cal_beta


# date
startdate_nav = '2017-01-18'
startdate_nav_increase = '2017-01-19'
startdate_sharpe = '2017-01-23'
enddate = '2017-02-28'

# product
product = 'GZFB0001'

#--------------- manage risk table ----------------#
# ----> date, nav and nav_increase
df_nav = db_query(product, startdate_nav, enddate, "nav")
# print(df_nav)

df_nav_increase = db_query(product, startdate_nav_increase, enddate, "nav_increase")
# print(df_nav_increase)

# print(df_nav)
# print(df_nav_increase)

df_temp = pd.merge(df_nav, df_nav_increase, how='outer')
# print(df_temp)

# -----> benchmark
w.start()
bmk_wind_data1 = w.wsd("M1001654", "close", startdate_nav, enddate, "Fill=Previous")
w.close()
df_temp['Benchmark'] = bmk_wind_data1.Data[0]

# -----> product
df_temp['Product_ID'] = product

# NaN --> 0
df_temp = df_temp.fillna(0)

# -----> beta
# df_temp['Beta'] = df_temp['NAV_Increase'].astype(float).cov(df_temp['Benchmark'].astype(float)) / df_temp['Benchmark'].astype(float).var()

print(df_temp)

# -----> average increase, annualized return, sharpe, maxdrawdown
w.start()
date_list = w.tdays(startdate_nav, enddate, "").Times
w.close()
dates = []
for i in date_list:
    dates.append(i.isoformat()[:10])
date_count = dates.__len__()
# ave
by_day_average_increase = []
# pup
by_day_probs_up = []
# an
by_day_annualized_return = []
# sharpe
by_day_sharpe = []
# vol
by_day_vol = []
# beta
by_day_beta = []
# mdd
by_day_maxDrawdown_rate = []
by_day_maxDrawdown_startdate = []
by_day_maxDrawdown_enddate = []
date_x = []
for i in range(1, date_count+1):
    x = '%s' % dates[i-1]
    # print(x)
    date_x.append(x)
    # ave
    ave = average_increase(product, startdate_nav, x)
    by_day_average_increase.append(ave)
    # probs up
    pup = probs_up(product, startdate_nav, x)
    by_day_probs_up.append(pup)
    # an
    an = annualized_return(product, startdate_nav, x)
    by_day_annualized_return.append(an)
    # sharpe
    sp = Cal_Sharpe(product, startdate_nav, x)
    by_day_sharpe.append(sp)
    # vol
    vol = volatility(product, startdate_nav, x)
    by_day_vol.append(vol)
    # beta
    bt = cal_beta(product, startdate_nav, x)
    by_day_beta.append(bt)
    # mdd
    mdd = Cal_MaxDrawdown(product, startdate_nav, x)
    by_day_maxDrawdown_rate.append(mdd[0])
    by_day_maxDrawdown_startdate.append(mdd[1])
    by_day_maxDrawdown_enddate.append(mdd[2])

# ave
df_temp["Average_Increase"] = pd.Series(by_day_average_increase)
# probs up
df_temp["Probability of UP"] = pd.Series(by_day_probs_up)
# an
df_temp["Annualized_Return"] = pd.Series(by_day_annualized_return)
# sp
df_temp["Sharpe"] = pd.Series(by_day_sharpe)
# vol
df_temp["Volatility"] = pd.Series(by_day_vol)
# beta
df_temp["Beta"] = pd.Series(by_day_beta)
# mdd
df_temp["Max_Drawdown_Rate"] = pd.Series(by_day_maxDrawdown_rate)
df_temp["Max_Drawdown_StartDate"] = pd.Series(by_day_maxDrawdown_startdate)
df_temp["Max_Drawdown_EndDate"] = pd.Series(by_day_maxDrawdown_enddate)

print(df_temp)


#--------------- Sharpe ----------------#
# today = time.strftime("%Y%m%d")
# today = "2017-03-10"
#
# product_list = ['GZFB0001', 'GZFB0002']
#
# # print("The risk data of today ( %s ) is as below: " % today)
# for product in product_list:
#     Daily_Sharpe_Value = Cal_Sharpe(product, '2017-01-19', today)
#     print("Sharpe value of product: "
#           "%s  is  %.4f  ( Rf = 10Y Treasury Bond return )"
#           % (product, Daily_Sharpe_Value))
#
# for product in product_list:
#     Daily_Sharpe_Value = Cal_Sharpe(product, '2017-01-19', today, "ZB")
#     print("Sharpe value of product: "
#           "%s  is  %.4f  ( Rf = 0 )"
#           % (product, Daily_Sharpe_Value))


