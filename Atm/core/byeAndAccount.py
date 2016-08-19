#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from Atm.core import manage

def byeAndAccount(username,productSum):
    WHITE_USER_INFO = manage.readWhite()
    availableBalance = WHITE_USER_INFO[username]['account'][0] + WHITE_USER_INFO[username]['account'][1]
    if productSum <= availableBalance:
        if productSum <= WHITE_USER_INFO[username]['account'][1]:
            WHITE_USER_INFO[username]['account'][1] = WHITE_USER_INFO[username]['account'][1] - productSum
            manage.writeWhite(WHITE_USER_INFO)
            return 'OK'
        elif productSum > WHITE_USER_INFO[username]['account'][1]:
            WHITE_USER_INFO[username]['account'][0] = WHITE_USER_INFO[username]['account'][0] - productSum
            WHITE_USER_INFO[username]['account'][2] = WHITE_USER_INFO[username]['account'][2] + productSum
            WHITE_USER_INFO[username]['account'][1] = 0
            manage.writeWhite(WHITE_USER_INFO)
            return 'OK'
#     else:
#         print('余额不足，请充值或适当减少购物车物品。')