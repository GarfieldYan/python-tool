# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')   # @UndefinedVariable
import os
import shutil


def copy(src, dest):
    if os.path.isdir(src):
        shutil.copytree(src, dest)
    else:
        shutil.copy(src, dest)

def move(src, dest):
    shutil.move(unicode(src, 'utf8'), unicode(dest, 'utf8'))
    
def rename(src, dest):
    move(src, dest)

def remove(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)