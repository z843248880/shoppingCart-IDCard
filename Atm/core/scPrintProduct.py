#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Atm.core import productListOpe
PRODUCT_LIST = productListOpe.readProduct()

def scPrintProduct():
    num = 1
    for data in PRODUCT_LIST:
        print('%s. %s' % (num,data))
        num += 1