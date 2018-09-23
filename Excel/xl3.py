# coding = utf-8
import xlsxwriter

workbook = xlsxwriter.Workbook("3.xlsx")
worksheet = workbook.add_worksheet("Sheet1")
bold = workbook.add_format({"bold":True})

data = [10, 20, 30, 40, 30, 20, 10, 20, 30, 40, 20, 10]

# 创建图表样式
chart = workbook.add_chart({'type':'radar'})
# column柱状图、area面积图、bar条形图、line折线图、radar雷达图
data1 = [
    [1,2,3,4,5],
    [2,4,6,8,10],
    [3,6,9,12,15],
]
worksheet.write_column('A1',data1[0])
worksheet.write_column('B1',data1[1])
worksheet.write_column('C1',data1[2])

# 配置图表，加入一个或多个数据序列
chart.add_series({'values':'=Sheet1!$A$1:$A$5'})
chart.add_series({'values':'=Sheet1!$B$1:$B$5'})
chart.add_series({'values':'=Sheet1!$C$1:$C$5'})

worksheet.insert_chart('A7', chart)

workbook.close()