import pandas as pd


df = pd.read_excel('C:/Users/taoma/Documents/行研/echarts/test1.xlsx')
print(df)

columns = df.columns
index = df.index

columns_count = len(columns)
index_count = len(index)

# print(columns_count, columns, index_count, index)

array = []
array_origin = []
for i in range(index_count):
    for j in range(columns_count):
        cell_origin = df.iloc[i, j]
        cell_reform = cell_origin.astype(float) / 700
        cell_result = '%.0f' % cell_reform
        cell1 = [i, j, cell_result]
        cell2 = [i, j, cell_origin]
        array.append(cell1)
        array_origin.append(cell2)
print('array reformed: '+ '\n', array)
print('array origin: '+ '\n', array_origin)
print('columns: '+ '\n', columns)
print('index: '+ '\n', index)