from pandas import read_excel

data = read_excel('整理后数据.xlsx', index_col = 0)
data['总工程量']=data['工程数量']*data['户数']
data.groupby(['项目名称','户型']).sum().to_csv('1.csv')
data.groupby(['项目名称'])['总工程量'].sum().to_csv('2.csv')