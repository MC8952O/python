'''
1 字符串及常用方法
    1.1 capitalize() 将字符串的第一个字符转换为大写
    1.2 endswtih() 检查字符串是否以指定的字符串结尾
    1.3 startswith() 检查字符串是否以指定的字符串开头
    1.4 find() 检测字符串中是否包含子字符串
    1.5 isalnum() 检测字符串是否由字母和数字组成
    1.6 isalpha() 检测字符串是否只由字母组成
    1.7 isdigit() 检测字符串是否只由数字组成
    1.8 islower() 检测字符串是否由小写字母组成
    1.9 join() 将列表中的字符串连接成一个字符串
    2.0 lower() 将字符串中的大写字母转换为小写字母
    2.1 upper() 将字符串中的小写字母转换为大写字母
    2.2 swapcase() 将字符串中的大小写字母进行转换
    2.3 lstrip() 删除字符串左侧的空白字符
    2.4 rstrip() 删除字符串右侧的空白字符
    2.5 strip() 删除字符串两侧的空白字符
    2.6 split() 将字符串按照指定的字符分割成列表
    2.7 title() 将字符串中的每个单词的首字母转换为大写
    2.8 replace(old, new, coount = None) 将字符串中的指定字符串替换为指定的字符串 old:被替换的字符串 new:替换的字符串 count:替换的次数,无表示全部替换
    2.9 count() 统计字符串中指定字符串出现的次数
2 列表及常用方法
    2.1 定义：是有序的数据集合
    2.2 特点：
        2.2.1 支持增删改查
        2.2.2 列表中的数据是可以变化的【数据项可以变化，但是内存地址不会改变】
        2.2.3 使用[]表示列表，数据项之间使用“，”分割，数据项可以是任何类型的数据
        2.2.4 支持索引和切片的操作处理
    2.3 常用的方法
        2.3.1 append() 在列表的末尾添加新的元素 语法：list.append(obj)
        2.3.2 count() 统计某个元素在列表中出现的次数 语法：list.count(obj)
        2.3.3 extend() 在列表的末尾一次性追加另一个序列中的多个值 语法：list.extend(seq)
        2.3.4 index() 从列表中找出某个值第一个匹配项的索引位置 语法：list.index(obj)
        2.3.5 insert() 将对象插入列表 语法：list.insert(index, obj)
        2.3.6 pop() 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 语法：list.pop(index = -1)
        2.3.7 remove() 移除列表中某个值的第一个匹配项 语法：list.remove(obj)
        2.3.8 reverse() 反向列表中元素 语法：list.reverse()
        2.3.9 sort() 对原列表进行排序 语法：list.sort(cmp = None, key = None, reverse = False)
        2.3.2 clear() 清空列表 语法：list.clear() 
3 元组及常用方法
    3.1 定义：是一种不可变的序列，在创建之后不能够做任何修改 使用()创建元组
    3.2 特点：元组类型可以是任何数据类型
              当元组只有一个元素时，需要在元素后面添加逗号，不然解释器会当作整型处理
              支持切片
    3.3常用方法：
        3.3.1 count() 统计某个元素在元组中出现的次数 语法：tuple.count(obj)
        3.3.2 index() 从元组中找出某个值第一个匹配项的索引位置 语法：tuple.index(obj)
                
4 字典及常用方法
    4.1 定义：是一种无序的数据集合，使用{}表示，数据项之间使用“，”分割，数据项的格式为：key:value
    4.2 特点：字典不是序列，不能使用索引进行访问，只能通过键进行访问，且不key不能重复 支持对数据增删改查进行操作
    4.4 如果key存在重复的，后者会覆盖前者
    4.4 常用方法：
        4.3.1 clear() 清空字典 语法：dict.clear()
        4.3.2 copy() 返回字典的浅复制 语法：dict.copy()
        4.3.3 fromkeys(seq[, val]) 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值 语法：dict.fromkeys(seq[, val])
        4.3.4 get(key, default = None) 返回指定键的值，如果值不在字典中返回default值 语法：dict.get(key, default = None)
        4.3.5 items() 以列表返回可遍历的(键, 值) 元组数组 语法：dict.items()
        4.3.6 keys() 返回一个迭代器，可以使用list()来转换为列表 语法：dict.keys()
        4.3.7 pop(key[, default]) 删除字典给定键key所对应的值，返回值为被删除的值，key值必须给出，否则返回default值 语法：
5 共有操作
    5.1合并操作 适用于字符串、列表、元组
    5.2 复制操作 适用于字符串、列表、元组
    5.3 in判断
6 序列(集合)
    6.1 定义：就是一组按照顺序排列的值
    6.2 分类：字符串、列表、元组
    6.3 优点：支持索引和切片的操作
    6.4 特征: 第一个正索引为0，指向的是左端，第一个索引为负数时，指向的是右端
    6.5 切片: 可以根据下标获取序列兑现的任意部一部分 [start:end:step]  start:开始位置，end:结束位置，step:步长 默认为1
'''
# 1 字符串及常用方法
strTest1 = "hello python"
# 打印字符串
print(type(strTest1))
for i in strTest1:
    print(i, end = " ")
