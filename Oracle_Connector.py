import cx_Oracle   # cp D:\Oracle\product\11.2.0\client_1\BIN\oci.dll D:\Anaconda3\Lib\site-packages if failed
import pandas as pd

conn = cx_Oracle.connect('trade_read/trade_read@172.17.100.15/testzgdb')
conn2 = cx_Oracle.connect('trade_read/trade_read@172.17.100.15/testzgdb')
cursor = conn.cursor()

sqls = "select * from trade.Tfundstock"

df = pd.read_sql(sql=sqls, con=conn)

print(df)

# cursor.execute(sqls)
# rows = cursor.fetchone()
# for row in rows:
#     print(row)
#
# cursor.close()
conn.close()
