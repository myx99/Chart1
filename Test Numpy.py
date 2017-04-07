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

x = 1.0255
y = 1.0318

m = 200000
roe = m * ((y-x)/x)
shares = 195026.82
roe2 = shares * y - m

check = roe - roe2
fee = (roe + m)*0.02


print(roe, roe2, check)