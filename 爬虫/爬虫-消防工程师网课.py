import requests
import json
# import re
# import ssl
# import os

def GetCourseVideoUrl(headers, CourseInfo, basicInfoData, VideoBasicData)
    url_basicInfo = "https://www.zongtongedu.com/video/basicInfo"
    url_VideoBasic = "https://www.zongtongedu.com/video/VideoBasic"

    JsonStr = session.post(url_basicInfo, headers=headers, data=basicInfoData)
    basicInfo = JsonStr.json()

    Chapters = basicInfo['Data']['infoList']
    for Chapter in Chapters:
        Sections = Chapter["infoList"]
        for Section in Sections:
            data = {
                "examid": 12,
                "courseid": Section["courseid"],
                "vid": Section["vid"]
            }
            JsonStr = session.post(url_VideoBasic, headers=headers, data=VideoBasicData)
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


if __name__ == "__main__":

    url_basicList = "https://www.zongtongedu.com/Video/basicList"
    url_userDetails = "https://www.zongtongedu.com/uc/userDetails"
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

    with open(r'F:\消防工程师\LogInData.json', "r") as f:
        LogInData = json.load(f)

    session = requests.session()

    url_Login = "https://www.zongtongedu.com/Login/login"
    session.post(url_Login,data = LogInData)

    data = {
        "examid":12,
        "year":0
    }
    url_firstBasic = "https://www.zongtongedu.com/video/firstBasic"
    JsonStr = session.post(url_firstBasic, headers=headers, data=data)
    firstBasic = JsonStr.json()
    with open(r'C:\firstBasic.json', 'w') as f:
        json.dump(firstBasic, f, ensure_ascii=False, indent=0)

    url_GetCouse = "https://www.zongtongedu.com/video/GetCouse"
    JsonStr = session.post(url_firstBasic, headers=headers, data={"examid":12})
    GetCouses = JsonStr.json()
    with open(r'C:\GetCouses.json', 'w') as f:
        json.dump(GetCouses, f, ensure_ascii=False, indent=0)

    CourseInfo = {
        "vtfid":5,
        "vtYear": 2018,
        "vtTitle": "教材精讲班",
        "classname": "技术综合能力",
        "videolist": []
    }
    data = {
        "examid": 12,
        "courseid": 3,
        "vtfid": 5
    }

