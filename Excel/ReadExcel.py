#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
import xlrd
import xlwings
import xlsxwriter

FileName = r'D:\MyHome\Documents\My RTX Files\zhhk188\4号构造油水井生产情况统计表(新版)2018.6.6-链接.xls'
# data = xlrd.open_workbook(FileName)  # 打开xls文件
# table = data.sheets()[0]  # 打开第一张表
# rows = table.nrows  # 获取表的行数
# for i in range(rows):  # 循环逐行打印
#     if i == 0:  # 跳过第一行
#         continue
#     print(table.row_values(i)[:13])  # 取前十三列

# workbook = xlwings.Book(FileName)
# sheet = workbook.sheets(1)
# print(sheet.name)

workbook = xlsxwriter.Workbook(FileName)
print(workbook.sheetnames)
