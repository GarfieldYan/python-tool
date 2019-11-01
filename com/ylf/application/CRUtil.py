# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import os
import re
import random
import time
import com.ylf.file.FileOperation as FileOperation

rules = [   ('/Volumes/Seagate/视频/CR/胖子', [('startwith', '胖子')] ),
            ('/Volumes/Seagate/视频/CR/连弩/标准电塔弩', [('startwith', '连弩冰人骷髅冰豆电塔弓箭滚木火球')] ),
            ('/Volumes/Seagate/视频/CR/连弩/非标准电塔弩', [(('startwith', '连弩'), ('contain', '电塔'))] )
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
                            if not os.path.exists(os.path.join(rule[0], filename)):
                                FileOperation.move(os.path.join(dirpath, filename), os.path.join(rule[0], filename))
                                print '%s moved to ---> %s' % (filename, rule[0])
                            processed = True
                    else:   # 由多个简单型ruleConfig组成的复合型ruleConfig(('startwith', 'A'), ('contain', 'B'), ('notcontain', 'C'))，只有多个简单型ruleConfig均满足时，才代表该复合型ruleConfig被满足
                        matchAll = True
                        for subRuleConfig in ruleConfig:
                            if (subRuleConfig[0] == 'startwith' and not leftDeckName.startswith(subRuleConfig[1])) or \
                                (subRuleConfig[0] == 'contain' and not leftDeckName.find(subRuleConfig[1]) > -1) or \
                                (subRuleConfig[0] == 'notcontain' and not leftDeckName.find(subRuleConfig[1]) == -1):
                                matchAll = False
                        if processed is False and matchAll is True:
                            if not os.path.exists(os.path.join(rule[0], filename)):
                                FileOperation.move(os.path.join(dirpath, filename), os.path.join(rule[0], filename))
                                print '%s moved to ---> %s' % (filename, rule[0])
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

if __name__  == '__main__':
    processCRVedios('/Users/jerry/Downloads')
    processCRVedios('/Volumes/Seagate/视频/CR/3. 石头/石头待命名')
    #replaceVideoNames('/Volumes/Seagate/视频/CR', '胖子小皮卡骷髅海墓园', '胖子墓园小皮卡骷髅海')
    
    
    