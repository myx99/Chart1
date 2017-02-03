from WindPy import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd as xd

# Open table of (stockid, weight)
data_mkt = xd.open_workbook("D:\\app\\mysvn\\files\\test.xlsx")
table_mkt = data_mkt.sheets()[0]

# Get close price based on the stockid and calculate the weight
index = np.array([])
for row_mkt in range(table_mkt.nrows):
    stock_id_raw = table_mkt.row(row_mkt)[0].value  # A column
    weight = table_mkt.row(row_mkt)[1].value  # B column
    market = stock_id_raw[-2:]
    stock_id = stock_id_raw[:-3]

    # Test to print stock id, market and weight TODO; DELETE
    #print("stock id: " + str(stock_id) + '\t' + "market: " + str(market) + '\t' + "weight: " + str(weight))

    # Get market data from WIND
    w.start()
    data = w.wsd(stock_id_raw, "close", "2016-01-01", "2016-06-30", "Fill=Previous")
    index_by_close_price = data.Data[0]
    index_duration = data.Times
    w.stop()

    # Test to print market data TODO: DELETE
    # print(index_by_close_price[:10])
    # print(index_duration[:10])

    # Cal index
    index.append(index_by_close_price)
    print(index)

# show by plot
# x = [index_duration[i] for i in range(index_duration.__len__())]
# y = [index[i] for i in range(index.__len__())]
# plt.plot(x, y)
# plt.show()

