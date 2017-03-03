import pymysql

# init db connection
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test', use_unicode=True, charset="utf8")
cur = conn.cursor()

# compile sql statement
fund = 'GZFB0001'
fund = "'%s'" % fund
select_statement = """select Occur_Date as 'Date', Subject_Name as 'NAV_Increase' from Valuation
                      where Product_ID = %s
                      and Occur_Date > '2017-01-31' and Occur_Date < '2017-03-01'
                      and Subject_Code = '净值日增长率:'
                      order by Occur_Date ; """ % fund

# get sql result
cur.execute(select_statement)
conn.commit()
rows = cur.fetchall()

for row in rows:
    print(row)

# close db connection
cur.close()
conn.close()