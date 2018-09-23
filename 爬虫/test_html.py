# -*- coding: UTF-8 -*-

import urllib.request
from bs4 import BeautifulSoup

url = "http://www.w3school.com.cn/tags/html_ref_eventattributes.asp"

try:
    urlfile = urllib.request.urlopen(url)
    html = urlfile.read()
except urllib.error.HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except urllib.error.URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    print("good!")
    soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')
for table in tables:
    rows = table.findAll('tr')
    for row in rows:
#         print(row.text,end='')
        cols = row.findAll('td')
        for col in cols:
            print("%s " % col.text,end='')
        print()

