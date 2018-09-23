#coding = utf8
import urllib.request

# 解决中文乱码问题
html01 = urllib.request.quote("https://www.baidu.com/s?wd=%E8%B4%B4%E5%90%A7")
print(html01)

html02 = urllib.request.unquote(html01)
print(html02)

html03 = urllib.request.quote("https://www.baidu.com/s?wd=贴吧")
print(html03)

html04 = urllib.request.unquote(html03)
print(html04)