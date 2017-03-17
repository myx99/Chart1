from WindPy import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

class stock:
    def __init__(self):
        self.date = 0
        self.closeprice = 0
        self.id = ""

w.start()
stocks = ["000001.SZ","002517.SZ","300392.SZ"]
for stock in stocks:
    print(stocks.index(stock))
    plt.figure(stocks.index(stock)+1)
    data=w.wsd(stock, "close", "2016-01-01", "2016-06-30", "TradingCalendar=SZSE;Fill=Previous")
    #print(data)
    #print(data.Times.__len__())
    count = data.Times.__len__()
    x = [data.Times[i] for i in range(count)]
    y = [data.Data[0][i] for i in range(count)]
    plt.plot(x,y)
plt.show()
w.close