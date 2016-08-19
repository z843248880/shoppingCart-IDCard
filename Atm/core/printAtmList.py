#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Atm.core import login

def printAtmList():
    print('欢迎使用ATM系统'.center(50,'-'))
    print('''
            1.查询
            2.转账
            3.提现
            4.退出
    ''')
    
    
def loginOk(func):
    def wrapper(*args,**kwargs):
        printAtmList()
        func(*args,**kwargs)
    return wrapper
        
    
