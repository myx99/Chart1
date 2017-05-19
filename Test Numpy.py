# import time
# import numpy as np
import random
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
x = 1.0255
y = 0.9959

m = 200000
roe = m * ((y-x)/x)
shares = 195026.82
roe2 = shares * y - m

check = roe - roe2
fee = (roe + m)*0.02


print(roe, roe2, check)

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