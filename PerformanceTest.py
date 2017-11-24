from WindPy import *
import pandas as pd
import pymysql


w.start()

def SingleStockGrowthRate(StockId):
    data = w.wsd(StockId, "pct_chg,trade_status", "ED-120TD", "2017-10-31", "ShowBlank=-1;PriceAdj=F")
    light = 0
    rawdata = data.Data[0]
    # print(rawdata)
    status = data.Data[1]
    # print(status[-1])
    # listed less than 120 trade days
    for i in rawdata:
        if i == -1 or i is None:
            light = 1
            break
    # suspended
    # for j in status:
    #     if j is None or j == "停牌一天":
    #         light = 2
    #         break
    if status[-1] == "停牌一天":
        light = 2

    if light != 0:
        return None
    elif light == 0:
        date_raw = data.Times
        date_count = data.Times.__len__()
        index_dates = []
        for i in range(date_count):
            date_format = str(date_raw[i])[:10]
            index_dates.append(date_format)
        df = pd.DataFrame()
        df['Date'] = index_dates
        df[StockId] = data.Data[0]
        df[StockId] = df[StockId].astype(float)
        return df


# x = SingleStockGrowthRate("399102.SZ")
# print(x)


def SingleBeta(StockId, IndexId):
    df_SH_Index = SingleStockGrowthRate(IndexId)
    df_SH_Stock = SingleStockGrowthRate(StockId)
    if df_SH_Stock is None:
        beta = 1
    else:
        df = pd.merge(df_SH_Index, df_SH_Stock, how='left', on='Date')
        beta = df[StockId].cov(df[IndexId]) / df[IndexId].var()
    return "%.4f" % beta


# result = SingleBeta("300083.SZ", "399102.SZ")
# print(result)
# pass


def DBquery(Product_ID, board):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test', use_unicode=True, charset="utf8")
    cur = conn.cursor()
    sql_statement = "select Occur_Date, Subject_Code, Subject_Name, Market_Value_Original_Currency from Valuation " \
                    "where Occur_Date = '2017-10-31' and Product_ID = '%s' and Subject_Code like '%s';" % (Product_ID, board)
    df = pd.read_sql(sql=sql_statement, con=conn)
    return df
    cur.close()
    conn.close()


def getStockList(Product_ID, board, IndexID, board2=None):
    if board2 is not None:
        df1 = DBquery(Product_ID, board)
        df2 = DBquery(Product_ID, board2)
        df = df1.append(df2)
        # print(df)
        # pass
    else:
        df = DBquery(Product_ID, board)
    # print(df)
    if IndexID == "000001.SH":
        suffix = ".SH"
    else:
        suffix = ".SZ"
    StockIdList_temp = df["Subject_Code"].values
    StockIdList = []
    BetaList = []
    for i in StockIdList_temp:
        newi = i[8:]
        StockID = newi + suffix
        # print(StockID)
        beta = SingleBeta(StockID, IndexID)
        StockIdList.append(newi)
        BetaList.append(beta)

    df["StockID"] = StockIdList
    df["Beta"] = BetaList
    df["Market_Value_Original_Currency"] = df["Market_Value_Original_Currency"].astype(float)
    df["Beta"] = df["Beta"].astype(float)
    df["MktValueBasedBeta"] = df["Market_Value_Original_Currency"] * df["Beta"]
    # print(df)
    # print(df["MktValueBasedBeta"].sum())
    # print(df["Market_Value_Original_Currency"].sum())
    MktValueSum = df["Market_Value_Original_Currency"].sum()
    if MktValueSum == 0:
        return [0, 0]
    else:
        BetaOfBoard = df["MktValueBasedBeta"].sum() / MktValueSum
        MktValueSum =  "%.2f" % MktValueSum
        BetaOfBoard =  "%.2f" % BetaOfBoard
        SumNBeta = [MktValueSum, BetaOfBoard]
        # print(SumNBeta[0], SumNBeta[1])
        return SumNBeta


# result = getStockList('GZFB0003', '%110241013%', "399102.SZ")
# print(result)

productlist = ['GZFB0001', 'GZFB0002', 'GZFB0003', 'GZFB0004']
boardlist = [['%1102010160%', "000001.SH"], [['%11023101000%', '%11023101001%'], "399001.SZ"], ['%11023101002%', "399101.SZ"], ['%110241013%', "399102.SZ"]]


if __name__ == '__main__':
    for p in productlist:
        for b in boardlist:
            if len(b[0]) != 2:
                x = "process input:%s, %s, %s" % (p, b[0], b[1])
                # print(x)
                result = getStockList(p, b[0], b[1])
            elif len(b[0]) == 2:
                y = "process input:%s, %s, %s, %s" % (p, b[0][1], b[1], b[0][1])
                # print(y)
                result = getStockList(p, b[0][0], b[1], b[0][1])
            output = "Product: %s  |  Market: %s  |  Market Value Sum: %s  |  BetaOfBoard: %s" % (p, b[-1], result[0], result[1])
            print(output)


w.stop()
