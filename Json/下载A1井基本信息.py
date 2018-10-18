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
    # 5、打开一个文件，存储数据
    file = open(JsonFileName, "w", 1)
    # 6、写入文件
    file.write(JsonStr)
    # 7、关闭文件
    file.close()

    print("当前的网页网址：%s" % AllWell_JSON.url)
    print("下载完成！")

    aa = json.loads(JsonStr)  # dict
    result = aa["result"]
    # print(result)
    # result1 = result[0]  # dict
    # WELL_ID = result1["WELL_ID"]
    # print(WELL_ID)

    # open函数中encoding参数设为'utf-8'时，文件以'utf-8'编码格式保存文件，Excel打开csv文件中文乱码
    # encoding设为'utf_8_sig'，文件以'utf-8-bom'编码格式保存文件，Excel打开csv文件中文正常显示
    # encoding设为'gb18030'，文件以'gb18030'编码格式保存文件，Excel打开csv文件中文正常显示
    with open(CsvFileName, 'w', newline='', encoding='gb18030') as f:
        writer = csv.writer(f)
        writer.writerow(result[0].keys())
        for row in result:
            # print(row.values())
            writer.writerow(row.values())
    f.close()
    print("转换完成")
    pass


if __name__ == "__main__":
    # 下载所有井基本信息
    AllWell_Url = "http://10.86.13.221/jsvc/service/A1_dataStatisBusiness/getA1DataCollectionManage?"
    # AllWell_Url = "http://10.86.13.221/jsvc/service/A1_dataStatisBusiness/getA1DataCollectionManagePage?page=1&rows=5"
    AllWell_JsonFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\getA1DataCollectionManage.json"
    AllWell_CsvFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\getA1DataCollectionManage.csv"
    if os.path.isfile(AllWell_JsonFileName) is False or os.path.isfile(
            AllWell_CsvFileName) is False:
        GetA1DataCollectionManage(AllWell_Url, AllWell_JsonFileName,
                                  AllWell_CsvFileName)

    # 给定wellid参数，下载井的单井卡片
    WellCardData_Url = "http://10.86.13.221/jsvc/service/A1_dataManagement/getWellCardDataByWellId?wellId="
    WellCard_JsonFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\单井卡片\单井卡片.json"
    WellCard_CsvFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\单井卡片\单井卡片.csv"
    with open(AllWell_JsonFileName, 'r', 1) as f:
        AllWell_Json = json.load(f)
    f.close()
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
            # str1 = JsonStr.text
            # str1 = str1.replace("\\r\\n", "")
            # str1 = str1.replace(" 00:00:00", "")
            # bb = json.loads(str1)
            bb = JsonStr.json()
            result["result"] += bb["result"]
            print(i, bb["result"][0]["WELL_COMMON_NAME"])
            i += 1
            # if i == 3:
            #     break
            pass
        str1 = str(result)
        str1 = str1.replace("\\r\\n", "")
        str1 = str1.replace("\r\n", "")
        str1 = str1.replace(" 00:00:00", "")
        # A1系统返回的JSON数据格式不标准，无法用json.load()加载，需更正为正确格式
        str1 = str1.replace("'", "\"")
        str1 = str1.replace("None", "null")
        str1 = str1.replace("True", "true")

        f = open(WellCard_JsonFileName, "w", 1)
        f.write(str1)
        f.close()
        print("下载完成！")
    else:
        with open(WellCard_JsonFileName, 'r', 1) as f:
            result = json.load(f)
        f.close()

    # open函数中encoding参数设为'utf-8'时，文件以'utf-8'编码格式保存文件，Excel打开csv文件中文乱码
    # encoding设为'utf_8_sig'，文件以'utf-8-bom'编码格式保存文件，Excel打开csv文件中文正常显示
    # encoding设为'gb18030'，文件以'gb18030'编码格式保存文件，Excel打开csv文件中文正常显示
    with open(WellCard_CsvFileName, 'w', newline='', encoding='gb18030') as f:
        writer = csv.writer(f)
        writer.writerow(result["result"][0].keys())
        for row in result["result"]:
            # print(row.values())
            writer.writerow(row.values())
    f.close()
    print("转换完成")
