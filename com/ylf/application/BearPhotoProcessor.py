# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import re
import os
import com.ylf.file.FileOperation as FileOperation
import com.ylf.file.FileUtil as FileUtil


def processBearPhotos(dirpath, movetoDirpath):
    for dirpath, _, filenames in os.walk(dirpath):
        for filename in filenames:
            matchObj = re.match(r'^小熊(.*)', filename)
            if matchObj:
                newFilename = '小熊.' + '[' + FileUtil.getFileCreateTime(os.path.join(dirpath, filename)) + ']' + '.' + matchObj.group(1)
                FileOperation.rename(os.path.join(dirpath, filename), os.path.join(movetoDirpath, newFilename))

if __name__ == '__main__':
    processBearPhotos('/Users/jerry/Downloads', '/Volumes/Seagate/图片/照片/人/小熊')