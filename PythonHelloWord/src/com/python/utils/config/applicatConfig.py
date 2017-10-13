#coding=utf-8
'''
Created on 2017年6月2日

@author: MuR
'''
import ConfigParser
import os

def getConfig(typeCode,keyCode):
    if typeCode and keyCode:
        #创建配置文件转换
        cf = ConfigParser.ConfigParser()
        #读取配置文件
        curentPath = os.getcwd()
        cf.read(curentPath.split("src")[0]+"src/com/python/utils/config/application.conf")
        return cf.get(typeCode, keyCode)
    else:
        return