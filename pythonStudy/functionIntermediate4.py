'''
函数中级学习
1 局部变量
    1.1概念：在函数内部定义的变量，只能再函数内部使用
    1.2 作用：临时保存数据，需要再函数中声明进行使用，函数执行完成，变量释放
2 全局变量
    2.1 概念：在函数外部定义的变量，可以在函数内部使用
    2.2 区别：作用范围不同
    2.3 优先级：当全局变量和局部变量出现重复定义的时候，程序会优先执行使用函数内部定义的变量
    2.4 当修改全局变量时，需要在函数内部申明全局变量，使用global关键字
3 变量与对象的关系
    3.1 变量：变量是内存中的一个对象，变量是对象的引用
    3.2 对象：对象是内存中的一个实体，对象是由类创建的，对象包含三个要素：id、type、value
    3.3 变量与对象的关系：变量引用对象
    3.4 变量与对象的关系：变量引用对象，变量可以引用不同类型的对象，变量可以引用不同类型的对象
    3.5 变量与对象的关系：变量可以引用不同类型的对象，变量可以引用不同类型的对象
4 总结 在python中，万物都是对象，在函数调用的时候，实参传递的是就是对象的引用
5 函数的参数传递
    5.1 不可变类型的参数传递
        5.1.1 不可变类型：在内存中创建一个新的对象，修改变量的值，就是让变量指向一个新的对象
        5.1.2 不可变类型的参数传递：不可变类型的参数传递，不会修改实参的值
    5.2 可变类型的参数传递
        5.2.1 可变类型：在内存中创建一个新的对象，修改变量的值，就是让变量指向一个新的对象
        5.2.2 可变类型的参数传递：可变类型的参数传递，会修改实参的值
    5.3 函数的参数传递：不可变类型的参数传递，不会修改实参的值
    5.4 函数的参数传递：可变类型的参数传递，会修改实参的值
6 匿名函数
    6.1 在python中使用lambda关键字创建匿名函数，匿名函数没有函数名也不用def关键字
    6.2 匿名函数的语法：lambda 参数1， 参数2， 参数3: 执行表达式（有且只有一个）
    6.3 特点： 匿名函数冒号后面的表达式有且只有一个，匿名函数自带return，返回值就是表达式的结果
    6.4 局限性：lambda只能是单个表达式，不是一个代码块，lambda的设计就是为了满足简单函数的场景
7 三元表达式
    a if b else c
    如果为真执行a, 否则执行c
8 递归函数
    8.1 定义：函数自己调用自己
    8.2 递归函数的特点：必须有一个明确的结束条件，递归的深度不宜过大
    8.3 递归函数的优点：代码简洁
    8.4 递归函数的缺点：递归深度大，会导致栈溢出

'''
age = 18
def test():
    name = 'mia'
    print('{}--{}---{}'.format(name, age, like))
def test2():
    name = 'mia1'
    print(name,end  = '')
    print(age)
    print(like)
    print()
def changeGlobal():
    '''
    修改全局变量
    '''
    global like 
    like = 'learn python'
    global age #声明age为全局变量
    age = 20
changeGlobal()
test()
test2()
a = 2
def func(x):
    print('x对象的地址:{}'.format(id(x)))
    x =1
    print('x对象修改后的地址:{}'.format(id(x)))
print('a对象的地址:{}'.format(id(a)))
func(a)
def sumNum(a, b):
    '''
   计算两个数的和 
    '''
    sum = a + b
    return sum
print(sumNum(20, 30))
#使用lambda函数计算两个数的和
sumA = lambda a, b: a+ b
print(sumA(20, 35))
#使用lambda函数计算三个数的积
multiplication = lambda a, b , c: a* b* c
print(multiplication(100, 100, 100))
#使用lambda与三元表达式结合范例
result = lambda x, y: x if x > y else y
print(result(21 , 22))
#lambda 另类的调用放hi
rs = (lambda intA,intB: intA if intA % 2 ==0 else intB) (4, 5)
print(rs)
# 普通函数求阶乘 
# 循环方式实现
number = int(input('请输入一个数：'))
result = 1
while number  > 0:
    result *= number
    number -= 1
print(result)
# 使用函数+循环方式求阶乘
def factorial(n):
    '''
    求阶乘
    '''
    rs1 = 1
    while n >0:
        rs1 *= n
        n -= 1
    return rs1
print(factorial(5))
#  使用递归函数实现阶乘
def factorial1(n):
    '''
    求阶乘递归方式实现
    '''
    if n == 1:
        return 1
    else:
        return n * factorial1(n-1)
# 递归调用
print(factorial1(5))
# 文件遍历 模拟实现树形结构遍历
import os #引入文件操作模块
def findFile(path):
    listRs = os.listdir(path) #得到该路径下所有的文件夹
    for fileItem in listRs:
        full_path = os.path.join(path, fileItem) #获取完整的文件路径
        if os.path.isdir(full_path):#判断是否是文件夹
            findFile(full_path) #如果是文件夹继续遍历
        else:
            print(fileItem)
    else:
        return
findFile('D:\\python')