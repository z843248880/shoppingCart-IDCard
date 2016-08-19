#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json

def readWhite():
    f = open(BASE_DIR + '/files/manager','r')
    MANAGER_INFO = json.loads(f.read())
    f.close()
    return MANAGER_INFO

def mlogin():
    MANAGER_INFO = readWhite()
    