# -*- coding: UTF-8 -*-

import mysql.connector
from mysql.connector import errorcode

def GetConnect(config):
    try:
        cnx = mysql.connector.connect(**config)
      
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    else:
        return cnx

# 提交的完成操作
def Finish(cnx):
    cnx.commit()
    cnx.close()
def CreateTables(HostConfig, Delete=False):
    cnx = GetConnect(HostConfig)
    print("Host: %s:%d Preparing..." % (cnx._host, cnx._port))
    cursor = cnx.cursor()
    
    if Delete == True:
        cursor.execute("DROP TABLE IF EXISTS `waterday_jh_count`;")
        cursor.execute("DROP TABLE IF EXISTS `oilday_jh_count`;")
        cursor.execute("DROP TABLE IF EXISTS `watermonth_jh_count`;")
        cursor.execute("DROP TABLE IF EXISTS `oilmonth_jh_count`;")
        cursor.execute("DROP TABLE IF EXISTS `rowscounydifferent`;")
        
    SQL = "CREATE TABLE IF NOT EXISTS `waterday_jh_count` (\
            `JH` varchar(50) NOT NULL,\
            `COUNT` int(10) DEFAULT '0'\
            ) ENGINE=MyISAM DEFAULT CHARSET=gbk;"
    cursor.execute(SQL)
    
    SQL = "CREATE TABLE IF NOT EXISTS  `oilday_jh_count` (\
            `JH` VARCHAR(50) NOT NULL,\
            `COUNT` INT(10) NULL DEFAULT '0')\
            COLLATE='gbk_chinese_ci'\
            ENGINE=MyISAM;"
    cursor.execute(SQL)
    

    SQL = "CREATE TABLE IF NOT EXISTS  `watermonth_jh_count` (\
            `JH` VARCHAR(50) NOT NULL,\
            `COUNT` INT(10) NULL DEFAULT '0')\
            COLLATE='gbk_chinese_ci'\
            ENGINE=MyISAM;"
    cursor.execute(SQL)
    
    SQL = "CREATE TABLE IF NOT EXISTS  `oilmonth_jh_count` (\
            `JH` VARCHAR(50) NOT NULL,\
            `COUNT` INT(10) NULL DEFAULT '0')\
            COLLATE='gbk_chinese_ci'\
            ENGINE=MyISAM;"
    cursor.execute(SQL)
    
    SQL = "CREATE TABLE IF NOT EXISTS  `rowscounydifferent` (\
            `TableName` VARCHAR(50) NOT NULL,\
            `JH` VARCHAR(50) NOT NULL,\
            `MySQLCount` INT(11) NULL DEFAULT NULL,\
            `MariaDBCount` INT(11) NULL DEFAULT NULL,\
            PRIMARY KEY (`TableName`, `JH`))\
            COLLATE='gbk_chinese_ci'\
            ENGINE=MyISAM;"
    cursor.execute(SQL)
    print("Host: %s:%d Prepared!" % (cnx._host, cnx._port))

    if cursor:
        cursor.close()
    if cnx:
        Finish(cnx)
    
def DoSum(HostConfig,WellCountTableName,DataTableName):
    cnx = GetConnect(HostConfig)
    if cnx == None:
        exit(1)

    cursor = cnx.cursor()
    query = "SELECT JH FROM %s" % WellCountTableName
    cursor.execute(query)
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            jh = row[0]
            query = "SELECT COUNT(*) FROM %s WHERE JH = '%s'" % (DataTableName,jh)
            cursor.execute(query)
            
            data = cursor.fetchone()
            count = data[0]
            
            query = "UPDATE %s SET COUNT = %d WHERE JH = '%s'" % (WellCountTableName,count,jh)
            cursor.execute(query)
#             print(count,jh)

        print("HOST：%s:%d 表：%s 更新%d条记录！" % (cnx._host, cnx._port, WellCountTableName, len(rows)))
        
    if cursor:
        cursor.close()
    if cnx:
        Finish(cnx)
