'''
编写一个程序将分钟转换为秒。
'''
'''inputMiunte = int(input('请输入需要转换的时间：'))
print('{}分钟转换后的时间为：{}s'.format(inputMiunte, inputMiunte*60))'''
'''
编写一个程序将字符串转换为整数
'''
'''inputStr = input('请输入一个字符串：')
print('{}转换后的整数为：{}'.format(inputStr, int(inputStr)),type(int(inputStr)))'''
'''eg = [1, 4 ,-10 ,-50 ,32 ,21]
print(len(eg))
a = 0
for i in range(len(eg)-1):
    for j in range(i+1,len(eg)):
        if eg[i] > eg[j]:
            a = eg[j]
            eg[j] = eg[i]
            eg[i] = a
print(eg[0])
print(eg[5])
print(eg[5] - eg[0])'''
'''eg = [1, 2 ,3]
print(eg[len(eg)-1])
print(type(eg[len(eg)-1]))'''
'''strA = 'ABC'
StrB = 'CDFE'
for i in strA:
    for j in StrB:
        if i == j:
            print(True)'''
#字符串首尾连接
'''strA = 'love pythontip'
print(strA[0:1]+strA[len(strA)-1])'''
# 单词是否为复数。
'''strA  = input('请输入一个单词：')
print(strA.endswith('s'))'''
#编写一个程序，用于在一组整数中找出唯一的数字。假设列表中只有一个唯一的数字。
'''egList = [1, 'mia', [1, 'mia', ('nihao')], (1,), {"name": 'mia'}]
for i in egList:
    if type(i) == int:
        print(i)'''
# 创建一个给定范围内的整数列表
'''intList = []
startElement  = int (input('请输入第一个数：'))
endElement = int(input('请输入最后一个数字：'))
for i in range(startElement+1, endElement):
    intList.append(i)
print(intList)
'''
#编写一个程序来判断一个数字是否为素数。
#素数：只能被1和自身整除的数
'''num  = int(input('请输入一个数字：'))
for i in range(2, num):
    if num % i == 0:
        print('{}不是素质'.format(num))
        break
    else:
        print('{}是素质'.format(num))
        break'''
#编写一个Python程序来计算字符串中元音字母的数量。
'''strA = input('请输入字符串：')
count = 0
for i in strA:
    if i in 'eaiou':
        count += 1
print(count)'''
'''num = int(input('请输入一个数字：'))
numList = []
for i in range(1, num+1):
    if num % i == 0:
       numList.append(i)
print(numList)'''
'''intNum = int((input('请输入一个数字：')))
intStr = str(intNum)
numList = []
for i in intStr:
    numList.append(i)
print(numList[::-1])'''
#编写一个Python程序来判断两个给定的字符串是否是错位
'''StrA = input('请输入字符串A:')
StrB= input('请输入字符串B:')
if len(StrA) != len(StrB):
    print(False)
else:
    for i in StrA:
        if i not in StrB:
            print(False)
        if StrA.count(i) != StrB.count(i):
            print(False)
        else:
            print(True)'''
'''StrA = input('请输入字符串：')
if StrA == StrA[::]:
    print(True)
else:
    print(False)'''
'''element = input('请输入数字：')
numList = [int(i) for i in str(element).split()]
sum = 0
integrable = 0
for j in numList:
    sum += j
    integrable *= j
if integrable / sum == 0:
    print(True)
else:
    print(False)'''
'''element = input('请输入数字：')
indexNum = int(input('请输入你需要查询第几小的数字：'))
numList = [int(i) for i in str(element).split()]
a = 0
for n in range(len(numList)-1):
    for j in range(n+1, len(numList)):
        if numList[n] > numList[j]:
            a = numList[j]
            numList[j] = numList[n]
            numList[n] = a
print(numList[indexNum-1])'''
# 用于求两个整数的最大公约数（GCD）。
'''numA = int(input('请输入一个整数：'))
numB = int(input('请输入一个整数：'))
i = 0
while i <= numA:
    if numA / i == 0:'''
'''def maxCommonDivisor(num1,num2):
    a = 0
    if num1 == num2:
        return num1
    elif num1 > num2:
        if num1 % num2 == 0:
            return num2
        elif num1 % num2 != 0:
            while num1 % num2 != 0:
                a = num1 % num2
                num1 = num2
                num2 = a
            return num2
    elif num1 < num2:
        if num2 % num1 ==0:
            return num1
        while num2 % num1 != 0:
            a = num2 % num1
            num2 = num1
            num1 = a
        return num1              
print(maxCommonDivisor(32,8))'''
'''def ends_with(string1, string2):
    if string1.endswith(string2):
        return True
    else:
        return False
print(ends_with('abc', 'bc'))
'''
'''def multiply_numbers_in_string(num_string):
    # 将字符串输入转换为列表
    num_list = list(map(int, num_string.split()))
    # 在此处编写你的代码
    integrable = 1
    for i in range(len(num_list)):
         integrable *= num_list[i]
    return integrable
# 获取输入字符串
num_string = input()
# 调用函数
print(multiply_numbers_in_string(num_string))'''
'''def is_string_isogram(word):
    # 将单词转换为小写
    word = word.lower()
    len1 = len(word)
    len2 = len(set(word))
    return len1 == len2
word = input('请输入字符：')
# 调用函数
print(is_string_isogram(word))'''
'''def count_binary_ones(num):
    # 此处写你的代码 
    egbin = bin(num)
    return egbin.count('1')
# 从标准输入读取一个整数
num = int(input())
# 调用函数
print(count_binary_ones(num))'''
def fibonacci_number(n):
    # 在此处编写你的代码
    # 1 1 2 3 5 8 13 21 34
    if n <= 1:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)
# 输入n的整数
n = 7
# 调用函数
print(fibonacci_number(n))
