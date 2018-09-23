# coding = utf-8
import xlsxwriter

workbook = xlsxwriter.Workbook("2.xlsx")
worksheet = workbook.add_worksheet("sheet1")
bold = workbook.add_format({"bold":True})
worksheet.write("D4", "Tangshan", bold)

#插入公式，求和
worksheet.write("A3", 2, bold)
worksheet.write("A4", 60, bold)
worksheet.write("A5", "=sum(A3:A4)", bold)

workbook.close()