def DoCountCompare(HostConfig1,HostConfig2,WellCountTableName,DataTableName):
    cnx1 = GetConnect(HostConfig1)
    cnx2 = GetConnect(HostConfig2)
    cursor1 = cnx1.cursor()
    cursor2 = cnx2.cursor()
    query = "SELECT JH FROM %s" % WellCountTableName
    cursor1.execute(query)
    cursor2.execute(query)
    rows1 = cursor1.fetchall()
    rows2 = cursor2.fetchall()
    rows =  list(set(rows1+rows2))
    i = 0
    for row in rows:
        jh = row[0]
        query = "SELECT COUNT FROM %s WHERE JH = '%s'" % (WellCountTableName, jh)
        cursor1.execute(query)
        data = cursor1.fetchall()
        if len(data) != 0:
            count1 = data[0][0]
        else:
            count1 = 0
            
        cursor2.execute(query)
        data = cursor2.fetchall()
        if len(data) != 0:
            count2 = data[0][0]
        else:
            count2 = 0
        if count1 != count2:
            query = "REPLACE INTO rowscounydifferent (TableName,JH,MariaDBCount,MySQLCount)\
                    VALUES ('%s','%s',%d,%d)" % (DataTableName, jh, count1, count2)
            cursor1.execute(query)
            i = i + 1
    print("Host: %s:%d REPLACE INTO rowscounydifferent: %d 条记录！" % (cnx1._host, cnx1._port, i))

    if cursor1:
        cursor1.close()
    if cnx1:
        Finish(cnx1)
    if cursor2:
        cursor2.close()
    if cnx2:
        Finish(cnx2)
def CountWellName(HostConfig):
    cnx = GetConnect(HostConfig)
    print("Host: %s:%d CountWellName..." % (cnx._host, cnx._port))
    cursor = cnx.cursor()
    
    cursor.execute("INSERT INTO waterday_jh_count (JH) SELECT JH FROM table_injectionwaterwelldaydata GROUP BY JH;")
    cursor.execute("INSERT INTO oilday_jh_count (JH) SELECT JH FROM table_oilwelldaydata GROUP BY JH;")
    cursor.execute("INSERT INTO watermonth_jh_count (JH) SELECT JH FROM table_injectionwaterwellmonthdata GROUP BY JH;")
    cursor.execute("INSERT INTO oilmonth_jh_count (JH) SELECT JH FROM table_oilwellmonthdata GROUP BY JH;")

    if cursor:
        cursor.close()
    if cnx:
        Finish(cnx)

def DoRowsCompare(HostConfig1,HostConfig2):
    cnx1 = GetConnect(HostConfig1)
    cnx2 = GetConnect(HostConfig2)
    cursor1 = cnx1.cursor()
    cursor2 = cnx2.cursor()
    query = "SELECT TableName,JH FROM rowscounydifferent"
    cursor1.execute(query)
    rows = cursor1.fetchall()
    for row in rows:
        TableName = row[0]
        JH = row[1]
        if TableName.find("month") > 0:
            query = "SELECT NY FROM %s WHERE JH = '%s'" % (TableName, JH)
        else:
            query = "SELECT RQ FROM %s WHERE JH = '%s'" % (TableName, JH)
        cursor1.execute(query)
        cursor2.execute(query)
        rows1 = cursor1.fetchall()
        rows2 = cursor2.fetchall()
        rows3 =  list(set(rows1) ^ set(rows2))
        print(JH,len(rows3))
        for row3 in rows3:
            print(JH,str(row3))
        #缺少2013-12-10采油井日数据，林1日、月数据
#     print("Host: %s:%d REPLACE INTO rowscounydifferent: %d 条记录！" % (cnx1._host, cnx1._port, i))

    if cursor1:
        cursor1.close()
    if cnx1:
        Finish(cnx1)
    if cursor2:
        cursor2.close()
    if cnx2:
        Finish(cnx2)

config1 = {
  'user': 'hengke',
  'password': 'zhhkhengke',
  'host': '127.0.0.1',
  'port': '3306',
  'database': 'kaifadata',
  'charset':'utf8',
#   'raise_on_warnings': True,
}
config2 = {
  'user': 'hengke',
  'password': 'zhhkhengke',
  'host': '127.0.0.1',
  'port': '3307',
  'database': 'kaifadata',
  'charset':'utf8',
#   'raise_on_warnings': True,
}
TableNames = [
    ['waterday_jh_count', 'table_injectionwaterwelldaydata'],
    ['watermonth_jh_count', 'table_injectionwaterwellmonthdata'],
    ['oilday_jh_count', 'table_oilwelldaydata'],
    ['oilmonth_jh_count', 'table_oilwellmonthdata'],
]

print("\nStart!")

DeleteTables = False
if DeleteTables == True:
    CreateTables(config1, DeleteTables)
    CountWellName(config1)
    for TableName in TableNames:
        DoSum(config1, TableName[0], TableName[1])
        
if DeleteTables == True:
    CreateTables(config2, DeleteTables)
    CountWellName(config2)
    for TableName in TableNames:
        DoSum(config2, TableName[0], TableName[1])

# for TableName in TableNames:
#     DoCountCompare(config1, config2, TableName[0], TableName[1])
DoRowsCompare(config1, config2)

print("End!")
