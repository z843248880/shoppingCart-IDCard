#coding:utf-8
import sys,os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
from Atm.core import atmLog
from Atm.core import reCharge
def payBack(username):
    
    while True:
            f = open(BASE_DIR + '/files/whiteUserInfo','r')
            WHITE_USER_INFO = json.loads(f.read())
            f.close()
            accountList = WHITE_USER_INFO[username]['account']
            newAccountList = []
            payback = input('系统显示您当前有欠款，输入p还款，输入q暂时不还：')
            if payback == 'p':
                if accountList[1] == 0:
                    userzero = input('您卡上的余额为0，暂无法还款，输入i进行充值，输入其他任意字符退出：')
                    if userzero == 'i':
                        reCharge.reCharge(username)
                    else:
                        break
                else:
                    print('您当前的可用余额是：%s' % accountList[1])
                    while True:
                        userhuankuan = input('请输入您要还款的金额：')
                        if userhuankuan.isdigit():
                            if int(userhuankuan) >  accountList[1]:
                                print('您输入的值过大，请重新输入。')
                            else:
                                newAccountList.append(accountList[0] + int(userhuankuan))
                                newAccountList.append(accountList[1] - int(userhuankuan))
                                newAccountList.append(accountList[2] - int(userhuankuan))
                                WHITE_USER_INFO[username]['account'] = newAccountList
                                f1 = open(BASE_DIR + '/files/whiteUserInfo','w')
                                f1.write(json.dumps(WHITE_USER_INFO))
                                f1.close()
                                atmLog.atmLog(time.asctime(),username,('payCash：%s' % userhuankuan))
                                print('还款成功。')
                                break
                        else:
                            print('请输入金额（阿拉伯数字）：')
            elif payback == 'q':
                break