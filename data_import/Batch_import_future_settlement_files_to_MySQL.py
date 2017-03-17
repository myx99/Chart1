import os
import time
from Utilities.TXT_to_MySQL_for_future_settlement_file import txt_to_mysql_FutureSettlementFile


path = "E:\\data\\gzouter\\"
# date = time.strftime("%Y%m%d")
filetype_list = ["cusaccount", "cuscode", "cusfund", "trddata"]

for parent, dirnames, filenames in os.walk(path):
    for dn in dirnames:
        sub_path = path + dn
        for ps, ds, fs in os.walk(sub_path):
            for f in fs:
                filetype = f[4:-12]
                file = sub_path + "\\" + f
                # print(file, filetype)
                if filetype in filetype_list:
                    txt_to_mysql_FutureSettlementFile(file, filetype)
                    # print("-----------targeted files: ", file, filetype)
