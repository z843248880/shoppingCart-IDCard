#coding:utf-8
import sys,os,time
from Atm.core import atmLog
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Atm.core import printAtmList
from Atm.core import login
from Atm.core import selectAtmChoice
from Atm.core import manage


def main():
    while True:
        userChoice = input('''
                        1.用户
                        2.管理
                        3.退出
                                                                        请输入：''')
        if userChoice == '1':
            username = login.login()        
            if username:
                atmLog.atmLog(time.asctime(),username,'login')
                selectAtmChoice.selectAtmChoice(username)            
            else:
                print('login failed.')
        elif userChoice == '2':
            manage.manage()
        elif userChoice == '3':
            print('bye')
            sys.exit()
        
main()