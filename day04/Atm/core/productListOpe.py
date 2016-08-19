#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import json

def readProduct():
    f = open(BASE_DIR + '/files/productList','r')
    PRODUCT_LIST = json.loads(f.read())
    f.close()
    return PRODUCT_LIST


def writeProduct(PRODUCT_LIST):
    f = open(BASE_DIR + '/files/productList','r')
    f.write(json.dumps(PRODUCT_LIST))
    f.close()