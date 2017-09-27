'''
Created on Jul 17, 2017

@author: e589831
'''

import os

folder1 = r"C:\Users\e589831\Desktop\ssrp_97"
folder2 = r"C:\Users\e589831\Desktop\ssrp_98"

def scanFolder(mainFolder, toBeComparedFolder):
    onlyInMainFolderFiles = []
    differenctFiles = []
    for dirName, _, fileList in os.walk(mainFolder):
        for fname in fileList:
            fullNameInMainFolder = dirName+"\\"+fname
            fullNameInToBeComparedFolder = dirName.replace(mainFolder, toBeComparedFolder)+"\\"+fname
            if os.path.exists(fullNameInToBeComparedFolder):
                if os.path.getsize(fullNameInMainFolder) != os.path.getsize(fullNameInToBeComparedFolder):
                    differenctFiles.append(fullNameInMainFolder)
            else:
                onlyInMainFolderFiles.append(fullNameInMainFolder)
    return (onlyInMainFolderFiles, differenctFiles)

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