# 首字母大写
print("首字母大写：{}".format(strTest1.capitalize()))
# 去除空格
strTest2 = '   hello mia.chen   '
print('去除空格：{}'.format(strTest2.strip()))
strTest3 = '   hello mia.chen  '
print('去除左边空格：{}'.format(strTest3.lstrip()))
strTest4 = '   hello mia.chen  '
print('去除右边空格：{}'.format(strTest4.rstrip()))
#查看a,b是否是同一个对象
a = 'hello'
print('a的内存地址是：{}'.format(id(a)))
b = a
print('b的内存地址是：{}'.format(id(b)))
'''
查找字符串
find 查找目标对象在序列中的索引，如果不存在则返回-1
find()只会显示目标对象在序列中第一个出现的索引
'''
dataStr = 'I love python'
print('查找字符串：{}'.format(dataStr.find(' ')))
'''
index()函数
找到目标对象在序列中的索引 返回索引，若没有找到对应的目标索引。则报错
'''
print('查找p在序列中的索引：{}'.format(dataStr.index('p')))
'''
startswith():判断以...开头
'''
print(dataStr.startswith('I')) #Ture
print(dataStr.startswith('p')) #false
'''
endswith()以什么结尾
'''
print(dataStr.endswith('on')) #True
print(dataStr.endswith('I')) #False
'''
大小写转换
1. 首字母大写 capitalized()
2. 全大写 upper()
3. 全小写 lower()
'''
# 首字母大写
print(dataStr.capitalize()) #I love python
print(dataStr.upper()) #I LOVE PYTHON
print(dataStr.lower()) #i love python
'''
切片
[start:end:step] 左闭右开

'''
sliceStr = 'hello mia good good study'
#获取0~5之间的字符
print(sliceStr[2:5]) #llo
#获取2以后的字符
print(sliceStr[2:]) #llo mia good good study
#完整字符
print(sliceStr[:])
#1~3
print(sliceStr[:3])
#倒序输出 负号
print(sliceStr[::-1])
#列表定义
myList = [1, 2, 3, 'hello python', 12.3 , True]
#查看序列长度(针对与字符串)，查看序列中元素的个数(针对于列表)
print(len(myList)) #4
myStr = 'my name is mia'
print(len(myStr)) #14
#查找
# 输出第一个元素
print(myList[0]) #1
#输出2-3个元素
print(myList[1:3]) #2,3
#输出第3个开始的所有
print(myList[2:]) #3,'hello python',12.3,True
#倒叙输出
print(myList[::-1]) #True,12.3,'hello python',3,2,1
# 列表计算 复制列表
print(myList*2) #[1, 2, 3, 'hello python', 12.3, True, 1, 2, 3, 'hello python', 12.3, True]
# 列表增加 常用的函数 append() insert(index, obj) extend()
# 追加元素追加的元素数据类型不做限制
myList.append('mia.chen')
print(myList) #[1, 2, 3, 'hello python', 12.3, True, 'mia.chen']
myList.append([1, 2, 3])
print(myList) #[1, 2, 3, 'hello python', 12.3, True, 'mia.chen', [1, 2, 3]]
# 插入元素  insert(index, obj)
myList.insert(4, '在4的位置插入改元素')
print(myList) #[1, 2, 3, 'hello python', '在4的位置插入改元素', 12.3, True, 'mia.chen', [1, 2, 3]]
myList.insert(12.3)
#批量插入  extend() #追加的元素必须是序列
rsData = list(range(10)) #强制转换为列表
print(type(rsData)) #<class 'list'>
myList.extend(rsData)
print(myList) #[1, 2, 3, 'hello python', '在4的位置插入改元素', 12.3, True, 'mia.chen', [1, 2, 3], 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#修改元素
updateList = [1, 2, 3, 'hello python', 12.3 , True]
#根据索引修改
updateList[2] = '将第二个元素修改'
print(updateList) #[1, 2, '将第二个元素修改', 'hello python', 12.3, True]
# 修改---删除元素
listDelete = list(range(10, 50))
#删除第一项元素
del listDelete[0]
print(listDelete)
#批量删除
del listDelete[1:3]
print(listDelete) #[11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22...]
#remove() 删除指定的元素
listDelete.remove(22) #删除22
print(listDelete) #[11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23...]
# pop(index)删除指定索引的元素
listDelete.pop(0)
#查找元素的索引
print(listDelete.index(24)) #6
#元素反转
listDelete.reverse()
print(listDelete) #[49, 48, 47, 46, 45, 44, 43, 42, 41, 40...]
#统计列表中元素个数
print(listDelete.count(23)) #0
#列表排序
listSort = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#正序
listSort.sort()
print(listSort) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#倒序
listSort.sort(reverse = True)
print(listSort) #[9, 8, 7, 6, 5, 4, 3, 2, 1]
#元组
#定义一个元组
myTuple = ()
print(type(myTuple)) #<class 'tuple'>
myTuple = (1, 2, 'hello python', 23.4, (1, 3, 'mia'), [12, 'mia', 12.4, (1,)], True)
print(myTuple)
#只能对元组进行查询操作
#遍历元组
for i in myTuple:
    print(i, end =" ") #1 2 hello python 23.4 (1, 3, 'mia') [12, 'mia', 12.4, (1,)] True
