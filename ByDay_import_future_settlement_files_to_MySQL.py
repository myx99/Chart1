import os
import time
from Utilities.TXT_to_MySQL_for_future_settlement_file import txt_to_mysql_FutureSettlementFile


date = time.strftime("%Y%m%d")
# date = "20170310"
path = "E:\\data\\gzouter\\%s\\" % date

filetype_list = ["cusaccount", "cuscode", "cusfund", "trddata"]

for parent, dirnames, filenames in os.walk(path):
    for f in filenames:
        filetype = f[4:-12]
        file = path + f
        # print(file, filetype)
        if filetype in filetype_list:
            txt_to_mysql_FutureSettlementFile(file, filetype)
            # print("--------> ")
            # print(file, filetype)
            # print("<-------- ")
