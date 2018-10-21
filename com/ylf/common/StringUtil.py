# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # @UndefinedVariable

'''
Created on Dec 2, 2016

@author: Jerry
'''

import re


def containChinese(check_str, charset='utf-8'):
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(check_str.decode(charset))
    if match:
        return True
    else:
        return False


def isBlank(check_str):
    return check_str == '' or check_str == None