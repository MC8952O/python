'''
Python内置函数
1 内置函数简介
    python自带的函数
2 数据运算
    2.1 abs() 绝对值
    2.2 round(x,y) 四舍五入 对x四舍五入保留y位小数
    2.3 pow(x, y) x的y次方
    2.4 divmod(x, y) 返回商和余数
    2.5 max() 返回最大值  序列中的最大值
    2.6 min() 返回最小值
    2.7 sum(interable, star) 求和  传值为可迭代对象 star相加参数 ，然后求和 没有指定则为0
    2.8 eval() 执行字符串表达式 可以调用函数执行
3 类型转换
 3.1 int() 转换为整型
 3.2 float() 转换为浮点型
 3.3 str() 转换为字符串
 3.4 ord() 将字符转换为ascii码
 3.5 chr() 将ascii码转换为字符
 3.6 bool() 转换为布尔类型
 3.7 bin() 转换为二进制
 3.8 hex() 转换为十六进制
 3.9 oct() 转换为八进制
 3.10 list() 转换为列表
 3.11 tuple() 转换为元组
 3.12 dict() 转换为字典
 3.13 bytes() 转换为字节类型 encoding='utf-8' 编码
4 序列操作
    4.1 all() 结果为 bool 类型用于判断给定的可迭代参数iterable中的所有元素是否都为TRUE，如果是返回True，否则返回False，除了是0 、空、None、False的元素都是True 所有元素都为True 结果才为True
    4.2 any() 结果为 bool 类型用于判断给定的可迭代参数iterable中的所有元素是否都为False，如果是返回False，否则返回True，除了是0 、空、None、False的元素都是True 只要有一个元素为True 结果就为True
    4.3 sorted() 对可迭代对象进行排序 sorted(iterable, key=None, reverse=False) key为排序规则 reverse为True 降序 sort()只是能为列表排序
        sorted()、sort() 区别 前者返回一个新的可列表，不在原有对象上进行修改，后者则是在原有列表上进行修改，返回已排序的列表
    4.4 reserse()
    4.5 range()
    4.6 zip() 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*号操作符，可以将元组解压为列表
    4.7 enumerrate() 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中
5 set集合 
    5.1 set() 创建一个无序不重复元素集合，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等,特点：不支持索引和切片
    5.2 add() 为集合添加元素
    5.3 update() 修改集合
    5.4 remove() 删除集合中的元素
    5.5 clear() 清空集合
    5.6 pop() 随机删除集合中的一个元素
    5.7 discard() 删除集合中指定的元素
    5.8 copy() 复制集合
    5.9 difference() 差集
    5.10 difference_update() 差集更新
    5.11 intersection() 交集
    5.12 intersection_update() 交集更新
    5.13 isdisjoint() 判断两个集合是否包含相同的元素，如果没有返回True，否则返回False
    5.14 issubset() 判断指定集合是否为该方法参数集合的子集
    5.15 issuperset() 判断该方法的参数集合是否为指定集合的子集
    5.16 symmetric_difference() 返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素
    5.17 symmetric_difference_update() 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
    5.18 union() 返回两个集合的并集


'''
print(abs(-1))
print(round(1.2324, 3))
print(pow(2,2))
print(max((1,2,4,6,7)))
print(max([10,30,60]))
print(max(20,20))
print(sum((12,34789)))
print(sum([1,2], 3))
print(all([1,23,4,True]))
print(all([1,0]))
print(all([None,1]))
print(all('你好'))
print(all(()))
print(any(()))
print(any([None,1]))
egList = [12, 32, 34, 23,23,45,654,2,121]
egList.sort()
print(egList)
print(sorted(egList,reverse = True))
egTuple = (12, 32, 34, 23,23,45,654,2,121)
print(sorted(egTuple, reverse = False))
print(type(sorted(egTuple, reverse = False)))
str = 'niho huiahdidiuweuwiehw'
print(sorted(str))
zipList1 = ['mame', 'age', 'esx', 'liek']
zipList2 = ['mia', 18, '女', 'butiful']
print(list(zip(zipList1)))
print(list(zip(zipList1, zipList2)))
zipList3 = ['mame', 'age', 'esx', 'liek']
zipList4 = ['mia', 18, '女']
zipList5 = ['nihao']
print(list(zip(zipList3, zipList4, zipList5)))
'''
def printBookInfo():
    打印图书信息
    books = [] # 存储图书信息
    id =  input('请输入书籍编号(每个标号以空格分隔)：')
    bookName = input('请输入书籍名称(每个名称以空格分隔)：')
    author = input('请输入作者名称(每个作者以空格分隔)：')
    bookPos = input('请输入书籍位置(每个位置以空格分隔)：')
    bookPrices = input('请输入书籍价格(每个价格以空格分隔)：')
    idList = id.split(' ')
    bookNameList = bookName.split(' ')
    authorList = author.split(' ')
    bookPosList = bookPos.split(' ')
    bookPricesList = bookPrices.split(' ')
    printBookInfo = zip(idList, bookNameList, authorList, bookPosList, bookPricesList)
    for book in printBookInfo:
        books.append(book)
    print(books)
printBookInfo()
'''
# 创建集合
set1 = {1,2,3,4,5,6,7,8,9,0}
print(type(set1))
# 添加操作
set1.add('mia')
print(set1)
set1.clear()
print(set1)
setA = {'mia', 12, 'cc',  'yuyue', '爱你哟'}
setB = {'mia', 12, 'cc',  'yuyue', 'haha'}
# 求差集
print(setA.difference(setB))
print(setA - setB)
print(setB.difference(setA))
print(setB - setA)
# 求交集
print(setA.intersection(setB))
print(setA & setB)
# 求并集
print(setA.union(setB))
print(setA |setB)
print(setA.pop()) #从集合中拿一个数据并且删除
print(setA)
# 移除指定的元素
setA.discard('cc')
print(setA)
# 更新集合 将集合B中的元素添加到集合A中
setA.update(setB)
print(setA)
print(divmod(10, 3))
