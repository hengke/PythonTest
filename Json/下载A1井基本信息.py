# coding=utf8

# 1、导入库
import requests
import json
import csv
import os


def GetA1DataCollectionManage(url, JsonFileName, CsvFileName):
    AllWell_JSON = requests.get(url)
    JsonStr = AllWell_JSON.text
    # 替换字符串中的换行
    JsonStr = JsonStr.replace("\\r\\n", "")
    # 替换日期中的时间00:00:00部分
    JsonStr = JsonStr.replace(" 00:00:00", "")
    
    aa = json.loads(JsonStr)  # 通过JSON模块转化为dict

    # 写入文件
    # ensure_ascii=False 不将字符串转化为ascii输出，解决中文输出问题
    # indent=0 格式化输出参数，可为负数、0、正数、""、"\t"等
    with open(JsonFileName, 'w') as f:
        json.dump(aa, f, ensure_ascii=False, indent=0)
    
    print("当前的网页网址：%s" % AllWell_JSON.url)
    print("下载完成！")

    result = aa["result"]

    # open函数中encoding参数设为'utf-8'时，文件以'utf-8'编码格式保存文件，Excel打开csv文件中文乱码
    # encoding设为'utf_8_sig'，文件以'utf-8-bom'编码格式保存文件，Excel打开csv文件中文正常显示
    # encoding设为'gb18030'，文件以'gb18030'编码格式保存文件，Excel打开csv文件中文正常显示
    with open(CsvFileName, 'w', newline='', encoding='gb18030') as f:
        writer = csv.writer(f)
        writer.writerow(result[0].keys())
        for row in result:
            writer.writerow(row.values())

    print("转换完成")
    pass


if __name__ == "__main__":
    # 下载所有井基本信息
    AllWell_Url = "http://10.86.13.221/jsvc/service/A1_dataStatisBusiness/getA1DataCollectionManage?"
    # AllWell_Url = "http://10.86.13.221/jsvc/service/A1_dataStatisBusiness/getA1DataCollectionManagePage?page=1&rows=5"
    AllWell_JsonFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\getA1DataCollectionManage.json"
    AllWell_CsvFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\getA1DataCollectionManage.csv"
    if os.path.isfile(AllWell_JsonFileName) is False or os.path.isfile(AllWell_CsvFileName) is False:
        GetA1DataCollectionManage(AllWell_Url, AllWell_JsonFileName,AllWell_CsvFileName)

    # 给定wellid参数，下载井的单井卡片
    WellCardData_Url = "http://10.86.13.221/jsvc/service/A1_dataManagement/getWellCardDataByWellId?wellId="
    WellCard_JsonFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\单井卡片\单井卡片.json"
    WellCard_CsvFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\单井卡片\单井卡片.csv"

    with open(AllWell_JsonFileName, 'r', 1) as f:
        AllWell_Json = json.load(f)

    result = {"resultCode": 0, "result": [], "msgId": "", "success": True}
    i = 0
    print("开始下载单井卡片！")
    if os.path.isfile(WellCard_JsonFileName) is False:
        # with open(AllWell_JsonFileName, 'r', 1) as f:
        #     WellCard_Json = json.load(f)
        # f.close()
        # ToDoList = ""

        for row in AllWell_Json["result"]:
            JsonStr = requests.get(WellCardData_Url + row["WELL_ID"])
            bb = JsonStr.json()
            result["result"] += bb["result"]
            print(i, bb["result"][0]["WELL_COMMON_NAME"])
            i += 1
#            if i == 30:
#                break
            pass
        
        str1 = json.dumps(result, ensure_ascii=False)
        str1 = str1.replace("\\r\\n", "")
#        str1 = str1.replace("\\r", "")
#        str1 = str1.replace("\\n", "")
#        str1 = str1.replace("\r\n", "")
#        str1 = str1.replace("\r", "")
#        str1 = str1.replace("\n", "")
        str1 = str1.replace(" 00:00:00", "")
        result = json.loads(str1)

        with open(WellCard_JsonFileName, 'w') as f:
            json.dump(result, f, ensure_ascii=False, indent=0)
#            json.dump(result, f, ensure_ascii=False, indent=0)
            
        print("下载完成！")

    # open函数中encoding参数设为'utf-8'时，文件以'utf-8'编码格式保存文件，Excel打开csv文件中文乱码
    # encoding设为'utf_8_sig'，文件以'utf-8-bom'编码格式保存文件，Excel打开csv文件中文正常显示
    # encoding设为'gb18030'，文件以'gb18030'编码格式保存文件，Excel打开csv文件中文正常显示
    with open(WellCard_CsvFileName, 'w', newline='', encoding='gb18030') as f:
        writer = csv.writer(f)
        writer.writerow(result["result"][0].keys())
        for row in result["result"]:
            # print(row.values())
            writer.writerow(row.values())

    print("转换完成")
