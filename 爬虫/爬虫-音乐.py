#coding = utf8
import urllib.request
from bs4 import BeautifulSoup

# 用户验证
import ssl
context = ssl._create_unverified_context()

# 打开地址，读取网页数据
url = "https://www.i4.cn/ring_1_0_1.html"
html = urllib.request.urlopen(url, context=context)
html_doc = html.read()

# 创建一个soup对象，解析器的类型
soup = BeautifulSoup(html_doc, "html.parser")

mp3s = soup.find_all("div", attrs={"title":"播放"})

name = 0
for item in mp3s:
    name = name + 1
    url1 = item.attrs["data-mp3"]
    urllib.request.urlretrieve(url1, "音乐/%s.mp3" % name)
    print("完成第%d首！" % name)
    # if name > 3:
    #     break
    # pass 占位符，没有任何含义，保证代码完整性
    pass