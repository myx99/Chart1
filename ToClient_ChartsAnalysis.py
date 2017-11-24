# -*- coding: utf-8 -*-
from WindPy import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager
import subprocess
from pylab import mpl
import pymysql


w.start()

def getwinddata():
    data = w.wsd("600487.SH", "close", "2017-05-01", "2017-10-31", "")

    date_raw = data.Times
    date_count = data.Times.__len__()
    index_dates = []
    for i in range(date_count):
        date_format = str(date_raw[i])[:10]
        index_dates.append(date_format)
    df = pd.DataFrame()
    df['Date'] = index_dates
    df['Date'] =df['Date'].astype(date)
    df['ClosePrice'] = data.Data[0]
    df['ClosePrice'] = df['ClosePrice'].astype(float)
    return df


def dbquery():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test', use_unicode=True, charset="utf8")
    cur = conn.cursor()
    sql_statement = "select Occur_Date as Date, Quantity from Valuation where Occur_Date < '2017-10-01' and Product_ID = 'GZFB0003' " \
                    "and Subject_Code like '%600487%' group by Quantity order by Occur_Date;"
    df = pd.read_sql(sql=sql_statement, con=conn)
    df['Date'] = df['Date'].astype(date)
    return df
    cur.close()
    conn.close()


df1 = getwinddata()
# print(df1)
df2 = dbquery()
# print(df2)
df = pd.merge(df1, df2, how='left', on='Date')
df = df.replace('NaN', 0)
print(df)

df = df.set_index('Date')
df['ClosePrice'] = df['ClosePrice'].astype(float)
df['Quantity'] = df['Quantity'].astype(float)

ChartName = u"股价走势"
mpl.rcParams['font.sans-serif'] = ['SimHei']
# df.plot(kind='line', grid='on', figsize=(20, 10), title=ChartName.upper())
df['ClosePrice'].plot( kind='line')
df['Quantity'].plot(kind='hist')
plt.legend(x=u'日期', y=u'当日收盘价',loc='best', grid='on', figsize=(20, 10), title=ChartName.upper())
plt.show()

