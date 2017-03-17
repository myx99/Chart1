from Utilities.Sharpe_Ratio import Cal_Benchmark_Rate
import time
from data_analysis.DB_query import db_query


startdate = '2017-01-19'
enddate = '2017-02-28'

#--------------- manage risk table ----------------#
# ----> date, nav and nav_increase
df_nav = db_query('GZFB0001', enddate, enddate, "nav")
# print(df_nav)

df_nav_increase = db_query('GZFB0001', enddate, enddate, "nav_increase")
# print(df_nav_increase)

df_nav['Nav_Day_Increase'] = df_nav_increase['NAV_Increase']

print(df_nav)
# print(df_nav.iloc[0])

# ----->

# benchmark
tbcode = "M1001654"
dpcod = "M1001648"
bmk_eq = Cal_Benchmark_Rate(tbcode, startdate, enddate)
bmk_fi = Cal_Benchmark_Rate(dpcod, startdate, enddate)

print("%s : benckmark_return1: %.4f , benckmark_return2: %.4f" % (enddate, bmk_eq, bmk_fi))

df_nav['Benchmark1'].values = "%.4f" % bmk_eq
df_nav['Benchmark2'].values = "%.4f" % bmk_fi


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


