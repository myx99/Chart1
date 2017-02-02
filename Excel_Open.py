import xlrd as xd
import math
import logging
import time
import os
import shutil

# Get date
date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

# See if log file exist, archive and clear
log_file_name = "C:\\temp\\test_%s.log" % date
if os.path.exists(log_file_name):
    shutil.copy(log_file_name, "C:\\temp\\log_bak")
    f = open(log_file_name, 'w')
    f.truncate()
    f.close()

# Define logging
logger = logging.getLogger('LOG')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("C:\\temp\\test_%s.log" % date)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info(50 * "-" + "Calculate CSI300 Index" + 50 * "-")
# Open market data table
data_mkt = xd.open_workbook("C:\\temp\\mkt_csi300.xls")
table_mkt = data_mkt.sheets()[0]
# Open CSI300 combination table
data_con = xd.open_workbook("C:\\temp\\000300cons.xls")
table_con = data_con.sheets()[0]

# Get the combination stock id list
stockid_con_list = []
for row_con in range(1, table_con.nrows):
    stockid_con_list.append(str(table_con.row(row_con)[0].value))

#Calculate index
suspended_stock = []
for row_mkt in range(1,table_mkt.nrows):
    #print(table_mkt.row(row_mkt)[1].value)
    stock_id = table_mkt.row(row_mkt)[1].value  # B column
    if table_mkt.row(row_mkt)[1].value in stockid_con_list:
        # Get data from spreadsheet
        close_price = table_mkt.row(row_mkt)[3].value  # D column
        previous_close_price = table_mkt.row(row_mkt)[18].value  # S column
        total_shares = table_mkt.row(row_mkt)[30].value  # AE column
        circulatioin_shares = table_mkt.row(row_mkt)[32].value  # AG column

        # Resolve without close price situation
        if close_price == "----":
            close_price = previous_close_price
            suspended_stock.append(stock_id)

        #format data
        close_price = float(close_price.lstrip().rstrip())
        previous_close_price = float(previous_close_price.lstrip().rstrip())
        total_shares = float(total_shares[:-1].lstrip())
        circulatioin_shares = float(circulatioin_shares[:-1].lstrip())

        # Print data
        def showdata():
            print("Stock ID: %s" % stock_id)
            print("Close Price: %.2f" % close_price)
            print("Previous Close Price: %.2f" % previous_close_price)
            print("Total Shares: %.2f " % total_shares)
            print("Circulation Shares: %.2f" % circulatioin_shares)
            print("-----------------------------------------")
        #showdata()

        logger.info("#%i" % (row_mkt - 1)  + '\t' +
                    "Stock ID: %s" % stock_id + '\t' +
                    "Close Price: %.2f" % close_price + '\t' +
                    "Previous Close Price: %.2f" % previous_close_price + '\t' +
                    "Total Shares(亿): %.2f " % total_shares + '\t' +
                    "Circulation Shares(亿): %.2f" % circulatioin_shares + '\t')

logger.info("-" * 100)
logger.info("There are %d suspended stocks which listed as: %s" % (suspended_stock.__len__(), suspended_stock))

print("End")