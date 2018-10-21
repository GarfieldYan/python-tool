# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import os


'''
在指定目录中查找文件名中包含目标字符的文件和文件夹，返回符合的文件名和文件夹名列表
'''
def findFile(folder, strToFind, includeDir=False):
    foundFiles = []
    foundDirs = []
    strToFind = strToFind.encode('utf8')
    for dirpath, dirnames, filenames in os.walk(unicode(folder, "utf8")):
        for fileName in filenames:
            if fileName.find(strToFind) != -1:
                foundFiles.append(os.path.join(dirpath, fileName))
        if includeDir:
            for dirName in dirnames:
                if dirName.find(strToFind) != -1:
                    foundDirs.append(os.path.join(dirpath, dirName))
    return foundFiles + foundDirs

'''
在指定目录中遍历所有子文件，在子文件内容中查找目标字符串，返回符合的文件名列表, 默认只查找txt文件
'''
def findContent(folder, strToFind, fileTypes=['.txt']):
    foundFiles = []
    strToFind = strToFind.encode('utf8')
    for dirpath, dirnames, filenames in os.walk(unicode(folder, "utf8")):  # @UnusedVariable
        for fileName in filenames:
            inFileTypes = False
            for fileType in fileTypes:
                if fileName.find(fileType.encode('utf8')) != -1:
                    inFileTypes = True
                    break
            if inFileTypes:
                with open(os.path.join(dirpath, fileName)) as f:
                    for line in f.readlines():
                        if line.find(strToFind) != -1:
                            foundFiles.append(os.path.join(dirpath, fileName))
                            break
    return foundFiles