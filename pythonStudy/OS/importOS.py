'''
模块的学习
1 使用import 关键字
2 调用格式 模块名.函数名
3 import导入执行步骤
    1 打开模块文件
    2 执行模块对应得文件，将执行过程中产生的名字都丢到模块得名称空间
    3 程序中会有一个模块的名称指向模块的名称空间去
4 导入模块的方式
    1 import 模块名
    2 form...import 方法名
    3 调用时直接使用方法，不需要模块名.方法
    4 from time import *  “*”使用导入时的是该模块全部的函数
    4 使用form时，如果函数名相同，后面导入的会覆盖前面导入的
5 导入模块起别名
    1 使用as关键字进行命名
'''
from time import time, ctime
print(ctime())
# 加别名
import pytest as my_pytest
