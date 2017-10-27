'''
Created on Jul 17, 2017

@author: e589831
'''

import os

folder1 = r"C:\Users\e589831\Desktop\ssrp_125"
folder2 = r"C:\Users\e589831\Desktop\ssrp_129"

def scanFolder(folder1, folder2):
    onlyInFolder1 = []
    diffFiles = []
    for dirName, _, fileList in os.walk(folder1):
        for fname in fileList:
            fullFName1 = dirName + "\\" + fname
            fullFName2 = dirName.replace(folder1, folder2) + "\\" + fname
            if os.path.exists(fullFName2):
                if os.path.getsize(fullFName1) != os.path.getsize(fullFName2):
                    diffFiles.append(fullFName1)
            else:
                onlyInFolder1.append(fullFName1)
    return (onlyInFolder1, diffFiles)

def compareFolders(folder1, folder2):
    result1 = scanFolder(folder1, folder2)
    result2 = scanFolder(folder2, folder1)
    return (result1[0], result2[0], result1[1])

def compareAndPrint():
    result = compareFolders(folder1, folder2)
    if len(result[0]) != 0:
        print "-----OnlyInFolder1Files-----"
        for i in result[0]:
            print i
    
    if len(result[1]) != 0:
        print "-----OnlyInFolder2Files-----"
        for i in result[1]:
            print i
    
    if len(result[2]) != 0:
        print "-----DifferentFiles-----"
        for i in result[2]:
            print i
    
if __name__ == '__main__':
    compareAndPrint()
