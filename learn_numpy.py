import tushare as ts
import matplotlib.pyplot as plt
import numpy as np

data1 = ts.get_hist_data('600050','2016-01-01','2016-01-31')
# print(data1[-10:-1:5])
# print(data1.loc[:,['close','volume']])
data2 = data1.loc[:,['close','volume']]
close_price = data2.values[:,:1].ravel()
volume = data2.values[:,1:2].ravel()
print(close_price)
print(volume)
vwap = np.average(close_price, weights=volume)
print(vwap)

data2 = data2.cumsum()
data2.plot()
# plt.figure()
# plt.legend(loc='best')
# plt.show()