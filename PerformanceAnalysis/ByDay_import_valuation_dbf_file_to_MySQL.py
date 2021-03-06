import os
import time
from .Import_ValuationDBF_to_MySQL import dbf_to_mysql_ValuationFile


# import by single folder based on the designated date
date = time.strftime("%Y%m%d")
date = "20170118"
dir = "D:\\PerformanceAnalysis\\gz_data\\2018\\" + date
print(dir)
try:
    for ps, ds, fs in os.walk(dir):
        for f in fs:
            dbf_file = dir + "\\" + f
            print(dbf_file)
            id = dbf_file[-12:-4]
            filetype = dbf_file[-4:]
            print(id)
            print(filetype)
            if filetype == '.dbf':
                dbf_to_mysql_ValuationFile(dbf_file)
                print(dbf_file + " has been imported!!!")
            else:
                print(dbf_file + " is not a DBF file, ignore to import...")
except Exception as error:
    print(error)

