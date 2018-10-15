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
#
# from WindPy import *
# import numpy as np
#
#
# # w.start()
# #
# # x = w.wsd("000746.OF", "nav", "2017-01-01", "2017-11-30", "Currency=CNY")
#
# import pandas as pd
#
#
# df = pd.read_excel('C:/Users/taoma/Documents/行研/echarts/test1.xlsx')
# print(df)
#
# columns = df.columns
# index = df.index
#
# columns_count = len(columns)
# index_count = len(index)

# print(columns_count, columns, index_count, index)

# array = []
# array_origin = []
# for i in range(index_count):
#     for j in range(columns_count):
#         cell_origin = df.iloc[i, j]
#         cell_reform = cell_origin.astype(float) / 700
#         cell_result = '%.0f' % cell_reform
#         cell1 = [i, j, cell_result]
#         cell2 = [i, j, cell_origin]
#         array.append(cell1)
#         array_origin.append(cell2)
# print('array reformed: '+ '\n', array)
# print('array origin: '+ '\n', array_origin)
# print('columns: '+ '\n', columns)
# print('index: '+ '\n', index)


# b = '2018-09-21'
# # c = b[0:3]+b[5:6] + b[8:9]
# c = b.replace("-", "")
# print(b, c)

import time

today = time.strftime("%Y%m%d")
print(today)
e = '2018-10-02'
end = e.replace("-", "")
print(end)
if today > end:
    print("yes")
else:
    print("no")
