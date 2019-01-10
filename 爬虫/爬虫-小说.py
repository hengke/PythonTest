import urllib.request
import re
import ssl

context = ssl._create_unverified_context()

url = "http://www.kanshuge.co/files/article/html/131/131811/"
url1 = url + "index.html"
html = urllib.request.urlopen(url1, context = context)
data = html.read()
data = data.decode(encoding="gbk")

result = re.search(r"<div class=\"btitle\">.*?<h1>(.*?)</h1>.*?<em>(.*?)</em>.*?</div>", data, re.S)
title = result.group(1)
anthor = result.group(2)
print(title + "：开始下载")

results = re.findall(r"<dd><a href=\"(.*?)\">(.*?)</a></dd>", data, re.S)
file = open("《" + title + "》" + anthor + ".txt", "w", 1)
for result in results:
    url1 = url + result[0]
    html = urllib.request.urlopen(url1, context = context)
    data = html.read()
    data = data.decode(encoding="gbk")
    results1 = re.findall(r"(?:&nbsp;)+(.*?)<", data, re.S)
    for line in results1:
        file.write(line)
        file.writelines()
        file.write("\r\n")
        pass
    print(result[1] + "：下载完成！")
    pass
file.close()
print(result[1] + "：下载完成！")