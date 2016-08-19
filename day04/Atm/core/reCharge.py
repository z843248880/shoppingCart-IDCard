#coding:utf-8
import sys,os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import json
from Atm.core import authCode, atmLog
def reCharge(username):
    f = open(BASE_DIR + '/files/whiteUserInfo','r')
    WHITE_USER_INFO = json.loads(f.read())
    f.close()
    accountList = WHITE_USER_INFO[username]['account']
    while True:
        authCodeStr = authCode.authCode(4)
        usercode = input('输入以下验证码即可充值500:')
        if usercode == authCodeStr:
            WHITE_USER_INFO[username]['account'][1] = WHITE_USER_INFO[username]['account'][1] + 500
            f = open(BASE_DIR + '/files/whiteUserInfo','w')
            f.write(json.dumps(WHITE_USER_INFO))
            f.close()
            atmLog.atmLog(time.asctime(),username,'chargeCash.')
            print('充值成功。')
            break
            
        else:
            print('输入错误。')