#coding:utf-8
import sys,os,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from Atm.core import scPrintProduct
from Atm.core import productListOpe
from Atm.core import byeAndAccount
from Atm.core import shoppingLog
from Atm.core import delRepeatList

def scShoppingCart(username):
    scPrintProduct.scPrintProduct()
    PRODUCT_LIST = productListOpe.readProduct()
    shoppingCartList = []
    nlist = []
    while True:
        productSum = 0
        userinput = input('请输入商品序号，输入q退出购物车程序，输入l打印已选商品，输入b购买已选商品，输入d删除商品：')
        if userinput.isdigit():
            for i in range(1,len(PRODUCT_LIST)+1):
                if i == int(userinput):
                    shoppingCartList.append(PRODUCT_LIST[i - 1])     
                    print('%s 添加成功。' % PRODUCT_LIST[i - 1])               
        elif userinput == 'q':
            print('bye')
            sys.exit()
        elif userinput == 'l':           
            for data in shoppingCartList:
                productSum += int(data.split(':')[1])
            nlist = delRepeatList.delRepeatList(shoppingCartList)
            for data in nlist:
                print(data)
            print('商品总额是：%s' % productSum)                    
            continue
        elif userinput == 'lp':
            scPrintProduct.scPrintProduct()
            continue
        elif userinput == 'd':
            while True:
                for num,data in zip(range(1,len(shoppingCartList)+1),shoppingCartList):
                    print('%s.%s' % (num,data))
                userdel = input('输入要删除的商品序号,输入q回到购物车列表：')
                if userdel.isdigit():
                    for i in range(1,len(shoppingCartList)+1):
                        if i == int(userdel):
                            del shoppingCartList[i - 1]
                elif userdel == 'q':
                    break
                else:
                    print('您输入的序号不存在。')
        elif userinput == 'b':
            for data in shoppingCartList:
                productSum += int(data.split(':')[1])
            print(nlist)
            if byeAndAccount.byeAndAccount(username, productSum) == 'OK':
                shoppingLog.shoppingLog((time.strftime("%Y-%m-%d %X",time.localtime())), username, ('[product:%s],[total sum:%s]' % (shoppingCartList,productSum)))
                shoppingCartList = []
                print('购物成功。')
            else:
                print('购物失败，请适当减少购物车物品或者充值。')
        else:
            print('请输入商品数字或对应字母。')
                    
                    
    