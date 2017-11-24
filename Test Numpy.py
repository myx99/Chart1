# import time
# import numpy as np
# import random
#
# a = []
# for i in range(10):
#     a.append(i)
# b = random.randint(10, 120)
# print(b)
# print("count down")
# time.sleep(b)
# print(a)
#
# x = 1.0255
# y = 0.9959
#
# m = 200000
# roe = m * ((y-x)/x)
# shares = 195026.82
# roe2 = shares * y - m
#
# check = roe - roe2
# fee = (roe + m)*0.02
#
#
# print(roe, roe2, check)

# restaurant_list = ["a", "b", 'c', 'd', 'e', 'f']
# x = random.randint(0, 5)
# print(x)
# print(restaurant_list[x])
# import time
# product_id = "abc"
#
# factor = "sharpe"
#
# folder_path = "E:\\风控合规\风险计量\\%s\\" % time.strftime("%Y-%m-%d")
# file_name = product_id + "_" + factor + ".png"
# file_path = folder_path + file_name
# print(file_path)

# from WindPy import w
# from datetime import *
# w.start()
#
# background = w.wsd("136160.SH", "holder_pct,net_profit_is,np_belongto_parcomsh",
#                            "2005-12-30", "2016-12-31", "order=1;unit=1;rptType=1;Period=Y;Days=Alldays")
#
# print(background)

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from WindPy import *
# import time
# import datetime
#
# FactorDF = pd.read_excel("D:\\app\\mysvn\\py\\CRA\\Excel\\FactorSheet.xlsx")
# # print(FactorDF)
# FactorList = FactorDF["WindApiField"].values
# Factors = ','.join(FactorList)
# # print(Factors)
# BondCode = "135053.SH"
# thisyear = time.strftime("%Y")
# EndDate = "%s-12-31" % str(int(thisyear) - 1)
# StartDate = "2007-12-31"
# W_config = "order=1;unit=1;rptType=1;Period=Y;Days=Alldays"
#
# RawData = w.wsd(BondCode, str(Factors), StartDate, EndDate, W_config)
#
# print(RawData)
#
# def test(AUM, RateType):
#
#     if RateType is 'D':
#         standard_1_percentage = 0.05  ## D rate percentage
#         standard_2 = 2000             ## D rate quota
#     elif RateType is 'C':
#         standard_1_percentage = 0.1   ## C rate percentage
#         standard_2 = 4000             ## C rate quota
#     elif RateType is 'B':
#         standard_1_percentage = 0.5   ## B rate percentage
#         standard_2 = 5000             ## B rate quota
#
#     standard_1 = standard_1_percentage * AUM
#
#     if standard_1 <= standard_2:
#         quota = standard_2
#     elif standard_1 > standard_2:
#         quota = standard_1
#     return int(quota)
#
#
# # main
# scale = [5000, 10000, 15000, 20000, 50000, 60000, 80000, 100000, 300000, 1000000]
#
# #simple test
# # quota = [test(i) for i in scale]
# # print(quota)
# # plt.plot(scale, quota)
# # plt.show()
#
# #df test
# df_temp = pd.DataFrame()
# df_temp['AUM'] = scale
# for r in ['D', 'C', 'B']:
#     temp = []
#     for i in scale:
#         temp.append(test(i, r))
#     df_temp[r] = temp
# print(df_temp)
# df_temp = df_temp.set_index('AUM')
# df_temp.plot()
# plt.show()

from WindPy import *
import numpy as np


w.start()
turnover = w.wsd("600487.SH", "free_turn", "ED-19TD", "2017-11-17", "")
data = turnover.Data[0]
turnover_20_avg = '%.2f' % np.average(data)
# print(turnover_20_avg)

tradableshares_temp = w.wsd("600487.SH", "free_float_shares", "2017-10-31", "2017-10-31", "unit=1")
tradableshares = '%.2f' % tradableshares_temp.Data[0][0]
# print(tradableshares)

amt_temp = w.wsd("600487.SH", "amt", "ED-20D", "2017-11-17", "")
amt = amt_temp.Data[0]

amt_decrease = np.diff(amt) / amt[:-1]
amtdecrease_20_avg = '%.2f' % np.average(amt_decrease)
# print(amtdecrease_20_avg)

result_temp = float(turnover_20_avg) * float(tradableshares) * 0.0005 * 0.9
# result_temp = float(turnover_20_avg) * float(tradableshares) * 0.0005 * (1 - float(amtdecrease_20_avg))
result = '%.2f' % result_temp
print(result)
