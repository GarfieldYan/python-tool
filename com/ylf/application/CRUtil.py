# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
import os
import com.ylf.file.FileOperation as FileOperation
import com.ylf.file.FileUtil as FileUtil

rules = [   ('/Volumes/Seagate/视频/CR/1. 胖子/1.2 胖子电法', [(('startwith', '胖子'), ('contain', '电法'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.3 胖子雷龙', [(('startwith', '胖子'), ('contain', '雷龙'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.4 胖子猎人', [(('startwith', '胖子'), ('contain', '猎人'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.5 胖子火枪', [(('startwith', '胖子'), ('contain', '火枪'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.6 胖子火法', [(('startwith', '胖子'), ('contain', '火法'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.7 胖子屠夫', [(('startwith', '胖子'), ('contain', '屠夫'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.8 胖子双苍', [(('startwith', '胖子'), ('contain', '机甲'), ('contain', '小苍'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.9 胖子九苍', [(('startwith', '胖子'), ('contain', '大苍'), ('contain', '小苍'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.1 胖子粉丝', [(('startwith', '胖子'), ('contain', '团伙'), ('contain', '蝙蝠'))] ),
            ('/Volumes/Seagate/视频/CR/1. 胖子/1.10 其它胖子', [('startwith', '胖子'), ('startwith', '绿胖')] ),
            ('/Volumes/Seagate/视频/CR/2. 连弩/2.1 电塔弩/2.1.1 经典电塔弩', [('startwith', '连弩电塔冰人弓箭骷髅冰豆滚木火球')] ),
            ('/Volumes/Seagate/视频/CR/2. 连弩/2.1 电塔弩/2.1.2 其它电塔弩', [(('startwith', '连弩'), ('contain', '电塔'))] ),
            ('/Volumes/Seagate/视频/CR/2. 连弩/2.2 冰法弩/2.2.1 火箭冰法弩', [(('startwith', '连弩'), ('contain', '冰法'), ('contain', '火箭'))] ),
            ('/Volumes/Seagate/视频/CR/2. 连弩/2.2 冰法弩/2.2.2 火球冰法弩', [(('startwith', '连弩'), ('contain', '冰法'), ('contain', '火球'))] ),
            ('/Volumes/Seagate/视频/CR/2. 连弩/2.3 其它弩', [('startwith', '连弩')] )
        ]
                        
""" supported ruleConfigType: startwith, contain """  
def processCRVedios(vedioFolder, rules = rules):
    for dirpath, _, filenames in os.walk(vedioFolder):
        for filename in filenames:
            if filename.find('.DS_Store') > -1:
                continue
            leftDeckName = filename.split('vs')[0]
            processed = False
            for rule in rules:
                for ruleConfig in rule[1]:      # ruleConfigs是一个由多个ruleConfig组成的列表，满足其中任意一个ruleConfig元素就符合该rule
                    if isinstance(ruleConfig[0], str):  # 简单型ruleConfig，如('startwith', 'A')
                        if processed is False and ruleConfig[0] == 'startwith' and leftDeckName.startswith(ruleConfig[1]):
                            availableVedioFullName = os.path.join(rule[0], getAvailableCRVedioBasename(rule[0], filename))
                            print '%s moved to ---> /%s' % (filename, FileUtil.getFolderName(availableVedioFullName))
                            FileOperation.move(os.path.join(dirpath, filename), availableVedioFullName)
                            processed = True
                        elif processed is False and ruleConfig[0] == 'contain' and leftDeckName.find(ruleConfig[1]) > -1:
                            availableVedioFullName = os.path.join(rule[0], getAvailableCRVedioBasename(rule[0], filename))
                            print '%s moved to ---> /%s' % (filename, FileUtil.getFolderName(availableVedioFullName))
                            FileOperation.move(os.path.join(dirpath, filename), availableVedioFullName)
                            processed = True
                        elif processed is False and ruleConfig[0] == 'notcontain' and leftDeckName.find(ruleConfig[1]) == -1:
                            availableVedioFullName = os.path.join(rule[0], getAvailableCRVedioBasename(rule[0], filename))
                            print '%s moved to ---> /%s' % (filename, FileUtil.getFolderName(availableVedioFullName))
                            FileOperation.move(os.path.join(dirpath, filename), availableVedioFullName)
                            processed = True
                    else:   # 由多个简单型ruleConfig组成的复合型ruleConfig(('startwith', 'A'), ('contain', 'B'), ('notcontain', 'C'))，只有多个简单型ruleConfig均满足时，才代表该复合型ruleConfig被满足
                        matchAll = True
                        for subRuleConfig in ruleConfig:
                            if subRuleConfig[0] == 'startwith' and not leftDeckName.startswith(subRuleConfig[1]):
                                matchAll = False
                            elif subRuleConfig[0] == 'contain' and not leftDeckName.find(subRuleConfig[1]) > -1:
                                matchAll = False
                            elif subRuleConfig[0] == 'notcontain' and not leftDeckName.find(subRuleConfig[1]) == -1:
                                matchAll = False
                        if processed is False and matchAll is True:
                            availableVedioFullName = os.path.join(rule[0], getAvailableCRVedioBasename(rule[0], filename))
                            print '%s moved to ---> /%s' % (filename, FileUtil.getFolderName(availableVedioFullName))
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
    
def replaceVideoNames(vedioFolder, srcStr, replacement):
    for dirpath, _, filenames in os.walk(vedioFolder):
        for filename in filenames:
            if filename.find(srcStr) > -1:
                print os.path.join(dirpath, filename)
                FileOperation.rename(os.path.join(dirpath, filename), os.path.join(dirpath, filename.replace(srcStr, replacement)))
        

if __name__  == '__main__':
    
    processCRVediosFlag = True
    replaceVideoNamesFlag = True
    
    if processCRVediosFlag is True:
        processCRVedios('/Users/jerry/Downloads')
    
    if replaceVideoNamesFlag is True:  
        replaceVideoNames('/Volumes/Seagate/视频/CR', '攻城槌', '槌子')
        replaceVideoNames('/Volumes/Seagate/视频/CR', '攻城锤', '槌子')
        replaceVideoNames('/Volumes/Seagate/视频/CR', '小骷髅', '骷髅')
        replaceVideoNames('/Volumes/Seagate/视频/CR', '大苍蝇', '大苍')
        replaceVideoNames('/Volumes/Seagate/视频/CR', '小苍蝇', '小苍')
        replaceVideoNames('/Volumes/Seagate/视频/CR', '黄毛房', '毛房')
        replaceVideoNames('/Volumes/Seagate/视频/CR', '黄毛房', '毛房')
        
        replaceVideoNames('/Users/jerry/Downloads', 'Replay Royale - ', '-2018')
        replaceVideoNames('/Users/jerry/Downloads', 'November ', '11')
        replaceVideoNames('/Users/jerry/Downloads', 'October ', '10')
        replaceVideoNames('/Users/jerry/Downloads', 'September ', '09')
        replaceVideoNames('/Users/jerry/Downloads', 'August ', '08')
        replaceVideoNames('/Users/jerry/Downloads', 'July ', '07')
        replaceVideoNames('/Users/jerry/Downloads', 'June ', '06')
        replaceVideoNames('/Users/jerry/Downloads', 'May ', '05')
        replaceVideoNames('/Users/jerry/Downloads', 'April ', '04')
        replaceVideoNames('/Users/jerry/Downloads', 'March ', '03')
        replaceVideoNames('/Users/jerry/Downloads', 'February ', '02')
        replaceVideoNames('/Users/jerry/Downloads', 'January ', '01')
        replaceVideoNames('/Users/jerry/Downloads', ', 2018 ', '')
        replaceVideoNames('/Users/jerry/Downloads', 'AM', '')
        replaceVideoNames('/Users/jerry/Downloads', '01PM', '13')
        replaceVideoNames('/Users/jerry/Downloads', '02PM', '14')
        replaceVideoNames('/Users/jerry/Downloads', '03PM', '15')
        replaceVideoNames('/Users/jerry/Downloads', '04PM', '16')
        replaceVideoNames('/Users/jerry/Downloads', '05PM', '17')
        replaceVideoNames('/Users/jerry/Downloads', '06PM', '18')
        replaceVideoNames('/Users/jerry/Downloads', '07PM', '19')
        replaceVideoNames('/Users/jerry/Downloads', '08PM', '20')
        replaceVideoNames('/Users/jerry/Downloads', '09PM', '21')
        replaceVideoNames('/Users/jerry/Downloads', '10PM', '22')
        replaceVideoNames('/Users/jerry/Downloads', '11PM', '23')
        replaceVideoNames('/Users/jerry/Downloads', '12PM', '00')
