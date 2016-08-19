#coding:utf-8
import sys,os,re
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import json

def printSuccess(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print('操作完成。')
    return wrapper


def readWhite():
    f = open(BASE_DIR + '/files/whiteUserInfo','r')
    WHITE_USER_INFO = json.loads(f.read())
    f.close()
    return WHITE_USER_INFO

def writeWhite(data):
    f = open(BASE_DIR + '/files/whiteUserInfo','w')
    f.write(json.dumps(data))
    f.close()


def addUser(username,password='q',zonge=15000,yue=0,qiankuan=0):
    if username == '':
        print('用户名不能为空。')
        return 'username is invalid.'
    else:
        WHITE_USER_INFO = readWhite()
        WHITE_USER_INFO[username] = {"info": [password, "11:13"], "account": [zonge, yue, qiankuan]}
        writeWhite(WHITE_USER_INFO)
        print('操作完成')
@printSuccess
def delUser(username):
    WHITE_USER_INFO = readWhite()
    WHITE_USER_INFO.pop(username)
    writeWhite(WHITE_USER_INFO)
    
@printSuccess    
def lockUser(username):
    f = open(BASE_DIR + '/files/blackUserInfo','r')
    fr = f.read()
    f.close()
    if re.search(r'\w', fr) is not None:
        BLACK_USER_INFO = json.loads(fr)
    else:
        BLACK_USER_INFO = {}
    WHITE_USER_INFO = readWhite()
    BLACK_USER_INFO[username] = WHITE_USER_INFO[username]
    f = open(BASE_DIR + '/files/blackUserInfo','w')
    f.write(json.dumps(BLACK_USER_INFO))
    f.close()
    WHITE_USER_INFO.pop(username)
    writeWhite(WHITE_USER_INFO)
@printSuccess
def updateUser(username,password='q',zonge=15000):
    WHITE_USER_INFO = readWhite()
    if password == ''  and zonge == '' :
        print('您未做任何修改，但是系统允许您这么玩儿。')
        return 'not change'
    elif password == '':
        WHITE_USER_INFO[username]['account'][0] = zonge
        writeWhite(WHITE_USER_INFO)
    elif zonge == '':
        WHITE_USER_INFO[username]['info'][0] = password
        writeWhite(WHITE_USER_INFO)
    else:
        WHITE_USER_INFO[username]['account'][0] = zonge
        WHITE_USER_INFO[username]['info'][0] = password
        writeWhite(WHITE_USER_INFO)
def listUser(username=None):
    WHITE_USER_INFO = readWhite()
    if username:
        print(WHITE_USER_INFO[username])
    else:
        print(WHITE_USER_INFO)
        
        
def manage():    
    while True:   
        userChoice = input('''
                        1.添加用户
                        2.删除用户
                        3.修改用户
                        4.查询用户
                        5.锁定用户
                        ''')
        username = input('请输入要操作的用户名：')
        f = open(BASE_DIR + '/files/whiteUserInfo','r')
        WHITE_USER_INFO = json.loads(f.read())
        f.close()
        list14 = ['1','4']
        if userChoice not in list14 and username not in WHITE_USER_INFO:
            print('您输入的用户名不存在，请重新输入。')
            continue
        if userChoice.isdigit():
            if userChoice == '1':
                addUser(username)
                break
            elif userChoice == '2':
                delUser(username)
                break
            elif userChoice == '3':
                password = input('请输入要设置的密码，回车则默认：')
                zonge = input('请输入信用卡可借款总额，回车则默认：')
                updateUser(username,password,zonge)
                break
            elif userChoice == '4':
                listUser(username)
                break
            elif userChoice == '5':
                lockUser(username)
                break
        else:
            print('请输入相应数字，谢谢。')
    
    
    
    