import win32com.client as wc
import os
# 启动Excel应用
excel_app = wc.Dispatch('Excel.Application')
excel_app.Visible = True
# 连接excel
xlsPath = "4.xlsx"
absPath = os.path.abspath(xlsPath)
# print("absPath =", absPath)
# absPath = D:\Home\Documents\PycharmProjects\exle\4.xlsx
workbook = excel_app.Workbooks.Open(absPath)
# 写入数据
workbook.Worksheets('Sheet1').Cells(1,1).Value = 'data'
# 关闭并保存
workbook.SaveAs(os.path.abspath(r"4-1.xlsx"))
excel_app.Application.Quit()