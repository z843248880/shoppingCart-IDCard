#coding:utf-8
import sys,os,time,json
from fileinput import filelineno
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# import webbrowser
# webbrowser.open('www.baidu.com')



print(filelineno())


















# listt = ['pear:50', 
#          'pear:50', 
#          'watermeon:55', 
#          'watermeon:55', 
#          'watermeon:55', 
#          'mangguo:90', 
#          'zuqiu:300', 
#          'dianshi:5000', 
#          'liequan:7335']
# def delRepeat(listt):
#     listt_set = list(set(listt))
#     nlist = []
#     for i in listt_set:
#         nstr = str(listt.count(i)) + '个' + i.split(':')[0] + ' : ' + str(listt.count(i) * int(i.split(':')[1]))
#         print(nstr)

# for i in range(0,len(listt)):
#     print(listt.count(listt[i]))

# for i in listt:
#     print(i) 
#     
# def noRepeat(listb):
#     nlist = []
#     for i in listb:
#         if i not in nlist:
#             nlist.append(i)
#         else:
#             indexNum = nlist.index(i )
#             indexCom = nlist[indexNum]
#             nlist[indexNum] = indexCom + indexCom
#     return nlist
# print(noRepeat(listt))
            
    
    




















# import psutil
# mem = psutil.virtual_memory()
# print(mem.total / 8 / 1024 / 1024,mem.used)







# operation = '查询'
# f = open(BASE_DIR + '/logs/atmOperation.log','a')
# f.write('[%s]' % (operation))
# f.write('\n')
# f.close()

# one = 500
# two = 300
# three = 100
# 
# print((three + (one - two)) * 0.05)
'''
productdict = {
               'apple':30,
'pear':50,
'watermalon':55,
'wangluo':90,
'zuqiu':300,
'dianshi':5000,
'liequan':7753,
               }
'''


# lista = ['pear:50','watermeon:55','mangguo:90','zuqiu:300','dianshi:5000','liequan:7335','apple:30']
# 
# f = open(BASE_DIR + '/files/productList','w')
# f.write(json.dumps(lista))



# print(time.strftime("%Y-%m-%d %X",time.localtime()))