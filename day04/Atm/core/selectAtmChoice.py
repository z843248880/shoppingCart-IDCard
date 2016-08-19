#coding:utf-8
import sys,os,time
from Atm.core import transferAccounts, atmLog, withdrawCash
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Atm.core import printAtmList
from Atm.core import searchAccounts


@printAtmList.loginOk
def selectAtmChoice(username):
    while True:   
        userChoice = input('请输入对应的数字：')
        if userChoice.isdigit():
            if userChoice == '1':
                atmLog.atmLog(time.asctime(),username,'search')
                searchAccounts.searchAccounts(username)
                break
            elif userChoice == '2':
                atmLog.atmLog(time.asctime(),username,'transferCash')
                transferAccounts.transferAccounts(username)
                break
            elif userChoice == '3':
                atmLog.atmLog(time.asctime(),username,'withdrawCash')
                withdrawCash.withdrawCash(username)
                break
            elif userChoice == '4':
                print('bye')
                break
            else:
                print('请输入相应数字，谢谢。')