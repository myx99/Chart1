import pymysql
import os
import time


# define dbf to mysql function
def txt_to_mysql_FutureSettlementFile(filename, filetype):

    # set mysql connection
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test', use_unicode=True, charset="utf8")
    cur = conn.cursor()

    # get broker id
    filename_temp = filename.split('\\')
    broker_id = filename_temp[-1][:4]
    print(broker_id)

    # read txt file
    f = open(filename,mode='r')
    lines = f.readlines()
    for line in lines:
        # init
        temp = []
        values = []

        # format line
        temp = line.split('@')
        temp[-1] = temp[-1].strip('\n')
        temp.append(broker_id)

        # add '' for strings (or can't be insert to db)
        for x in temp:
            # if type(x) is type(0.0):
            #     value = x
            # elif type(x) is type(0):
            #     value = float(x)
            # else:
            value = "'%s'" % str(x).encode('utf-8').decode('utf-8')
            values.append(value)
        print(temp)
        print(values)
        insert_values = tuple(values)

        # insert record to mysql db by line
        ## Case 1 - cus account table
        if filetype == "cusaccount":
            insert_statement = """insert into Future_cusaccount values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % insert_values
        elif filetype == "cuscode":
            insert_statement = """insert into Future_cuscode values(%s,%s,%s,%s,%s)""" % insert_values
        elif filetype == "cusfund":
            insert_statement = """insert into Future_cusfund values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % insert_values
        elif filetype == "trddata":
            insert_statement = """insert into Future_trddata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % insert_values
        else:
            print("filetype error....")
            break
        cur.execute(insert_statement)
        conn.commit()
        print("Data inserted!")

    # close mysql connection
    cur.close()
    conn.close()


# main
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
