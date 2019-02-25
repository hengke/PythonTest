import urllib.request
import re
import ssl
import os

savepath = "D:\MyHome\Documents\我的小说"
url0 = "http://www.kanshuge.co/files/article/html/17/17211/index.html"
url0 = "https://www.x88dushu.com/xiaoshuo/17/17585/index.html"
if url0.find("index.html") > 0:
    url = url0.replace("index.html","")
    url1 = url0
    pass
else:
    url = url0
    url1 = url + "index.html"
    pass

html_charset = "gbk"
context = ssl._create_unverified_context()
html = urllib.request.urlopen(url1, context = context)
data = html.read()
# result = re.search(r"<meta charset=\"(.*?)\">", data, re.S)
# html_charset = result.group(1)
data = data.decode(encoding=html_charset)

# 书名
result = re.search(r"<div class=\"rt\">.*?<h1>(.*?)</h1>.*?<em>(.*?)</em>.*?</div>", data, re.S)
title = result.group(1)
anthor = result.group(2)
print(title + "。。。。。。开始下载！")

htmlsavepath = os.path.join(savepath, title)

if  not os.path.exists(htmlsavepath) :
    os.makedirs(htmlsavepath)

# 目录
result = re.search(r"<div class=\"mulu\">(.*?)</div>", data, re.S)
chapter = result.group(1)
chapterlist = re.findall(r"<li><a href=\"(.*?)\">(.*?)</a></li>", chapter, re.S)

for chapter in chapterlist:
    htmlfilename = os.path.join(htmlsavepath,  chapter[0])
    if  not os.path.exists(htmlfilename) :
        url1 = url + chapter[0]
        html = urllib.request.urlopen(url1, context = context)
        data = html.read()
        data = data.decode(encoding=html_charset)
        htmlfile = open(htmlfilename, "w", 1, encoding='utf-8')
        htmlfile.write(data)
        htmlfile.close
        print(chapter[0], chapter[1], "  下载完成！")
    else:
        print(chapter[0], chapter[1], "  存在！ 跳过！")
    pass
print("下载完成！")

print("开始合并！")
file = open(os.path.join(savepath,"《" + title + "》" + anthor + ".txt"), "w", 1, encoding='utf-8')

for chapter in chapterlist:
    htmlfile = open(os.path.join(htmlsavepath,  chapter[0]), "r", encoding='utf-8')
    data = htmlfile.read()
    htmlfile.close
    
    file.write(chapter[1].replace("正文 ", ""))
    file.write("\r\n")
    
    lines = re.findall(r"(?:&nbsp;)+(.*?)<", data, re.S)
    if len(lines) != 0:
        if re.search(r"第(.*?)章", lines[0], re.S):
            for i in range(1, len(lines)):
                file.write(lines[i])
                file.write("\r\n")
        else:
            for i in range(0, len(lines)):
                file.write(lines[i])
                file.write("\r\n")

    print(chapter[0], chapter[1])
    pass

file.close()
print("合并完成！")