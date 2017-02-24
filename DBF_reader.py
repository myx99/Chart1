from dbfread import DBF


# before open the file, need to consider if the file was opened by any other apps
# can add "try.....catch" method to solve it
dbffile = "D:\\data\\valuation\\20170222\\GZFB0002.dbf"
# for record in DBF(filename=dbffile,encoding='gb2312'):
#     print(record)

table = DBF(filename=dbffile, load=True, encoding="gb2312")
for row in table.records:
    print(row)
    break


# for row in table.records:
#     if row['A4'] > 0:
#         print(row)