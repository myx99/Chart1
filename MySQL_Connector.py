import pymysql
from dbfread import DBF

# set mysql connection
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Matao_2012', db='test')
cur = conn.cursor()

# load dbf and insert to db
dbf_file = "D:\\data\\valuation\\20170222\\GZFB0002.dbf"
table = DBF(filename=dbf_file, load=True, encoding="gb2312")
for row in table.records:
    temp_row_list = []
    for key in row:
        # temp_row_list.append(row.get(key).decode('gb2312'))
        if not (type(row.get(key)) is type(0.0)):
            value = (str(row.get(key)))
        else:
            value = row.get(key)
        temp_row_list.append(value)
    # temp_row_list.append(row.get('FfDate'))
    # temp_row_list.append(unicode(row.get('A0')), "gbk2312")
    # temp_row_list.append(row.get('A1'))
    # temp_row_list.append(row.get('A2'))
    # temp_row_list.append(row.get('A3'))
    # temp_row_list.append(row.get('A4'))
    # temp_row_list.append(row.get('A5'))
    # temp_row_list.append(row.get('A6'))
    # temp_row_list.append(row.get('A7'))
    # temp_row_list.append(row.get('A8'))
    # temp_row_list.append(row.get('A9'))
    # temp_row_list.append(row.get('A10'))
    # temp_row_list.append(row.get('A11'))
    # temp_row_list.append(row.get('A12'))
    # temp_row_list.append(row.get('A13'))
    # temp_row_list.append(row.get('A14'))
    # temp_row_list.append(row.get('A15'))
    # temp_row_list.append(row.get('L_SFQR'))

    print(temp_row_list)
    print(tuple(temp_row_list))
    insert_statement = "insert into Valuation values(%s,%s,%s,%f,%f,%f,%f,\'%s\',%s,%s,%s,%s,%f,%f,%f,%f,%f,%s)" % tuple(temp_row_list)
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

