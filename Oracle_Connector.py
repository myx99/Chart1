import cx_Oracle   # cp D:\Oracle\product\11.2.0\client_1\BIN\oci.dll D:\Anaconda3\Lib\site-packages if failed
import pandas as pd

# conn = cx_Oracle.connect('trade_read/trade_read@172.17.100.15/testzgdb')
# conn2 = cx_Oracle.connect('trade_read/trade_read@172.17.100.15/testzgdb')
conn3 = cx_Oracle.connect('wdtest/wdtest@172.17.100.18/testwd')
cursor = conn3.cursor()

sqls = "select * from trade.Tfundstock"

df = pd.read_sql(sql=sqls, con=conn3)

print(df)

conn3.close()
