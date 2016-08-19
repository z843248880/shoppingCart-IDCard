#coding:utf-8
import sys,os,json,time
from Atm.core import atmLog
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Atm.core import manage


def withdrawCash(username):
    WHITE_USER_INFO = manage.readWhite()
    accountList = WHITE_USER_INFO[username]['account']
    print('信用卡可用额度：' + str(accountList[0]))
    print('卡上余额：' + str(accountList[1]))
    print('已欠款额：' + str(accountList[2])) 
    print('您当前最多可提现金额：' + str(accountList[0] + accountList[1]))
    while True:
        userCash = input('请输入要提现的金额：')
        if userCash.isdigit():
            userCash = int(userCash)
            if userCash <= 0:
                print('您输入的数字必须大于0，请重新输入。')
                continue
            elif userCash <= accountList[1]:
                WHITE_USER_INFO[username]['account'][1] = WHITE_USER_INFO[username]['account'][1] - userCash
                f = open(BASE_DIR + '/files/whiteUserInfo','w')
                f.write(json.dumps(WHITE_USER_INFO))
                f.close()
                atmLog.atmLog(time.asctime(),username,('withdrasw cash %s success.' % userCash))
                print('提现%s成功' % userCash)
                break
            elif accountList[1] < userCash <= accountList[0] + accountList[1]:
                interest = (userCash - accountList[1]) * 0.05
                if userCash + interest > accountList[0] + accountList[1]:
                    print('您输入的数值过大，无法扣利息，请重新输入.')
                    continue
                WHITE_USER_INFO[username]['account'][0] = WHITE_USER_INFO[username]['account'][0] - (userCash - accountList[1]) - interest
                WHITE_USER_INFO[username]['account'][2] = WHITE_USER_INFO[username]['account'][2] + (userCash - accountList[1]) + interest
                WHITE_USER_INFO[username]['account'][1] = 0
                f = open(BASE_DIR + '/files/whiteUserInfo','w')
                f.write(json.dumps(WHITE_USER_INFO))
                f.close()
                atmLog.atmLog(time.asctime(),username,('withdrasw cash %s success,the interest is %s' % (userCash,interest)))
                print('提现%s成功' % userCash)
                break
            else:
                print('您输入的数字过大，无法提取现金。')
        else:
            print('请输入数值（阿拉伯数字）：')

