from WindPy import *


# get 10Y T-bond return as benchmark(non-risk) return rate
w.start()
data = w.wsd("M1001654", "close", "2017-01-19", "2017-02-27", "Fill=Previous")
print(data)
brr = data.Data[0]
print(brr)
print(brr)
w.close