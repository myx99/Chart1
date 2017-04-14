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
# print(df)

# format dtype and expand to 3 charts based on the value range:
df_1 = pd.DataFrame()
df_1['Date'] = df['Date'].astype(date)
df_1['Sharpe'] = df['Sharpe'].astype(float)
df_1['Volatility'] = df['Volatility'].astype(float)
df_1['Info Rate'] = df['Info Rate'].astype(float)

df_2 = pd.DataFrame()
df_2['Date'] = df['Date'].astype(date)
df_2['Benchmark'] = df['Benchmark'].astype(float)
df_2['Average Increase'] = df['Average Increase'].astype(float) * 100
df_2['Annualized Return'] = df['Annualized Return'].astype(float) * 100

df_3 = pd.DataFrame()
df_3['Date'] = df['Date'].astype(date)
df_3['NAV_Increase'] = df['NAV_Increase'].astype(float) * 100
df_3['Probability of UP'] = df['Probability of UP'].astype(float) * 100

df_4 = pd.DataFrame()
df_4['Date'] = df['Date'].astype(date)
df_4['NAV'] = df['NAV'].astype(float)
df_4['Beta'] = df['Beta'].astype(float)
df_4['Max Drawdown Rate'] = df['Max Drawdown Rate'].astype(float)

df_1 = df_1.set_index('Date')
df_2 = df_2.set_index('Date')
df_3 = df_3.set_index('Date')
df_4 = df_4.set_index('Date')

df_1.plot()
df_2.plot()
df_3.plot()
df_4.plot()
plt.show()
