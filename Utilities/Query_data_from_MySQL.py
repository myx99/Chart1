import pymysql
import pandas as pd


def Query_MySQL(fund_id, startdate, enddate):
    # init db connection
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test', use_unicode=True, charset="utf8")
    cur = conn.cursor()

    # compile sql statement
    # This is to get the NAV increase rate from db and calculate SHARPE value
    select_statement = "select Occur_Date as 'Date', Subject_Name as 'NAV_Increase' from Valuation " \
                       "where Product_ID = '%s' " \
                       "and Occur_Date >= '%s' and Occur_Date <= '%s' " \
                       "and Subject_Code = '净值日增长率(%s):' " \
                       "order by Occur_Date" % (fund_id, startdate, enddate, '%')
    # print(select_statement)  # DEBUG

    # use pandas to get the sql result
    # df = pd.read_sql(sql=select_statement, con=conn, index_col="Date")
    df = pd.read_sql(sql=select_statement, con=conn)
    # print(df)  # DEBUG
    return df

    # close db connection
    cur.close()
    conn.close()
