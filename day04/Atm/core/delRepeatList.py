#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def delRepeatList(listt):
    listt_set = list(set(listt))
    nlist = []
    for i in listt_set:
        nstr = str(listt.count(i)) + '个' + i.split(':')[0] + ' : ' + str(listt.count(i) * int(i.split(':')[1]))
        nlist.append(nstr)
    return nlist