from PerformanceTest import DBquery
import pandas as pd
import datetime
from WindPy import *
import numpy as np


w.start()


def singlestock_day_liquility(stockid, x):
    turnover = w.wsd(stockid, "free_turn", "ED-19TD", "2017-11-17", "")
    data = turnover.Data[0]
    turnover_20_avg = '%.2f' % np.average(data)
    # print(turnover_20_avg)

    tradableshares_temp = w.wsd(stockid, "free_float_shares", "2017-10-31", "2017-10-31", "unit=1")
    tradableshares = '%.2f' % tradableshares_temp.Data[0][0]
    # print(tradableshares)

    amt_temp = w.wsd(stockid, "amt", "ED-20D", "2017-11-17", "")
    amt = amt_temp.Data[0]

    amt_decrease = np.diff(amt) / amt[:-1]
    amtdecrease_20_avg = '%.2f' % np.average(amt_decrease)
    # print(amtdecrease_20_avg)

    # result_temp = float(turnover_20_avg) * float(tradableshares) * 0.0005 * (1 - float(amtdecrease_20_avg))
    result_temp = float(turnover_20_avg) * float(tradableshares) * 0.0005 * float(x)
    result = '%.2f' % result_temp
    # print(result)
    return result



def cal(Product_ID, rate):
    board1 = '%1102010160%'
    board2 = '%1102310100%'
    board3 = '%110241013%'
    print(Product_ID, rate)

    df1 = DBquery(Product_ID, board1)
    df2 = DBquery(Product_ID, board2)
    df3 = DBquery(Product_ID, board3)
    df_temp = df1.append(df2).append(df3)

    daysoffset = 85
    StockIdList_temp = df_temp["Subject_Code"].values
    StockIdList = []
    stockliquilitylist = []
    for i in StockIdList_temp:
        newi = i[8:]
        if newi[0] == '6':
            suffix = '.SH'
        else:
            suffix = '.SZ'
        StockID = newi + suffix
        sll = float(singlestock_day_liquility(StockID, rate))*daysoffset
        StockIdList.append(StockID)
        stockliquilitylist.append(sll)

    df = pd.DataFrame()
    df['Date'] = df_temp['Occur_Date']
    df["StockID"] = StockIdList
    df['MktValue'] = df_temp['Market_Value_Original_Currency'].astype(float)
    df['Liquility_Temp'] = stockliquilitylist
    print(df)


Product_list = ['GZFB0001', 'GZFB0002']
rate_list = [0.9, 0.8, 0.65]

for p in Product_list:
    for r in rate_list:
        cal(p, r)





