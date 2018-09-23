#coding = utf8
import urllib.request
import re
import ssl

context = ssl._create_unverified_context()
url = "https://www.i4.cn/wper_1_1_0_1.html"
html = urllib.request.urlopen(url, context = context)
data = html.read()
file = open("i4.txt", "wb", 1)
file.write(data)
file.close()
print("网页下载完成！")

# 封装函数，下载图片
def GetUrlImage(info):
    # 创建正则表达式
    # r = r"http[s]://[^\s]*max[^\s]*.(jpg|jpeg|png)"
    r = r"http[s]://[^\s]*max[^\s]*.jpg"
    # 创建匹配模型
    pat = re.compile(r)
    # 匹配数据
    imgs  = re.findall(pat, str(info))

    # 图片命名
    name = 0
    # 循环遍历得到所有图片
    for imgurl in imgs:
        name = name + 1
        urllib.request.urlretrieve(imgurl, "图片/%s.jpg"%name)
        print("完成第%d张！"%name)
        if name > 3:
            break
        #pass 占位符，没有任何含义，保证代码完整性
        pass
    pass

# 调用函数
GetUrlImage(data)
print("下载完成！")