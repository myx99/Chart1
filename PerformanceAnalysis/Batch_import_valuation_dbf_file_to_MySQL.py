import os

from Utilities.DBF_to_MySQL_for_ValuationTable import dbf_to_mysql_ValuationFile


# dir = "E:\\data\\gz\\"
dir = "D:\\PerformanceAnalysis\\gz_data\\2018\\"
try:
    for parent,dirnames,filenames in os.walk(dir):
        for dirname in dirnames:
            sub_dir = dir + dirname
            for ps, ds, fs in os.walk(sub_dir):
                for f in fs:
                    dbf_file = sub_dir + "\\" + f
                    print(dbf_file)
                    id = dbf_file[-12:-4]
                    filetype = dbf_file[-4:]
                    # print(id)
                    # print(filetype)
                    if filetype == '.dbf':
                        dbf_to_mysql_ValuationFile(dbf_file)
                        print("ok")
                    else:
                        print("Not a DBF file")
except Exception as error:
    print(error)


