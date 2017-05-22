import xlrd as xd
import time
from xlutils.copy import copy

getdate = time.strftime("%Y%m%d")
year = getdate[:4] + u'年'
month = getdate[4:6] + u'月'
day = getdate[-2:] + u'日'
date_in_chinese = year + month + day
# print(date_in_chinese)

# test path
template = "D:\\temp\\reports\\风险管理日报_模板.xls"
# template = "D:\\temp\\reports\\temp.xls"
result = "D:\\temp\\reports\\风险管理日报_%s.xls" % getdate
# print(template, result)

data = xd.open_workbook(template, formatting_info=True)
temp_data = copy(data)
temp_data.get_sheet(0).write(3, 1, date_in_chinese)
temp_data.save(result)
