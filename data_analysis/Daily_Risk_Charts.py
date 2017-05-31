import matplotlib.pyplot as plt
import pandas as pd
from WindPy import *
import pymysql
import time
import os
import matplotlib
matplotlib.use('Agg')


def risk_charting(product_id, factor):
    product = product_id

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test', use_unicode=True, charset="utf8")
    cur = conn.cursor()

    statement = "select Date, NAV, NAV_Increase, Benchmark, `Average Increase`, `Probability of UP`, " \
                "`Annualized Return`, Sharpe, Volatility, Beta, `Info Rate`, `Max Drawdown Rate` " \
                "from daily_risk_cal where Product_ID = '%s' order by Date" % product

    df = pd.read_sql(sql=statement, con=conn)

    # fill null with 0
    df = df.replace('', 0)

    # format dtype and expand to 3 charts based on the value range:
    df_temp = pd.DataFrame()
    df_temp['Date'] = df['Date'].astype(date)

    percentage_group = ['Average Increase', 'Annualized Return', 'NAV_Increase', 'Probability of UP']
    if factor not in percentage_group:
        df_temp[factor] = df[factor].astype(float)
    else:
        df_temp[factor] = df[factor].astype(float) * 100

    df_temp = df_temp.set_index('Date')

    chartname = factor + " of " + product
    df_temp.plot(kind='bar', grid='on', figsize=(20, 10), title=chartname.upper())

    getdate = time.strftime("%Y-%m-%d")
    getdate = "2017-05-26"
    folder_path = "E:/风控合规/风险计量/%s/" % getdate
    file_name = product_id + "_" + factor + ".png"
    file_path = folder_path + file_name
    # print(file_path)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    plt.savefig(file_path, dpi=120)
    plt.close()
    # plt.show()


# main
id_list = ['GZFB0001', 'GZFB0002', 'GZFB0003']
factor_list = ['Sharpe', 'Volatility', 'Info Rate', 'Benchmark', 'Average Increase', 'Annualized Return', 'NAV_Increase',
               'Probability of UP', 'NAV', 'Beta', 'Max Drawdown Rate']
for pid in id_list:
    for factor in factor_list:
        risk_charting(pid, factor)

# risk_charting('GZFB0001', 'Volatility')