#通过下边取值
print(myTuple[1]) #2
#切片 4~5的元素 
print(myTuple[3:5]) #23.4 (1, 3, 'mia')
# 切片倒序
print(myTuple[::-1]) #True [12, 'mia', 12.4, (1,)] (1, 3, 'mia') 23.4 hello python 2 1
#倒序切片1
print(myTuple[::-2]) #(True, (1, 3, 'mia'), 'hello python', 1)
#倒序切片2
print(myTuple[-5:-1:1]) #('hello python', 23.4, (1, 3, 'mia'), [12, 'mia', 12.4, (1,)])
#倒序切片3
print(myTuple[-4:-2:-1]) #()
#可以对元组中的列表进行修改
myTuple[6][1] = 'mia'
print(myTuple)
#统计元组中某个元素出现的次数
print(myTuple.count(1)) #2
myDict = {}
print(type(myDict)) #<class 'dict'>
#添加数据
myDict['name'] = 'mia'
print(myDict) #{'name': 'mia'}
myDict['age'] = 18
myDict['jobNme'] = 'teacher'
print(myDict) #{'name': 'mia', 'age': 18, 'jobNme': 'teacher'}
# 申明一个字典时初始化值
myDict1 = {'name': 'mia', 'age': 16, 'jobName': 'teacher'}
#计算长度
print(len(myDict1)) #3
# 查找--通过键查找对应的值
print(myDict['name']) #mia
# 修改
myDict['name'] = 'mia.chen'
print(myDict) #{'name': 'mia.chen', 'age': 18, 'jobNme': 'teacher'}
#获取所有的键
print(myDict.keys()) #dict_keys(['name', 'age', 'jobNme'])
#获取所有的值
print(myDict.values) #dict_values(['mia.chen', 18, 'teacher'])
#获取所有的键和值
print(myDict.items()) #dict_items([('name', 'mia.chen'), ('age', 18), ('jobNme', 'teacher')]) 
# 遍历字典
for item in myDict.items():
    print(item)             #('name', 'mia.chen') ('age', 18) ('jobNme', 'teacher')
#分别获取键和值--for 遍历
for key, value in myDict.item():
    print('{}:{}'.format(key, value))       #name:mia.chen age:18 jobNme:teacher
#更新字典 --update() -修改
myDict.update({'name':'情绪稳定'})
print(myDict) #{'name': '情绪稳定', 'age': 18, 'jobNme': 'teacher'}
#更新字典 --uodate() -添加
myDict.update({'school': '北京大学'})
print(myDict) #{'name': '情绪稳定', 'age': 18, 'jobNme': 'teacher', 'school': '北京大学'}
#更新update总结，如果键存在做修改操作，如果不存在做新增操作
#删除字典中的元素
del myDict['school']
print(myDict) #{'name': '情绪稳定', 'age': 18, 'jobNme': 'teacher'}
#pop删除
myDict.pop('age')
print(myDict) #{'name': '情绪稳定', 'jobNme': 'teacher'}
#对字典进行排序操作 sorted()
#按照key排序
print(sorted(myDict.items(), key = lambda d:d[0])) #[('jobNme', 'teacher'), ('name', '情绪稳定')]   按照键排序
#按照value排序
print(sorted(myDict.item(), value = lambda d:d[1])) #[('name', '情绪稳定'), ('jobNme', 'teacher')]   按照值排序
# 共有方法
strA = '你好，我是mia'
strB = '我正在学习python'
print(strA + strB) #你好，我是mia我正在学习python
listA = list(range(10))
listB = list(range(10,20))
print(listA + listB) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...] 列表合并
#复制操作 使用* 进行复制
print(strA * 2) #你好，我是mia你好，我是mia
print(listA*2) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0...]
#判断对象是否存在
print('我' in strA) #True
print('da' in strA) #False
