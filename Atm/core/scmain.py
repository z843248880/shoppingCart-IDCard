#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Atm.core import login
from Atm.core import scPrintProduct
from Atm.core import scShoppingCart
def scmain():
    username = login.login()        
    if username:
        scShoppingCart.scShoppingCart(username)          
    else:
        print('login failed.')   
scmain()