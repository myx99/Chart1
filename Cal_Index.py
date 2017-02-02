import xlrd as xd

data = xd.open_workbook("C:\\temp\\test.xls")
table = data.sheets()[0]

#display rows and columns
print("Rows of the table: %i" % table.nrows + '\n' + "Columns of the table: %i" % table.ncols)

#Display table
print("The table is as below: ")
for i in range(table.nrows):
    list = ""
    for j in range(table.ncols):
        list += str(table.cell(i,j).value) + "\t"
    print(list)

#Calculate index
temp = 0
for row in range(table.nrows):
    print(table.row(row))
    temp += float(table.row(row)[1].value) * float(table.row(row)[2].value)
print("The total index is %.2f" % temp)

# Calculate weighted_propotion by circulation ratio
def weighted_proportion_method(circulation_ratio):
    if circulation_ratio <= 0.1:
        return circulation_ratio
    elif 0.1 < circulation_ratio <= 0.2:
        return 0.2
    elif 0.2 < circulation_ratio <= 0.3:
        return 0.3
    elif 0.3 < circulation_ratio <= 0.4:
        return 0.4
    elif 0.4 < circulation_ratio <= 0.5:
        return 0.5
    elif 0.5 < circulation_ratio <= 0.6:
        return 0.6
    elif 0.6 < circulation_ratio <= 0.7:
        return 0.7
    elif 0.7 < circulation_ratio <= 0.8:
        return 0.8
    elif 0.8 < circulation_ratio:
        return 1
    else:
        return -1

# Calculate current total adjust market value
def current_adjust_market_value_method(close_price, total_shares, circulation_shares):
    circulation_ratio = float('%.2f' % circulation_shares/total_shares)
    if circulation_ratio <= 0.1:
        return circulation_ratio
    elif 0.1 < circulation_ratio <= 0.2:
        weighted_proportion = circulation_ratio
    elif 0.2 < circulation_ratio <= 0.3:
        weighted_proportion = 0.3
    elif 0.3 < circulation_ratio <= 0.4:
        weighted_proportion = 0.4
    elif 0.4 < circulation_ratio <= 0.5:
        weighted_proportion = 0.5
    elif 0.5 < circulation_ratio <= 0.6:
        weighted_proportion = 0.6
    elif 0.6 < circulation_ratio <= 0.7:
        weighted_proportion = 0.7
    elif 0.7 < circulation_ratio <= 0.8:
        weighted_proportion = 0.8
    elif 0.8 < circulation_ratio:
        weighted_proportion = 1
    else:
        print("Achtung! Wrong Circulation Ratio!")
    current = close_price * total_shares * weighted_proportion