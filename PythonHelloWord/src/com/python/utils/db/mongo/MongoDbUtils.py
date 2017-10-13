#coding=utf-8  
'''
Created on 2017年6月2日

@author: 余国云
'''
import pymongo
from com.python.utils.config import applicatConfig

'''
获取数据库连接
'''
def getConnection():
    host = applicatConfig.getConfig("mysql_db", "mysql_db_host")
    name = applicatConfig.getConfig("mysql_db", "mysql_db_user")
    pwd = applicatConfig.getConfig("mysql_db", "mysql_db_passwd")
    db = applicatConfig.getConfig("mysql_db", "mysql_db_name")
    port = applicatConfig.getConfig("mysql_db", "mysql_db_port")
    charset = applicatConfig.getConfig("mysql_db", "mysql_db_ecoding")
    return MySQLdb.Connect(host,name,pwd,db,int(port),charset=charset);

'''
根据sql查询所有数据
'''
def find(sql,isSingle = False):
    if sql:
        #获得数据库连接
        dbConnection = getConnection(); 
        
        try:
            #获取游标
            cursor = dbConnection.cursor();
            
            #执行查询
            cursor.execute(sql);
            
            #获取结果集
            if isSingle:
                result  = cursor.fetchone()
            else:
                result  = cursor.fetchall()
            
            #关闭数据库连接
            dbConnection.close()
            
            #返回结果集
            return result
        except:
            print ("find all exception,please checkout your sql or other reason")
            return []
        else:
            print ("query all successful")
    else:
        print ("query sql is empty")
        return []

'''
插入数据
'''
def insert(sql):
    if sql:
        #获得数据库连接
        dbConnection = getConnection();  
        
        try:
            #获取游标
            cursor = dbConnection.cursor();
            
            #执行查询
            cursor.execute(sql);
            
            #提交事务
            dbConnection.commit()
            
            #关闭数据库连接
            dbConnection.close()
            
            #返回结果集
            return True
        except:
            dbConnection.rollback()
            print ("find all exception,please checkout your sql or other reason")
            return False
        else:
            print ("query all successful")
    else:
        print ("query sql is empty")
        return False

