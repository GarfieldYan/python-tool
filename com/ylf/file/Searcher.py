'''
Created on Oct 18, 2017

@author: e589831
'''

import os

def searchFile(path, fileName):
    for dirName, _folderList, fileList in os.walk(path):
        for fileNameInList in fileList:
            if fileName in fileNameInList:
                print dirName+'\\'+fileNameInList


if __name__ == '__main__':
    searchFile(r'C:\test\unzip', 'ACMFramework')