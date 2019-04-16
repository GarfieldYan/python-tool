# -*- coding: utf8 -*-
import os
 
def getDiffFiles(dirpath1, dirpath2):
    result = []
    diffInDir1AndDir2Files = []
    onlyInDir1Files = []
    onlyInDir2Files = []
    for folder, _, filenames in os.walk(dirpath1):
        for filename in filenames:
            fullFilenameForDir1 = os.path.join(folder, filename)
            fullFilenameForDir2 = os.path.join(folder.replace(dirpath1, dirpath2), filename)
            if os.path.isfile(fullFilenameForDir2):
                if os.stat(fullFilenameForDir1).st_size != os.stat(fullFilenameForDir2).st_size:
                    diffInDir1AndDir2Files.append(fullFilenameForDir1.replace(dirpath1, ''))
            else:
                onlyInDir1Files.append(fullFilenameForDir1)
    for folder, _, filenames in os.walk(dirpath2):
        for filename in filenames:
            fullFilenameForDir2 = os.path.join(folder, filename)
            fullFilenameForDir1 = os.path.join(folder.replace(dirpath2, dirpath1), filename)
            if not os.path.isfile(fullFilenameForDir1):
                onlyInDir2Files.append(fullFilenameForDir2)
    result.append(diffInDir1AndDir2Files)
    result.append(onlyInDir1Files)
    result.append(onlyInDir2Files)
    return result
 
 
if __name__ == '__main__':
 
    dirpath1 = '/Users/jerry/Downloads/jartest/lingfeng/jishu'
    dirpath2 = '/Users/jerry/Downloads/jartest/shaoben/jishu'
 
    result = getDiffFiles(dirpath1, dirpath2)
 
    if len(result[0]) > 0:
        print 'different files:'
        for diffFile in result[0]:
            print diffFile
 
    if len(result[1]) > 0:
        print '\nonly in %s:' % dirpath1
        for dir1File in result[1]:
            print dir1File
 
    if len(result[2]) > 0:
        print '\nonly in %s:' % dirpath2
        for dir2File in result[2]:
            print dir2File