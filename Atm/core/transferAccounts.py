#coding:utf-8
import sys,os,time
from Atm.core import atmLog
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json

def transferAccounts(username):
    f = open(BASE_DIR + '/files/whiteUserInfo','r')
    WHITE_USER_INFO = json.loads(f.read())
    f.close()
    while True:
        toWho = input('请输入您要转入的账号(数字ID)：')
        if toWho not in WHITE_USER_INFO:
            print('您输入的账号不存在，请重新输入.')
        else:
            accountFrom = WHITE_USER_INFO[username]['account']
            accountTo = WHITE_USER_INFO[toWho]['account']
            print('信用卡可用额度：' + str(accountFrom[0]))
            print('卡上余额：' + str(accountFrom[1]))
            print('已欠款额：' + str(accountFrom[2])) 
            print('您当前最多可转金额：' + str(accountFrom[0] + accountFrom[1]))
            transferCash = input('请输入您要输入的转账金额：')
            if transferCash.isdigit():
                transferCash = int(transferCash)
                if transferCash <= 0:
                    print('您输入的值必须大于0')
                    continue
                if transferCash <= accountFrom[1]:
                    WHITE_USER_INFO[username]['account'][1] = WHITE_USER_INFO[username]['account'][1] - transferCash
                    WHITE_USER_INFO[toWho]['account'][1] = WHITE_USER_INFO[toWho]['account'][1] + transferCash
                    f = open(BASE_DIR + '/files/whiteUserInfo','w')
                    f.write(json.dumps(WHITE_USER_INFO))
                    f.close()
                    atmLog.atmLog(time.asctime(),username,('transer %s to %s' % (transferCash,toWho)))
                    print('转账成功。')
                    break
                elif accountFrom[1] < transferCash <= accountFrom[0] + accountFrom[1]:
                    WHITE_USER_INFO[username]['account'][0] = WHITE_USER_INFO[username]['account'][0] - (transferCash - accountFrom[1])
                    WHITE_USER_INFO[username]['account'][2] = WHITE_USER_INFO[username]['account'][2] + (transferCash - accountFrom[1])
                    WHITE_USER_INFO[username]['account'][1] = 0
                    WHITE_USER_INFO[toWho]['account'][1] = WHITE_USER_INFO[toWho]['account'][1] + transferCash
                    f = open(BASE_DIR + '/files/whiteUserInfo','w')
                    f.write(json.dumps(WHITE_USER_INFO))
                    print('转账成功。')
                    break
                else:
                    print('您输入的值过大，已经超过可用余额与可贷余额的总和，请重新输入。')
            else:
                print('请输入数字。')