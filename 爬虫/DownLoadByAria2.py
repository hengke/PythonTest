import json
import xmlrpc.client
import os

GetCousesFile = r"F:\消防工程师\2018\教材精讲班_技术综合能力.json"
RootSavePath = r"F:\消防工程师"
with open(GetCousesFile, "r") as f:
    GetCouses = json.load(f)
SavePath = os.path.join(RootSavePath, GetCouses['vtYear'],GetCouses['vtTitle']+"_"+GetCouses['classname'])
with xmlrpc.client.ServerProxy("http://localhost:6800/rpc") as s:
    # r = s.aria2.getVersion()
    # print(r)
    for filevideo in GetCouses['videolist']:
        r = s.aria2.addUri([filevideo['url']], {"dir": SavePath, "out":filevideo['filename']})
        print(r)
        pass