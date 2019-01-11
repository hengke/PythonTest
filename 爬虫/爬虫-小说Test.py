import urllib.request
import ssl
import os

context = ssl._create_unverified_context()
htmlsavepath = "D:\MyHome\Documents\我的小说\黑暗血时代"
url1 = "http://www.kanshuge.co/files/article/html/14/14930/7044899.html"
html = urllib.request.urlopen(url1, context = context)
print(html)
data = html.read()
print(data)
data = data.decode(encoding="gb18030")
print(data)
htmlfile = open(os.path.join(htmlsavepath, "7044181.html"), "w", 1, encoding='utf-8')
htmlfile.write(data)
htmlfile.close
print("7044181.html" + "。。。。。。下载完成！")
