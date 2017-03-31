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
from data_analysis.cal_info_rate import cal_info_rate
from data_analysis.DB_insert import db_insert


# date
startdate_nav = '2017-01-18'
# startdate_nav_increase = '2017-01-19'
# startdate_sharpe = '2017-01-23'
# startdate_nav = '2017-01-23'
# startdate_nav_increase = '2017-01-23'
# startdate_sharpe = '2017-01-23'
enddate = '2017-01-31'

# benchmark code
bmc = "CGB10Y.WI"

# product
product = 'GZFB0001'

#--------------- manage risk table ----------------#
# ----> | date | nav | nav_increase |
df_nav = db_query(product, startdate_nav, enddate, "nav")
df_nav_increase = db_query(product, startdate_nav, enddate, "nav_increase")
# print(df_nav)
# print(df_nav_increase)
df_temp = pd.merge(df_nav, df_nav_increase, how='outer')
# print(df_temp)

# -----> | date | nav | nav_increase | benchmark |
w.start()
bmk_wind_data1 = w.wsd(bmc, "close", startdate_nav, enddate, "")
w.close()
# print(bmk_wind_data1.Data[0])
df_temp['Benchmark'] = bmk_wind_data1.Data[0]
# print(df_temp)
# -----> | date | nav | nav_increase | benchmark | product
df_temp['Product_ID'] = product

# -----> fill NaN with 0
# df_temp = df_temp.fillna(0)

# print(df_temp)

# -----> | date | nav | nav_increase | benchmark | product | Average_Increase | Probability of UP | Annualized_Return | Sharpe | Volatility | Beta | Info_Rate | Max_Drawdown_Rate | Max_Drawdown_StartDate | Max_Drawdown_EndDate
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
# info rate
by_day_info_rate = []
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
    # info rate
    info = cal_info_rate(product, startdate_nav, x)
    by_day_info_rate.append(info)
    # mdd
    mdd = Cal_MaxDrawdown(product, startdate_nav, x)
    by_day_maxDrawdown_rate.append(mdd[0])
    by_day_maxDrawdown_startdate.append(mdd[1])
    by_day_maxDrawdown_enddate.append(mdd[2])

# ave
df_temp["Average Increase"] = pd.Series(by_day_average_increase)
# probs up
df_temp["Probability of UP"] = pd.Series(by_day_probs_up)
# an
df_temp["Annualized Return"] = pd.Series(by_day_annualized_return)
# sp
df_temp["Sharpe"] = pd.Series(by_day_sharpe)
# vol
df_temp["Volatility"] = pd.Series(by_day_vol)
# beta
df_temp["Beta"] = pd.Series(by_day_beta)
# info rate
df_temp["Info Rate"] = pd.Series(by_day_info_rate)
# mdd
df_temp["Max Drawdown Rate"] = pd.Series(by_day_maxDrawdown_rate)
df_temp["Max Drawdown StartDate"] = pd.Series(by_day_maxDrawdown_startdate)
df_temp["Max Drawdown EndDate"] = pd.Series(by_day_maxDrawdown_enddate)

print(df_temp)

# process NaN inf nan
# df_temp = df_temp.replace(float('inf'), 0)
# df_temp = df_temp.replace(float('nan'), 0)
df_temp = df_temp.fillna('Null')
print(df_temp)

db_insert(df_temp, 'daily_risk_cal')
