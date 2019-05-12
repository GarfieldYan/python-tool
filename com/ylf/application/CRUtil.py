# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import os
import com.ylf.file.FileOperation as FileOperation
import com.ylf.file.FileUtil as FileUtil
import re
import random
import time

rules = [   ('/Volumes/Seagate/视频/CR/1. 胖子/1.11 胖子电磁炮', [(('startwith', '胖子'), ('contain', '电磁炮'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.12 胖子墓园', [(('startwith', '胖子'), ('contain', '墓园'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.13 胖子气球', [(('startwith', '胖子'), ('contain', '气球'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.7 胖子九苍', [(('startwith', '胖子'), ('contain', '大苍'), ('contain', '小苍'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.9 双胖', [(('startwith', '胖子'), ('contain', '蓝胖'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.8 胖子女巫:暗巫', [(('startwith', '胖子'), ('contain', '女巫')),
                                                                (('startwith', '胖子'), ('contain', '暗巫'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.5 胖子粉丝', [(('startwith', '胖子'), ('contain', '团伙'), ('contain', '蝙蝠')), 
                                                            (('startwith', '胖子'), ('contain', '茅哥'), ('contain', '团伙')), 
                                                            (('startwith', '胖子'), ('contain', '墓碑吹箭火豆'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.1 胖子双王', [(('startwith', '胖子'), ('contain', '王子'), ('contain', '黑王'), ('notcontain', '矿工')), 
                                                            (('startwith', '胖子'), ('contain', '王子'), ('contain', '幽灵'), ('notcontain', '矿工')),
                                                            (('startwith', '胖子'), ('contain', '王子'), ('contain', '樵夫'), ('notcontain', '矿工')),
                                                            (('startwith', '胖子'), ('contain', '王子'), ('contain', '小皮卡'), ('notcontain', '矿工')),
                                                            (('startwith', '胖子'), ('contain', '小皮卡'), ('contain', '樵夫'), ('notcontain', '矿工')),
                                                            (('startwith', '胖子'), ('contain', '樵夫'), ('contain', '黑王'), ('notcontain', '矿工')),
                                                            (('startwith', '胖子'), ('contain', '樵夫'), ('contain', '幽灵'), ('notcontain', '矿工'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.2 胖子双王矿工', [(('startwith', '胖子'), ('contain', '王子'), ('contain', '黑王'), ('contain', '矿工')), 
                                                                (('startwith', '胖子'), ('contain', '王子'), ('contain', '幽灵'), ('contain', '矿工'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.3 胖子单王矿工', [(('startwith', '胖子'), ('contain', '王子'), ('contain', '矿工'), ('notcontain', '黑王'), ('notcontain', '幽灵')),
                                                                (('startwith', '胖子'), ('contain', '黑王'), ('contain', '矿工'), ('notcontain', '王子'), ('notcontain', '幽灵')),
                                                                (('startwith', '胖子'), ('contain', '小皮卡'), ('contain', '矿工'), ('notcontain', '王子'), ('notcontain', '黑王'), ('notcontain', '幽灵')),
                                                                (('startwith', '胖子'), ('contain', '樵夫'), ('contain', '矿工'), ('notcontain', '王子'), ('notcontain', '黑王'), ('notcontain', '幽灵'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.4 胖子矿工', [(('startwith', '胖子'), ('contain', '矿工'), ('notcontain', '王子'), ('notcontain', '黑王'), ('notcontain', '幽灵'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.6 快速胖', [(('startwith', '胖子'), ('contain', '王子'), ('contain', '冰豆')),
                                                            (('startwith', '胖子'), ('contain', '小皮卡'), ('contain', '冰豆'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.10 其它胖子推进', [(('startwith', '胖子')), (('startwith', '绿胖'))] ),
            ('/Volumes/Seagate/视频/CR/2. 石头', [('startwith', '石头')] ),
            ('/Volumes/Seagate/视频/CR/3. 连弩/3.1 电塔弩/3.1.1 经典电塔弩', [('startwith', '连弩电塔冰人弓箭骷髅冰豆滚木火球')] ),
            ('/Volumes/Seagate/视频/CR/3. 连弩/3.1 电塔弩/3.1.2 其它电塔弩', [(('startwith', '连弩'), ('contain', '电塔'))] ),
            ('/Volumes/Seagate/视频/CR/3. 连弩/3.2 冰法弩/3.2.1 火箭冰法弩', [(('startwith', '连弩'), ('contain', '冰法'), ('contain', '火箭'))] ),
            ('/Volumes/Seagate/视频/CR/3. 连弩/3.2 冰法弩/3.2.2 火球冰法弩', [(('startwith', '连弩'), ('contain', '冰法'), ('contain', '火球'))] ),
            ('/Volumes/Seagate/视频/CR/3. 连弩/3.3 其它弩', [('startwith', '连弩')] )
        ]
                        
""" supported ruleConfigType: startwith, contain """  
def processCRVedios(vedioFolder, rules = rules):
    preProcess(vedioFolder)
    for dirpath, _, filenames in os.walk(vedioFolder):
        for filename in filenames:
            matchObj = re.match(r'^(\W*)vs(\W*).(\[[0-9]{10}\])(\.\w{3})$', filename)
            if not matchObj:
                continue
            leftDeckName = filename.split('vs')[0]
            processed = False
            for rule in rules:
                for ruleConfig in rule[1]:      # ruleConfigs是一个由多个ruleConfig组成的列表，满足其中任意一个ruleConfig元素就符合该rule
                    if isinstance(ruleConfig[0], str):  # 处理简单型ruleConfig，如('startwith', 'A')
                        if processed is False and \
                            ((ruleConfig[0] == 'startwith' and leftDeckName.startswith(ruleConfig[1])) or \
                             (ruleConfig[0] == 'contain' and leftDeckName.find(ruleConfig[1]) > -1) or \
                             (ruleConfig[0] == 'notcontain' and leftDeckName.find(ruleConfig[1]) == -1)):
                            print '%s moved to ---> %s' % (filename, rule[0])
                            FileOperation.move(os.path.join(dirpath, filename), os.path.join(rule[0], filename))
                            processed = True
                    else:   # 由多个简单型ruleConfig组成的复合型ruleConfig(('startwith', 'A'), ('contain', 'B'), ('notcontain', 'C'))，只有多个简单型ruleConfig均满足时，才代表该复合型ruleConfig被满足
                        matchAll = True
                        for subRuleConfig in ruleConfig:
                            if (subRuleConfig[0] == 'startwith' and not leftDeckName.startswith(subRuleConfig[1])) or \
                                (subRuleConfig[0] == 'contain' and not leftDeckName.find(subRuleConfig[1]) > -1) or \
                                (subRuleConfig[0] == 'notcontain' and not leftDeckName.find(subRuleConfig[1]) == -1):
                                matchAll = False
                        if processed is False and matchAll is True:
                            print '%s moved to ---> %s' % (filename, rule[0])
                            FileOperation.move(os.path.join(dirpath, filename), os.path.join(rule[0], filename))
                            processed = True

def processOldVideoNames(vedioFolder):
    for dirpath, _, filenames in os.walk(vedioFolder):
        for filename in filenames:
            
            matchObj = re.match(r'^(\W*)vs(\W*)-([0-9]{1,20})(\.\w{3})$', filename)
            if matchObj:
                timestamp = chansferOldTimeStrToTimestamp(matchObj.group(3))
                if timestamp is None:
                    continue
                newFilename = matchObj.group(1) + 'vs' + matchObj.group(2) + '.[' + timestamp + ']' + matchObj.group(4)
                FileOperation.rename(os.path.join(dirpath, filename), os.path.join(dirpath, newFilename))
                continue
            
            matchObj = re.match(r'^(\W*)vs(\W*)-(tv[0-9]+)(\.\w{3})$', filename)
            if matchObj:
                timestamp = '20180401' + str(random.randint(10,24)) + str(random.randint(10,59)) + str(random.randint(10,59))
                newFilename = matchObj.group(1) + 'vs' + matchObj.group(2) + '.[' + timestamp + ']' + matchObj.group(4)
                FileOperation.rename(os.path.join(dirpath, filename), os.path.join(dirpath, newFilename))
                continue
            
            matchObj = re.match(r'^(\W*)vs(\W*)(\.[0-9]{1,2})(\.\w{3})$', filename)
            if matchObj:
                timestamp = getFileShortCreateTime(os.path.join(dirpath, filename))
                newFilename = matchObj.group(1) + 'vs' + matchObj.group(2) + '.[' + timestamp + ']' + matchObj.group(4)
                FileOperation.rename(os.path.join(dirpath, filename), os.path.join(dirpath, newFilename))
                continue
            
            matchObj = re.match(r'^(\W*)vs(\W*)(\.\w{3})$', filename)
            if matchObj:
                timestamp = getFileShortCreateTime(os.path.join(dirpath, filename))
                newFilename = matchObj.group(1) + 'vs' + matchObj.group(2) + '.[' + timestamp + ']' + matchObj.group(3)
                FileOperation.rename(os.path.join(dirpath, filename), os.path.join(dirpath, newFilename))
                continue
                
def chansferOldTimeStrToTimestamp(oldTimeStr):
    if len(oldTimeStr) > 10:
        return '%s%s%s%s' % (oldTimeStr[0:4], oldTimeStr[4:6], oldTimeStr[6:8], oldTimeStr[8:])
    elif len(oldTimeStr) == 10:
        return '%s%s%s%s' % (oldTimeStr[0:4], oldTimeStr[4:6], oldTimeStr[6:8], oldTimeStr[8:])
    elif len(oldTimeStr) == 9:
        if int(oldTimeStr[4:6]) <= 12:
            if int(oldTimeStr[7:]) <= 24:
                return '%s%s%s%s' % (oldTimeStr[0:4], oldTimeStr[4:6], '0'+oldTimeStr[6:7], oldTimeStr[7:])
            elif int(oldTimeStr[6:8]) <= 31:
                return '%s%s%s%s' % (oldTimeStr[0:4], oldTimeStr[4:6], oldTimeStr[6:8], '0'+oldTimeStr[8:])
            else:
                return None
        else:
            return None
    elif len(oldTimeStr) == 8:
        return '%s%s%s%s' % (oldTimeStr[0:4],oldTimeStr[4:6],'0'+oldTimeStr[6:7],'0'+oldTimeStr[7:8])
    else:
        return None
    
def replaceVideoNames(vedioFolder, srcStr, replacement):
    for dirpath, _, filenames in os.walk(vedioFolder):
        for filename in filenames:
            if filename.find(srcStr) > -1:
                FileOperation.rename(os.path.join(dirpath, filename), os.path.join(dirpath, filename.replace(srcStr, replacement)))
    
def preProcess(dirpath):
    replaceVideoNames(dirpath, '.MOV', '.mov')
    replaceVideoNames(dirpath, '.MP4', '.mp4')
    processOldVideoNames(dirpath)
    
def getFileShortCreateTime(filePath):
    filePath = unicode(filePath,'utf8')
    t = os.path.getmtime(filePath)
    timeStruct = time.localtime(t)
    return time.strftime('%Y%m%d%H',timeStruct)

def processBearPhotos(dirpath, movetoDirpath):
    for dirpath, _, filenames in os.walk(dirpath):
        for filename in filenames:
            matchObj = re.match(r'^小熊(.*)', filename)
            if matchObj:
                newFilename = '小熊.' + '[' + FileUtil.getFileCreateTime(os.path.join(dirpath, filename)) + ']' + '.' + matchObj.group(1)
                FileOperation.rename(os.path.join(dirpath, filename), os.path.join(movetoDirpath, newFilename))

if __name__  == '__main__':
    processCRVedios('/Users/jerry/Downloads')
    processBearPhotos('/Users/jerry/Downloads', '/Volumes/Seagate/图片/照片/人/小熊')
    
    
    