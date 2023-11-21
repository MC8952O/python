'''
函数的学习
1 函数的概念：python语句的租户组合，可以在程序中运行一次或者多次，一般是完整的独立功能
2 作用：代码复用最大化、最小化冗余代码，整体代码结构清晰，问题局部化
3 函数定义：def 函数名 (参数列表)：
                函数体
4 函数的调用：函数名(参数列表)
5 函数参数分类
    5.1 必选参数
        5.1.1 形式参数：定义函数时，括号中的参数，在定义的时候是不占内存地址的
        5.1.2 实际参数： 实参。调用函数时，括号中的参数，占内存地址
    5.2 默认参数(省略参数)
        5.2.1 调用参数时 如果未赋值，就会用定义函数时给定的默认值 
        5.2.2 缺省参数始终存在于形参的末尾
    5.3 可变参数
        5.3.1 定义：当参数不确定个数时使用
        5.3.2 可变参数的定义：在形参前面加上*，表示可变参数，可变参数是一个元组
        5.3.3 可变参数的调用：在实参前面加上*，表示可变参数，可变参数是一个元组
    5.4 关键字参数
        5.4.1 定义：当参数不确定个数时使用
        5.4.2 关键字参数的定义：在形参前面加上**，表示可变参数，可变参数是一个字典
        5.4.3 在函数体内，关键字参数的key必须是s一个字符串
6 返回值 return
    6.1 概念：函数执行结束，返回一个对象，使用关键字：return，否则返回null
    6.2 return可以返回任意数据类型
    6.3 在一个函数内可以出现多个return多个关键字，但是只能执行一个return关键字
    6.4 在函数内体执行了return，函数就结束了，return后面的代码不会执行
7 函数嵌套调用
    7.1 

'''
# 输出个人信息
def personInformation():
    '''
    函数备注，当鼠标放在函数名上时，会显示函数备注
    '''
    print('姓名：')
    print('年龄：')
    print('性别：')
    print('地址：')
    print('电话：')
personInformation()
#输出不同人的信息
def personInfo(name, age, sex, address, phone):
    '''
    输出不同人的信息
    '''
    print('姓名：{}'.format(name))
    print('年龄：{}'.format(age))
    print('性别：{}'.format(sex))
    print('地址：{}'.format(address))
    print('电话：{}'.format(phone))
personInfo('mia', 18, '女', '苏州', '123456789 ')
# 定义必选参数函数
def sum(a, b):
    '''
    计算两个数的和
    '''
    return a + b
print(sum(1, 4))
# 缺省参数
def sum1(a = 10, b = 20):
    print(a + b)
sum1()  # 30
sum1(1, 3) # 4
sum1(1) # 21
sum1(b = 40) # 50
def sum2(*args): #可变参数
    '''
    可变参数函数
    '''
    sum2 = 0
    for i in args:
        sum2 += i
    print(sum2)
sum2(13, 2, 3, 4)
def keyparam(**kwargs):
    print(kwargs)
dict = {'name':'mia','age':18}
keyparam(**dict) #直接传递字典对象
keyparam(name = 'mia', age = 18, sex = '女') #传递关键字参数
keyparam() #传空
# 混合使用
def complexFunc(b , *args, **kwargs):
    print(b)
    print(args)
    print(kwargs)
complexFunc('他是', 1, name = 'niudehua')
def sum_return(a, b):
    sum = a + b
    return sum
print(sum_return(1, 20))# 将结果返回函数调用的地方，print()打印输出
# 计算累计和函数
def sumAdd(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum
print(sumAdd(1,100))
def sumadd(num):
    sum = 0
    i = 1
    while i <= num:
        sum += i
        i += 1
    return sum
print(sumadd(100))
def A():
    print('---------------A start----------------')
    print('---------------A 执行代码----------------')
    print('---------------A end----------------')
def B():
    '''
    嵌套使用A函数
    '''
    print('---------------B start----------------')
    A()
    print('---------------B end----------------')
B()
# 用函数求接受N个数，求这些参数的和
def sumA(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(sumA(1,200, 100, 2222))
'''def sumB():
    element = input()
    sum = 0
    numList = [int(i) for i in str(element).split()]
    for i in numList:
        sum += i
    return sum 
print(sumB())'''
def egList(*args):
    sumList = []
    resultList = []
    for i in args:
        sumList.append(i)
    print(sumList)
    for j in range(len(sumList)):
        if j % 2 != 0:
            resultList.append(sumList[j])
    return resultList
print(egList(0, 1, 2, 3, 4, 5, 7, 8, 9))
