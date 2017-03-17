from scripts.data_analysis.s_Sharpe_Ratio import Cal_Sharpe
import time


today = time.strftime("%Y%m%d")
today = "2017-03-10"

product_list = ['GZFB0001', 'GZFB0002']

# print("The risk data of today ( %s ) is as below: " % today)
for product in product_list:
    Daily_Sharpe_Value = Cal_Sharpe(product, '2017-01-19', today)
    print("Sharpe value of product: "
          "%s  is  %.4f  ( Rf = 10Y Treasury Bond return )"
          % (product, Daily_Sharpe_Value))

for product in product_list:
    Daily_Sharpe_Value = Cal_Sharpe(product, '2017-01-19', today, "ZB")
    print("Sharpe value of product: "
          "%s  is  %.4f  ( Rf = 0 )"
          % (product, Daily_Sharpe_Value))
