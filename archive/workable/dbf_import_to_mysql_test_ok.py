import pymysql
from dbfread import DBF

# set mysql connection
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test', use_unicode=True, charset="utf8")
cur = conn.cursor()

# load dbf and insert to db
dbf_file = "D:\\data\\valuation\\20170222\\GZFB0002.dbf"
table = DBF(filename=dbf_file, load=True, encoding="gb2312")
for row in table.records:
    temp_row_list = []

    # filter
    if row.get('A0') == '' or row.get('Ffdate') == '':
        continue
    # use loop to get values, but meet problem if field is none, can't decide if it's String or Float
    for key in row:
        x = row.get(key)
        if not (type(x) is type(0.0)):
            value1 = str(x).encode('utf-8').decode('utf-8')
            value = "'%s'" % value1
        else:
            value = x
        temp_row_list.append(value)

    # replace None with 0.0/0 for float/int field
    def replace_none_value(list, startpoint, endpoint, givenvalue):
        s = int(startpoint)
        if endpoint == 'null':  # single item
            if list[s] ==  "'None'":
                list[s] = givenvalue
            return list
        else:
            e = int(endpoint)
            for i in list[s:e]:  # multiple items
                if i ==  "'None'":
                    list[list.index(i)] = givenvalue
            return list

    row_list = replace_none_value(temp_row_list,3,7,0.0)
    row_list = replace_none_value(temp_row_list,12,17,0.0)
    row_list = replace_none_value(temp_row_list,-1,'null',0)

    # format list to tuple
    insert_values = tuple(row_list)
    print(row_list)
    print(insert_values)
    insert_statement = """insert into Valuation values(%s,%s,%s,%f,%f,%f,%f,%s,%s,%s,%s,%s,%f,%f,%f,%f,%f,%s)""" % insert_values
    insert_result = cur.execute(insert_statement)
    conn.commit()
    print(insert_result)

# check insert result
select_statement = "select * from Valuation"
select_result = cur.execute(select_statement)
conn.commit()
print(select_result)

# close mysql connection
cur.close()
conn.close()

