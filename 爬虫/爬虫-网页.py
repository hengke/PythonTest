#coding=utf8

# 1、导入库
import urllib.request

# 2、用户验证
import ssl
context = ssl._create_unverified_context()

# 3、获取网页的HTML
url = "https://tieba.baidu.com/index.html"
html = urllib.request.urlopen(url, context=context)

# 4、读取数据
data = html.read()

# 5、打开一个文件，存储数据
file = open("tieba.html", "wb", 1)

# 6、写入文件
file.write(data)

# 7、关闭文件
file.close()

# 8、输出提示
print("当前的网页网址：%s"%html.geturl())
print("下载完成！")

