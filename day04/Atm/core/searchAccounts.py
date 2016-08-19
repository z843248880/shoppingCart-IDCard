#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
from Atm.core import login
from Atm.core import payBack
from Atm.core import reCharge

def searchAccounts(username):
    f = open(BASE_DIR + '/files/whiteUserInfo','r')
    WHITE_USER_INFO = json.loads(f.read())
    f.close()
    accountList = WHITE_USER_INFO[username]['account']
    print('信用卡可用额度：' + str(accountList[0]))
    print('卡上余额：' + str(accountList[1]))
    print('已欠款额：' + str(accountList[2]))
    if accountList[2] > 0:
        payBack.payBack(username)
#     if accountList[1] <= accountList[2]:
#         userchoice = input('系统显示您有欠款且卡上余额不足以还款，输入i进行充值，输入其他退出：')
#         if userchoice == 'i':
#             reCharge.reCharge(username)
        