import urllib.request
import re
import ssl
import os
import sys
import io

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')         #改变标准输出的默认编码

savepath = "D:\MyHome\Documents\我的小说"
url0 = "http://www.kanshuge.co/files/article/html/14/14930/"
if url0.find("index.html") > 0:
    url = url0.replace("index.html","")
    url1 = url0
    pass
else:
    url = url0
    url1 = url + "index.html"
    pass

context = ssl._create_unverified_context()
html = urllib.request.urlopen(url1, context = context)
data = html.read()
data = data.decode(encoding="gb18030")

result = re.search(r"<div class=\"btitle\">.*?<h1>(.*?)</h1>.*?<em>(.*?)</em>.*?</div>", data, re.S)
title = result.group(1)
anthor = result.group(2)
print(title + "。。。。。。开始下载")

htmlsavepath = os.path.join(savepath, title)

if  not os.path.exists(htmlsavepath) :
    os.makedirs(htmlsavepath)

results = re.findall(r"<dd><a href=\"(.*?)\">(.*?)</a></dd>", data, re.S)

for result in results:
    url1 = url + result[0]
    html = urllib.request.urlopen(url1, context = context)
    data = html.read()
    data = data.decode(encoding="gb18030")
    htmlfile = open(os.path.join(htmlsavepath,  result[0]), "w", 1, encoding='utf-8')
    htmlfile.write(data)
    htmlfile.close
    print(result[1])
    pass
print("下载完成！")
print("开始合并！")
file = open(os.path.join(savepath,"《" + title + "》" + anthor + ".txt"), "w", 1, encoding='utf-8')

for result in results:
    htmlfile = open(os.path.join(htmlsavepath,  result[0]), "r", encoding='utf-8')
    data = htmlfile.read()
    htmlfile.close
    results1 = re.findall(r"(?:&nbsp;)+(.*?)<", data, re.S)
    for line in results1:
        file.write(line)
        file.write("\r\n")
        pass
    print(result[1])
    pass
file.close()
print("合并完成！")