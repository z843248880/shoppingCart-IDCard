#coding:utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json,re

def login():
    with open(BASE_DIR + '/files/whiteUserInfo','r') as fwr:
        WHITE_USER_INFO = json.loads(fwr.read())
    with open(BASE_DIR + '/files/blackUserInfo','r') as fbr:
        fbrr = fbr.read()
        if re.search(r'\w', fbrr) is not None:
            BLACK_USER_INFO = json.loads(fbrr)
        else:
            BLACK_USER_INFO = {}
    count = 1
    while count <= 4:
        if count == 3:
            print('最后一次机会，输入错误，程序将会退出。')
        if count == 4:
            print('再见。')
            return False
        username = input('username:>')
        if username in BLACK_USER_INFO:
            print('您的账户已被锁定。')
            sys.exit()
        userpasswd = input('userpassword:>')
        if username in WHITE_USER_INFO:
            if userpasswd == WHITE_USER_INFO[username]['info'][0]:
                return username
        else:
            print('username or password is invalid,enter again.')
            count += 1