# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')       # @UndefinedVariable
import os
import time


'''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
def timestampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y%m%d%H%M%S',timeStruct)

'''获取文件的大小,结果保留两位小数，单位为MB'''
def getFileSize(filePath):
    filePath = unicode(filePath, 'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

'''获取文件的访问时间'''
def getFileAccessTime(filePath):
    filePath = unicode(filePath,'utf8')
    t = os.path.getatime(filePath)
    return timestampToTime(t)

'''获取文件的创建时间'''
def getFileModifyTime(filePath):
    filePath = unicode(filePath,'utf8')
    t = os.path.getctime(filePath)
    return timestampToTime(t)

'''获取文件的修改时间'''
def getFileCreateTime(filePath):
    filePath = unicode(filePath,'utf8')
    t = os.path.getmtime(filePath)
    return timestampToTime(t)

'''获取文件所在的文件夹名'''
def getFolderName(filePath):
    filePath = unicode(filePath,'utf8')
    return os.path.basename(os.path.dirname(filePath))
    