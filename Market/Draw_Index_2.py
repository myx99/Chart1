from WindPy import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd as xd

# Open table of (stockid, weight)
data_mkt = xd.open_workbook("D:\\app\\mysvn\\files\\test.xlsx")
table_mkt = data_mkt.sheets()[0]

# Set period
start_date = "2016-01-01"
end_date = "2016-01-06"

# Start Wind api
w.start()

# Create dataframe using dates as index
# Get date list
dates = w.tdays(start_date, end_date, "")
date_raw = dates.Times
date_count = dates.Times.__len__()
index_dates = []
for i in range(date_count):
    date_format = str(date_raw[i])[:10]
    index_dates.append(date_format)
# Create dataframe using dates as index
df = pd.DataFrame(index=index_dates)
# print(df)
columns = []

# Get close price based on the stockid and calculate the weight
for row_mkt in range(table_mkt.nrows):
    stock_id_raw = table_mkt.row(row_mkt)[0].value  # A column
    weight = table_mkt.row(row_mkt)[1].value  # B column
    market = stock_id_raw[-2:]
    stock_id = stock_id_raw[:-3]

    # Get market data from WIND
    data = w.wsd(stock_id_raw, "close", start_date, end_date, "Fill=Previous")
    index_by_close_price = [round(float(i)*weight,4) for i in data.Data[0]]
    # print(index_by_close_price )

    # Add data to dataframe
    df[stock_id_raw] = pd.Series(index_by_close_price, index=df.index)
    columns.append(stock_id_raw)

# Stop Wind API
w.stop()

print(df)

# Aggregate
f1 = [lambda s: s[0] + s[i] for i in range(1, columns.__len__())]
sum_df = df.apply(f1, axis=1)
print(sum_df)

column_sum = []
for i in range(columns.__len__()):
    print(df.valu[columns[i]])
    column_sum += df[columns[i]]
print(column_sum)


# Display
# df.plot()
# plt.show()


