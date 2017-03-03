import os
from Utilities.TXT_to_MySQL_for_future_settlement_file import txt_to_mysql_FutureSettlementFile


path = "D:\\data\\future\\"
# filetype = "cusaccount"
# filetype = "cuscode"
# filetype = "cusfund"
filetype = "trddata"
for parent, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filetype in filename:
            file = path + filename
            print(file)
            txt_to_mysql_FutureSettlementFile(file, filetype)