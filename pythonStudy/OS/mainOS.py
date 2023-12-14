#最原始的导入
'''import make_OS
print(make_OS.sum(20,40))'''
#from ...import  导入
'''from make_OS import sum
print(sum(30,50))'''
# from 全部导入
from make_OS import *
print(sum(40,50))
print(printInfo())
print(diff(20, 500))
