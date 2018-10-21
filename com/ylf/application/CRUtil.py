# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import os
import com.ylf.file.FileOperation as FileOperation


def replaceVideoNames(vedioFolder, srcStr, replacement):
    for dirpath, _, filenames in os.walk(vedioFolder):
        for filename in filenames:
            if filename.find(srcStr) > -1:
                print os.path.join(dirpath, filename)
                FileOperation.rename(os.path.join(dirpath, filename), os.path.join(dirpath, filename.replace(srcStr, replacement)))

configs = [('/Volumes/Seagate/视频/CR/1. 胖子/1.6 胖子9苍蝇', [('startswithAndContains', ('胖子', '9苍蝇'))]),
               ('/Volumes/Seagate/视频/CR/1. 胖子/1.1 胖子单:双王', [('startswith', '胖子双王'), ('startswith', '胖子王子'), ('startswith', '胖子双苍蝇王子'), ('startswith', '胖子双苍蝇双王')]),
               ('/Volumes/Seagate/视频/CR/1. 胖子/1.2 胖子猎人', [('startswith', '胖子猎人')]),
               ('/Volumes/Seagate/视频/CR/1. 胖子/1.3 胖子火法', [('startswith', '胖子火法')]),
               ('/Volumes/Seagate/视频/CR/1. 胖子/1.4 胖子电法', [('startswith', '胖子电法')]),
               ('/Volumes/Seagate/视频/CR/1. 胖子/1.5 胖子火枪', [('startswith', '胖子火枪')]),
               ('/Volumes/Seagate/视频/CR/1. 胖子/1.7 其它胖子', [('startswith', '胖子')]),
               ('/Volumes/Seagate/视频/CR/2. 三枪/2.3 三枪猎人', [('startswithAndContains', ('三枪', '猎人'))]),
               ('/Volumes/Seagate/视频/CR/2. 三枪/2.1 三枪胖', [('startswith', '三枪胖子攻城槌大苍蝇蝙蝠团伙')]),
               ('/Volumes/Seagate/视频/CR/2. 三枪/2.2 三枪史蒂夫', [('startswith', '三枪冰人攻城槌大苍蝇团伙矿工')]),
               ('/Volumes/Seagate/视频/CR/2. 三枪/2.4 其它三枪', [('startswith', '三枪')]),
               ('/Volumes/Seagate/视频/CR/3. 皮卡/3.1 皮卡槌', [('startswithAndContains', ('皮卡', '槌'))]),
               ('/Volumes/Seagate/视频/CR/3. 皮卡/3.2 皮卡矿', [('startswithAndContains', ('皮卡', '矿'))]),
               ('/Volumes/Seagate/视频/CR/4. 其它/4.1 野猪/4.1.1 快速猪', [('startswith', '快速猪')]),
               ('/Volumes/Seagate/视频/CR/4. 其它/4.1 野猪/4.1.2 屠夫猪', [('startswith', '屠夫猪')]),
               ('/Volumes/Seagate/视频/CR/4. 其它/4.1 野猪/4.1.3 飓风冰法猪', [('startswith', '飓风冰法猪')]),
               ('/Volumes/Seagate/视频/CR/4. 其它/4.2 连弩/4.2.1 电塔弩', [('startswith', '电塔弩')]),
               ('/Volumes/Seagate/视频/CR/4. 其它/4.2 连弩/4.2.2 冰法弩', [('startswith', '冰法弩')]),
               ('/Volumes/Seagate/视频/CR/4. 其它/4.2 连弩/4.2.3 其它弩', [('contains', '弩')])]

'''
supported config types: startswith, contains, startswithAndContains
'''
def processCRVedios(vedioFolder, configs = configs):
    for dirpath, _, filenames in os.walk(vedioFolder):
        for filename in filenames:
            mainVedioName = filename.split('vs')[0]
            processed = False
            for config in configs:
                for item in config[1]:
                    if processed == False and item[0] == 'startswith' and mainVedioName.startswith(item[1]):
                        availableVedioFullName = os.path.join(config[0], getAvailableCRVedioBasename(config[0], filename))
                        print '%s startswith %s, so moved to %s' % (filename, item[1], availableVedioFullName)
                        FileOperation.move(os.path.join(dirpath, filename), availableVedioFullName)
                        processed = True
                    elif processed == False and item[0] == 'contains' and mainVedioName.find(item[1]) > -1:
                        availableVedioFullName = os.path.join(config[0], getAvailableCRVedioBasename(config[0], filename))
                        print '%s contains %s, so moved to %s' % (filename, item[1], availableVedioFullName)
                        FileOperation.move(os.path.join(dirpath, filename), availableVedioFullName)
                        processed = True
                    elif processed == False and item[0] == 'startswithAndContains' and mainVedioName.startswith(item[1][0]) and mainVedioName.find(item[1][1]) > -1:
                        availableVedioFullName = os.path.join(config[0], getAvailableCRVedioBasename(config[0], filename))
                        print '%s startswith %s and contains %s, so moved to %s' % (filename, item[1][0], item[1][1], availableVedioFullName)
                        FileOperation.move(os.path.join(dirpath, filename), availableVedioFullName)
                        processed = True

def getAvailableCRVedioBasename(vedioFolder, vedioBasename):
    count = 0
    for _, _, filenames in os.walk(vedioFolder):
        for filename in filenames:
            if filename.find(os.path.splitext(vedioBasename)[0]) > -1:
                count += 1
    if count > 0:
        return os.path.splitext(vedioBasename)[0] + '.' + str(count + 1) + os.path.splitext(vedioBasename)[1]
    else:
        return vedioBasename


if __name__  == '__main__':
    replaceVideoNames('/Volumes/Seagate/视频/CR', '飓风冰法猪', '冰风猪')
    #processCRVedios('/Users/jerry/Downloads')
                
                