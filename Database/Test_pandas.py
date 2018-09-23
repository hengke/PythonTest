# -*- coding: UTF-8 -*-

import os
import urllib.parse
import urllib.request
from urllib.error import URLError, HTTPError
# import psycopg2
import pandas as pd
from sqlalchemy import create_engine


### 下载HTML到指定文件
def DownHtmlToFile(url,filename):
    url = urllib.parse.quote(url, ',\'?/:=&' , encoding='gb2312') #空格是需要转化的，不能设置在safe参数中
    try:
        print("Start Get Html!")
        response = urllib.request.urlopen(url)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print("Get Html Good!")

    html = response.read().decode("gbk")

    f = open(filename, 'w')
    f.write(html)
    f.close()
    print("Write File Ok!")

if __name__ == "__main__":
    # url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
    date = '20000101'
    url1 = """http://10.86.10.111/kf/kfsjk/query/check.asp?a1=select TCRQ,
    JH,RQ,SCSJ,ZSFS,GXYL,YY,TY,FZYL,HGYL,JKHT,JKZZ,RPZSL,RZSL,ZRYL,ZJHWFZL,RZGFL,
    ZRYND,ZRYND1,PZCDS,YLL,BZDM,BZ from V_DBA02&a2= where RQ='
    """
    url2 = """'&a3=投产日期,井号,日期,生产时间,注水方式,
    干线压力,油压,套压,阀组压力,汇管压力,井口含铁,井口杂质,日配注水量,日注水量,注入液量,注聚合物分子量,
    注干粉量,注入液浓度,注入液粘度,配注层段数,溢流量,备注代码,备注&a4=23&a5=注水井日数据&a6=V_DBA02
    """
    url = url1 + date + url2
    filename = "D:\\" + date + ".htm"
    if os.path.exists(filename) is False:
        DownHtmlToFile(url, filename)
    #dfs = pd.read_html(url, flavor=['lxml', 'bs4'])
    with open(filename, 'r') as f:
       # dfs = pd.read_html(f.read(), header=None, index_col=None)
       # header=0表示第一行为列标题
       dfs = pd.read_html(f.read(), header=0, flavor='bs4', converters={'注水方式':str, '备注代码':str})
    data = dfs[0]
    # 不显示行号、显示列名
    # data.to_csv("D:\\" + date + ".csv", header=True, index=False)

    new_labels = ['TCRQ','JH','RQ','SCSJ','ZSFS','GXYL','YY','TY','FZYL','HGYL','JKHT','JKZZ','RPZSL','RZSL','ZRYL','ZJHWFZL','RZGFL','ZRYND','ZRYND1','PZCDS','YLL','BZDM','BZ']
    data.columns = new_labels
    # data.reindex_axis(new_labels, axis='columns')
    # data.reindex_axis(new_labels, axis=1)
    dsn = 'postgresql://postgres:zhhkhengke@localhost:5432/postgres'
    # conn = psycopg2.connect(dsn)
    # cur = conn.cursor()
    # cur.execute("")
    # print(cur.statusmessage)
    # print(conn.notices)
    # pd.io.sql.to_sql(data[1:],'table_injectionwaterwelldaydata', conn, schema='public', if_exists='replace', index=False, index_label=None, chunksize=1000)

    # engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
    # engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')
    # engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname')
    # engine = create_engine('mssql+pyodbc://mydsn')
    # # sqlite://<nohostname>/<path>
    # # where <path> is relative:
    # engine = create_engine('sqlite:///foo.db')
    # # or absolute, starting with a slash:
    # engine = create_engine('sqlite:////absolute/path/to/foo.db')

    engine = create_engine(dsn)
    data.to_sql('table_injectionwaterwelldaydata', engine, schema='public', if_exists='append', index=None, chunksize=1000)
    # pd.io.sql.to_sql(data,'table_injectionwaterwelldaydata', engine, schema='public', if_exists='append', index=None, chunksize=1000)
    # SELECT * FROM public.table_injectionwaterwelldaydata WHERE  "JH" = 'N80-1';
    print(data[2:3]) # 第1行
    # print(data[0:1]) # 第1行
    # print(data.head(1)) # 第1行
    # print(data.head()) # 前5行
    # print(data.iloc[0]) # 第1行
    # print(data.ix[1]) # 第2行
    # print(data.ix[1:3]) # 第2-4行
    # print(data.iloc[0:1]) # 第1行
    # print(data[0]) # 第1列
    # print(data[1]) # 第2列
    # print(data.iloc[0][0]) # 第1行第1列,=cell(0,0)
    # print(data.columns)
