from bs4 import BeautifulSoup

soup = BeautifulSoup("<html>data</html>","html.parser")
print(soup)

soup = BeautifulSoup("<html>data</html>","lxml")
print(soup)

soup = BeautifulSoup("<html>data</html>","html5lib")
print(soup)

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',"html.parser")
tag = soup.b
print(type(tag))