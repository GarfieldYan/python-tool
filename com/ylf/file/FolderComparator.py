'''
Created on Jul 17, 2017

@author: e589831
'''

import os

folder1 = r"C:\Users\e589831\Desktop\tmp\app_700P3"
folder2 = r"C:\Users\e589831\Desktop\tmp\app_702"

OnlyIn1 = []
OnlyIn2 = []
DiffFiles = [] 

for dirName, subdirList, fileList in os.walk(folder1):
    for fname in fileList:
        fullNameIn1 = dirName+"\\"+fname
        fullNameIn2 = dirName.replace(folder1, folder2)+"\\"+fname
        if os.path.exists(fullNameIn2):
            if os.path.getsize(fullNameIn1) != os.path.getsize(fullNameIn2):
                DiffFiles.append(fullNameIn1)
        else:
            OnlyIn1.append(fullNameIn1)

if len(OnlyIn1) != 0:
    print "-----OnlyInFolder1-----"
    for i in OnlyIn1:
        print i

if len(OnlyIn2) != 0:
    print "-----OnlyInFolder2-----"
    for i in OnlyIn2:
        print i

if len(DiffFiles) != 0:
    print "-----DiffFiles-----"
    for i in DiffFiles:
        print i