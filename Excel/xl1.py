# coding = utf-8
import xlsxwriter

# 创建excel文件
work = xlsxwriter.Workbook("1.xlsx")
# 创建表格
worksheet = work.add_worksheet("red")
# 修改内容
# 修改格式
worksheet.set_column("A:B", 20)
# 下标
worksheet.set_column(2, 3, 20)
# 完整样式
worksheet.set_column("D:D", 20, None,{'hidden':0})
# 边框加粗
bold = work.add_format({"bold":True})
# 字符操作
worksheet.write('A1', 'red', bold)
# 图片
worksheet.insert_image("A2", "1.png")
# 保存
work.close()
