import PerformanceAnalysis.DailyGenerate_BasicPerformanceInfo as DGBPI
from Common.OracleConnector import OracleConnector
import pandas as pd
from Common.GlobalConfig import GlobalConfig
import time


def tradeDayCollect(start, end):
    m = OracleConnector()
    connection = m.getConn()
    sqls = "select trade_days from wind.asharecalendar where S_INFO_EXCHMARKET = 'SZSE' and trade_days >= '%s' and trade_days <= '%s' order by trade_days" % start, end
    df = pd.read_sql(sql=sqls, con=connection)
    tradedays = df['TRADE_DAYS']
    print(tradedays)
    return tradedays
    m.closeConn()


def singleImport(pid):
    m = GlobalConfig()
    start_temp = m.getConfig(pid, 'Start_date')
    start = start_temp.replace("-", "")
    end_temp = m.getConfig(pid, 'End_date')
    end_temp2 = end_temp.replace("-", "")
    today = time.strftime("%Y%m%d")  #TODO use yeaterday tmp = (datetime.date.today() - datetime.timedelta(days = 1)).strftime("%Y%m%d")
    if end_temp2 is "notyet":
        end = today
    elif today > end_temp2:
        end = end_temp2
    tradedays = tradeDayCollect(start, end)
    print(tradedays)
    for td in tradedays:
        array = DGBPI.composeArray(pid, td)
        print(array)
        DGBPI.insertArray(array)





pid = 'FB0004'
singleImport(pid)

m = GlobalConfig()
product_list = m.getConfig('product', 'list')
for p in product_list:
    singleImport(p)

