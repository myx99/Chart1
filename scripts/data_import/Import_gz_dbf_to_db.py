import pymysql
from dbfread import DBF
import os
import time


# define dbf to mysql function
def dbf_to_mysql_ValuationFile(filename):

    # set mysql connection
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test', use_unicode=True, charset="utf8")
    cur = conn.cursor()

    # load dbf and insert to db
    dbf_file = filename
    product = dbf_file[-12:-4]
    table = DBF(filename=dbf_file, load=True, encoding="gb2312")

    # get record
    for row in table.records:
        temp_row_list = []

        # filter empty lines
        if row.get('A0') == '' or row.get('Ffdate') == '':
            continue

        # get values for each rows
        for key in row:
            x = row.get(key)
            if not (type(x) is type(0.0)):
                value1 = str(x).encode('utf-8').decode('utf-8')
                value = "'%s'" % value1
            else:
                value = x
            temp_row_list.append(value)

        # mark product id
        product_id = "'%s'" % str(product).encode('utf-8').decode('utf-8')
        temp_row_list.append(product_id)

        # replace None with 0.0/0 for float/int field
        ## define a method first
        def replace_none_value(list, startpoint, endpoint, givenvalue):
            s = int(startpoint)
            if endpoint == 'null':  # single item
                if list[s] == "'None'":
                    list[s] = givenvalue
                return list
            else:
                e = int(endpoint)
                for i in list[s:e]:  # multiple items
                    if i ==  "'None'":
                        list[list.index(i)] = givenvalue
                return list
        ## execute the method
        row_list = replace_none_value(temp_row_list,3,7,0.0)
        row_list = replace_none_value(temp_row_list,12,17,0.0)
        row_list = replace_none_value(temp_row_list,-2,'null',0)

        # format list to tuple
        insert_values = tuple(row_list)
        print(row_list)
        print(insert_values)

        # compile sql statement
        insert_statement = """insert into Valuation values(%s,%s,%s,%f,%f,%f,%f,%s,%s,%s,%s,%s,%f,%f,%f,%f,%f,%s,%s)""" % insert_values

        # execute sql
        insert_result = cur.execute(insert_statement)
        conn.commit()
        print(insert_result)

    # close mysql connection
    cur.close()
    conn.close()

# main
# import by single folder based on the designed date
date = time.strftime("%Y%m%d")
date = "20170705"
dir = "E:\\data\\gz\\" + date
for ps, ds, fs in os.walk(dir):
    for f in fs:
        dbf_file = dir + "\\" + f
        # id = dbf_file[-12:-4]
        filetype = dbf_file[-4:]
        # print(id)
        # print(filetype)
        if filetype == '.dbf':
            dbf_to_mysql_ValuationFile(dbf_file)
