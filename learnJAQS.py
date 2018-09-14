from jaqs.data import DataApi
import matplotlib.pyplot as plt
# matplotlib inline
import pandas as pd
import numpy as np


api = DataApi(addr='tcp://data.tushare.org:8910')
phone = 'phone'
token = 'token'
df, msg = api.login(phone, token)
print(df, msg)


df, msg = api.query(
    view="jz.instrumentInfo",
    fields="market,symbol,list_date,status",
    filter="inst_type=1&status=1&market=SH,SZ",
    data_format="pandas"
)

df.index = df['symbol']
df.sort_index(inplace=True)

print(len(df))
print(len(df[df['market']=='SZ']))
print(len(df[df['market']=='SH']))
