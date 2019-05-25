import requests
import json
# import re
# import ssl
import os
import xmlrpc.client

SavePath = r"C:\xfgcs"
url_basicList = "https://www.zongtongedu.com/Video/basicList"
url_userDetails = "https://www.zongtongedu.com/uc/userDetails"
url_Login = "https://www.zongtongedu.com/Login/login"
url_firstBasic = "https://www.zongtongedu.com/video/firstBasic"
url_GetCouse = "https://www.zongtongedu.com/video/GetCouse"
url_basicInfo = "https://www.zongtongedu.com/video/basicInfo"
url_VideoBasic = "https://www.zongtongedu.com/video/VideoBasic"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
}
RootSavePath = r"F:\消防工程师"

def GetSectionVideoUrl(session, Chapter, Section, CourseInfo, basicInfoData):
    data = {
        "examid": basicInfoData["examid"],
        "courseid": Section["courseid"],
        "vid": Section["vid"]
    }
    # JsonStr = session.post(url_VideoBasic, headers=headers, data=data)
    # resultVideo = JsonStr.json()
    Title = Chapter["title"] + " " + Section["title"]
    Title = Title.replace(" ", "_")
    filename = str(CourseInfo['vtYear']) + "_" + CourseInfo['vtTitle'] + "_" + CourseInfo['classname'] + "_" + Title + ".json"
    VideoListFile = os.path.join(SavePath, filename)
    if not os.path.isfile(VideoListFile):
        JsonStr = session.post(url_VideoBasic, headers=headers, data=data)
        if JsonStr.status_code == 500:
            print(JsonStr.reason)
        else:
            resultVideo = JsonStr.json()
            with open(VideoListFile, 'w') as f:
                json.dump(resultVideo, f, ensure_ascii=False, indent=0)
    else:
        with open(VideoListFile, "r") as f:
            resultVideo = json.load(f)

    VideoInfo = {
        "filename": Title + ".mp4",
        "url": resultVideo['Data']['vUrl']
    }
    CourseInfo["videolist"].append(VideoInfo)
    print(VideoInfo)

def GetCourseVideoUrl(session, CourseInfo, basicInfoData):
    filename = str(CourseInfo['vtYear']) + "_" + CourseInfo['vtTitle'] + "_" + CourseInfo['classname']
    basicInfoFile = os.path.join(SavePath, filename + ".json")
    if not os.path.isfile(basicInfoFile):
        JsonStr = session.post(url_basicInfo, headers=headers, data=basicInfoData)
        if JsonStr.status_code == 500:
            print(JsonStr.reason)
        else:
            basicInfo = JsonStr.json()
            with open(basicInfoFile, 'w') as f:
                json.dump(basicInfo, f, ensure_ascii=False, indent=0)
    else:
        with open(basicInfoFile, "r") as f:
            basicInfo = json.load(f)

    for Chapter in basicInfo['Data']['infoList']:
        if len(Chapter["infoList"]) == 0:
            Section1 = Chapter
            GetSectionVideoUrl(session, Chapter, Section1, CourseInfo, basicInfoData)
        else:
            for Section in Chapter["infoList"]:
                GetSectionVideoUrl(session, Chapter, Section, CourseInfo, basicInfoData)

    # GetVideo(CourseInfo)
    JsonFileName = os.path.join(SavePath, filename + "_VideoList.json")
    with open(JsonFileName, 'w') as f:
        json.dump(CourseInfo, f, ensure_ascii=False, indent=0)


def GetVideo(CourseInfo):
    SavePath = os.path.join(RootSavePath, str(CourseInfo['vtYear']), (CourseInfo['vtTitle'] + '_' + CourseInfo['classname']))
    if not os.path.isdir(SavePath):
        os.makedirs(SavePath)

    with xmlrpc.client.ServerProxy("http://localhost:6800/rpc") as s:
        for filevideo in CourseInfo['videolist']:
            if not os.path.isfile(os.path.join(SavePath, filevideo['filename'])) and filevideo['url'] != '':
                r = s.aria2.addUri([filevideo['url']], {"dir": SavePath, "out": filevideo['filename']})
            pass
    pass

if __name__ == "__main__":

    examid = 12

    with open(os.path.join(SavePath, 'LogInData.json'), "r") as f:
        LogInData = json.load(f)
    session = requests.session()
    session.post(url_Login, data=LogInData)

    firstBasicFile = os.path.join(SavePath, "firstBasic.json")
    if not os.path.isfile(firstBasicFile):
        data = {
            "courseid": 2,
            "examid": examid,
            "year": 0
        }
        JsonStr = session.post(url_firstBasic, headers=headers, data=data)
        if JsonStr.status_code == 500:
            print(JsonStr.reason)
        else:
            firstBasic = JsonStr.json()
            with open(firstBasicFile, 'w') as f:
                json.dump(firstBasic, f, ensure_ascii=False, indent=0)
    else:
        with open(firstBasicFile, "r") as f:
            firstBasic = json.load(f)

    GetCousesFile = os.path.join(SavePath, "GetCouses.json")
    if not os.path.isfile(GetCousesFile):
        data = {
            "examid":examid,
        }
        JsonStr = session.post(url_GetCouse, headers=headers, data=data)
        if JsonStr.status_code == 500:
            print(JsonStr.reason)
        else:
            GetCouses = JsonStr.json()
            with open(GetCousesFile, 'w') as f:
                json.dump(GetCouses, f, ensure_ascii=False, indent=0)
    else:
        with open(GetCousesFile, "r") as f:
            GetCouses = json.load(f)

    for Basic in firstBasic["Data"]:
        if Basic["vtYear"] != 2019:
            for Course in GetCouses["Data"]:
                CourseInfo = {
                    "vtfid":Basic["vtfid"],
                    "vtYear": Basic["vtYear"],
                    "vtTitle": Basic["vtTitle"],
                    "classname": Course["title"],
                    "videolist": []
                }
                data = {
                    "examid": examid,
                    "courseid": Course["courseId"],
                    "vtfid": Basic["vtfid"]
                }
                GetCourseVideoUrl(session, CourseInfo, data)
                pass
        print(Basic)
        pass
# 只能下载2019年的数据