'''
模块的制作
1 模块定义： python中一个py文件就是一个模块
2 作用：使我们能够有逻辑的去组织我们的python代码，以库的形式封装功能，能定义函数，定义类，定义变量 也能包含可执行的代码， 不通的模块可以定义相同的变量名，但是作用域仅在本模块之中
3 模块的分类： 内置模块 自定义模块 第三方模块
模块发布

'''
#__all__:作用，如果存在__all__变量，那么这个变量中的元素会被from xxx import * 事导入， 但是使用import 模块名，不受__all__影响
__all__=['sum', 'printInfo'] 
def sum(x, y):
    return x + y
def diff(a, b):
    return a-b
def printInfo():
    return '这是模块方法'
#__name__魔术变量，只有在本模块下才执行if中的代码
if __name__ =='__main__':
    print('模块执行代码的结果是：{}'.format(sum(30, 49)))
