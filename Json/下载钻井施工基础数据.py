# coding=utf8

# 1、导入库
import requests
import csv
import os

if __name__ == "__main__":
    # 下载钻井施工基础数据
    JsonFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\钻井施工基础数据\钻井施工基础数据.json"
    CsvFileName = r"F:\冀东油田数据库应用系统\冀东油田-数据库-提取地址\A1-2.0数据\钻井施工基础数据\钻井施工基础数据.csv"
 
    DillBaseData_Url = "http://10.86.13.221/jsvc/service/epDataService/queryPageByCriteria.json?1=1&entityCode=a1epdm_vSjbzDrZjsgjcsj_V1&where.virtual=false&modeId="
    cookies = {
        "JSESSIONID": "F9CFBF3B0C3925EBCBEFCAD1C9F453FC",
        "loginUrl": "/portal/a1/login.jsp",
        "sec_login": "SEC--n6xwxUsAOc0EjiyWHKikmIcabdFw==|1538275225531",
        "sys": "a1"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"
    }
    data = {
        "where.squeryId": "",
        "where.0": 1,
        "page": 1,
        "rows": 100
    }
    JsonStr = requests.post(DillBaseData_Url, headers=headers, data=data, cookies=cookies)
    result = JsonStr.json()
    print("Page %d/%d" % (data["page"], result['result']['totalPages']))
    if result["success"] is True:
        bb = result
        while bb["result"]["lastPage"] is False:
            data["page"] += 1
            JsonStr = requests.post(DillBaseData_Url, headers=headers, data=data, cookies=cookies)
            bb = JsonStr.json()
            print("Page %d/%d" % (data["page"], result['result']['totalPages']))
            if bb["success"] is True:
                result["result"]["content"] += bb["result"]["content"]
            pass
    content = result["result"]["content"]
    file = open(JsonFileName, "w", 1)
    # 6、写入文件
    file.write(str(result))
    # 7、关闭文件
    file.close()
    print("下载完成！")
    # open函数中encoding参数设为'utf-8'时，文件以'utf-8'编码格式保存文件，Excel打开csv文件中文乱码
    # encoding设为'utf_8_sig'，文件以'utf-8-bom'编码格式保存文件，Excel打开csv文件中文正常显示
    # encoding设为'gb18030'，文件以'gb18030'编码格式保存文件，Excel打开csv文件中文正常显示
    with open(CsvFileName, 'w', newline='', encoding='gb18030') as f:
        writer = csv.writer(f)
        writer.writerow(content[0].keys())
        for row in content:
            # print(row.values())
            writer.writerow(row.values())
    f.close()
    print("转换完成")
