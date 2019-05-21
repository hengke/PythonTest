import requests
import json
# import re
# import ssl
# import os

if __name__ == "__main__":
    url_VideoBasic = "https://www.zongtongedu.com/video/VideoBasic"
    url_basicInfo = "https://www.zongtongedu.com/video/basicInfo"
    url_basicList = "https://www.zongtongedu.com/Video/basicList"
    # cookies = {
    #     "ASP.NET_SessionId": "4qtjjehksqmxx1l4xolrxd5x",
    #     "p_h5_u":"14CE65DC-11D8-4374-83E2-0964D51A19C9",
    #     "selectedStreamLevel": "SD",
    #     "uToKen":"480a644e33feea6dcff6685eb2eee7ef"
    # }

    # 教材精讲班
    data = {
        "examid":12,
        "courseid":3,
        "vtfid":5
    }
    session = requests.session()
    LogInData = {
        "PhoneText":"13111469643",
        "PasswordText":"659061",
        "chkRem":"checked"
    }
    session.post("https://www.zongtongedu.com/Login/login",data = LogInData)
    userDetails = "https://www.zongtongedu.com/uc/userDetails"
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "X-Requested-With": "XMLHttpRequest",
    #     "Connection": "keep-alive",
    #     "path": "/uc/userDetails",
    #     "origin": "https://www.zongtongedu.com",
    #     "referer": "https://www.zongtongedu.com/Uc/Uc"
    # }
    # JsonStr = session.post(userDetails, headers=headers)
    # result = JsonStr.encoding
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
    }
    # JsonStr = session.post(url_basicInfo, headers=headers, data=data, cookies=cookies)
    JsonStr = session.post(url_basicInfo, headers=headers, data=data)
    result = JsonStr.json()

    ClassInfo =  {
        "vtfid":5,
        "vtYear": 2018,
        "vtTitle": "教材精讲班",
        "classname": "技术综合能力",
        "videolist": []
    }
    Chapters = result['Data']['infoList']
    for Chapter in Chapters:
        Sections = Chapter["infoList"]
        for Section in Sections:
            data = {
                "examid": 12,
                "courseid": Section["courseid"],
                "vid": Section["vid"]
            }
            JsonStr = requests.post(url_VideoBasic, headers=headers, data=data, cookies=cookies)
            resultVideo = JsonStr.json()
            Title = Chapter["title"] + " " + Section["title"]
            VideoInfo = {
                "filename": Title.replace(" ", "_") + ".mp4",
                "url": resultVideo['Data']['vUrl']
            }
            ClassInfo["videolist"].append(VideoInfo)
            print(VideoInfo)
    # JsonFileName = r"F:\消防工程师\2018\教材精讲班_技术综合能力.json"
    JsonFileName = r"C:\教材精讲班_技术综合能力.json"
    with open(JsonFileName, 'w') as f:
        json.dump(ClassInfo, f, ensure_ascii=False, indent=0)
