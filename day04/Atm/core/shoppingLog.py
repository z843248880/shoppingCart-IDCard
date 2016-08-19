#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def shoppingLog(date,username,operation):
    f = open(BASE_DIR + '/logs/' + username + 'shopping.log','a')
    f.write('[date:%s] [user:%s] [operation:%s]' % (date,username,operation))
    f.write('\n')
    f.close()
    