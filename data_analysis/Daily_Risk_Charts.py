import matplotlib.pyplot as plt
import pandas as pd
from WindPy import *
import pymysql

product = 'GZFB0001'

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test', use_unicode=True, charset="utf8")
cur = conn.cursor()

statement = "select Date, NAV, NAV_Increase, Benchmark, `Average Increase`, `Probability of UP`, " \
            "`Annualized Return`, Sharpe, Volatility, Beta, `Info Rate`, `Max Drawdown Rate` " \
            "from daily_risk_cal where Product_ID = '%s' order by Date" % product

df = pd.read_sql(sql=statement, con=conn)

# print(df)

# fill null with 0
df = df.replace('', 0)
# df = df.replace(460.3235, 0)

print(df)

# format dtype
df['Date'] = df['Date'].astype(date)
df['NAV'] = df['NAV'].astype(float)
df['NAV_Increase'] = df['NAV_Increase'].astype(float)
df['Benchmark'] = df['Benchmark'].astype(float)
df['Average Increase'] = df['Average Increase'].astype(float)
df['Probability of UP'] = df['Probability of UP'].astype(float)
df['Annualized Return'] = df['Annualized Return'].astype(float)
df['Sharpe'] = df['Sharpe'].astype(float)
df['Volatility'] = df['Volatility'].astype(float)
df['Beta'] = df['Beta'].astype(float)
# df['Info Rate'] = df['Info Rate'].astype(float)
df['Max Drawdown Rate'] = df['Max Drawdown Rate'].astype(float)

df = df.set_index('Date')
df.plot()
plt.show()
