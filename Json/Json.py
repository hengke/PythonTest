import json
import csv

with open("getA1DataCollectionManage.json", "r", encoding='utf-8') as f:
# with open("1.txt", "r", encoding='gb18030') as f:
    JsonStr = f.read()
    # f.seek(0)
    # bb = json.load(f)    # 与 json.loads(f.read())
    pass

# 替换字符串中的换行
# JsonStr = JsonStr.replace("\\r\\n", "")
# 替换日期中的时间00:00:00部分
# JsonStr = JsonStr.replace(" 00:00:00", "")
# print(JsonStr)
aa = json.loads(JsonStr)  # dict

result = aa["result"]  # list
# result1 = result[0]  # dict
# WELL_ID = result1["WELL_ID"]
# # print(result1)
# print(WELL_ID)

# open函数中encoding参数设为'utf-8'时，文件以'utf-8'编码格式保存文件，Excel打开csv文件中文乱码
# encoding设为'utf_8_sig'，文件以'utf-8-bom'编码格式保存文件，Excel打开csv文件中文正常显示
# encoding设为'gb18030'，文件以'gb18030'编码格式保存文件，Excel打开csv文件中文正常显示
with open('getA1DataCollectionManage.csv', 'w', newline='', encoding='gb18030') as f:
    writer = csv.writer(f)
    writer.writerow(result[0].keys())
    for row in result:
        # print(row.values())
        writer.writerow(row.values())
f.close()
print("转换完成")
