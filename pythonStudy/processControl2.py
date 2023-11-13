'''
流程控制学习
流程：计算机代码执行的顺序
流程控制：对计算机代码执行顺序进行有效的管理
控制流程的分类
1、顺序流程：就是代码一种自上而下的执行结构，也是python默认的流程
2、选择流程/分支流程：根据在某一步的判断，有选择地去执行相应的逻辑的一种结构
    2.1、单分支
        if 表达式：
            代码块1
            代码块21
            ......
    2.2、双分支
        if 条件表达式：
            代码块1
            代码块2
            ......
        else：
            代码块1
            代码块2
            ......
    2.3、多分支
        if 条件表达式1：
            代码块1
            代码块2
            ......
        elif 条件表达式2：
            代码块1
            代码块2
            ......
        elif 条件表达式3：
            代码块1
            代码块2
            ......
        else：
            代码块1
            代码块2
            ......
3、循环流程：在一定的条件下，一直重复的去执行某一段代码的逻辑
    3.1、while 条件表达式：
        代码块1
        代码块2
        ......
    3.2、for 变量 in 集合对象/可迭代对象：
        代码块1
        代码块2
        ......
1、if-else语句
2、while 循环
3、for循环
4、break、contine
5、多条件与短路运算
'''
# 1、if-else语句
    # 1.1、单分支 
'''
if 条件表达式：
    代码块
    .....
'''
score = int(input("请输入成绩："))
if score >= 80:
    print("成绩优秀")
elif score >= 60 and socre < 80:
    print("成绩合格")
else:
    print("成绩不合格")
'''
多分支学习
！！！注意特征：
1.1 只要满足一个其中一个分支，就会退出本层if语句结构/必然执行一个分支
1.2 至少有两种情况可以选择
1.3 elif后面必须写上条件和语句
1.4 else时选配，根据实际情况选择是否需要
if 条件表达式1:
    代码块1
    代码块2
    ......
elif 条件表达式2:
    代码块1
    代码块2
    ......
elif 条件表达式3:
    代码块1
    代码块2
    ......
else:
    代码块
'''
score = int(input("请输入分数："))
if score > 90:
    print("您的成绩为%d，等级为A"%score)
elif score > 80 and score <= 90:
    print("您的分数为.{},等级为B",format(score))
elif score > 60 and score <= 80:
    print("您的分数为.{},等级为C",format(score))
else:
    print("您的等级为D,暂不展示具体分数")
'''
循环控制学习
1 while循环
    1.1 whil循环语法格式
    while 条件表达式:
        代码块
2 语法特定
    2.1 初始值
    2.2 条件表达式
    2.3 变量的自增或者自减[循环体内的计数变量]
3 使用条件
    循环次数往往不确定，是依靠循环条件的结束的
4 目的
    使代码重复利用
'''

#输出1~100的数字
i = 1
while i <= 100:
    print(i)
    i += 1
print("循环结束")
#输出1~100之间的偶数
j = 1
while j <= 100:
    if j % 2 == 0:
        print(j)
    j += 1
print("循环结束")
#输出1~ 100之间的奇数
k = 1
while k <= 100:
    if k % 2 == 1:
        print("奇数为：{}".format(k))
    k += 1
print("循环结束")
#猜拳游戏
import random
# 出拳
player = int(input("公主请出拳：(0--石头，1--剪刀，2--布)"))
computer = random.randint(0, 2)
# 游戏次数
index = int(input("亲输入游戏次数："))
a = 0
while a < index:
    # 判断输赢
    if player == 0 and computer == 1:
        print("公主您赢了~") 
    elif player == 1 and computer == 2:
        print("公主您赢了~")
    elif player == 2 and computer ==0:
        print("公主您赢了~")
    elif player == 0 and computer == 0 or player ==1 and computer == 1 or player == 2 and computer ==2:
        print("棋逢对手，公主您和我平局了~")
    else:
        print("公主您输了！")
    a += 1
print("游戏结束一共玩了{}次游戏".format(index))
#循环嵌套打印9X9乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("{}X{}={}\t".format(row, col, row*col), end = "")
        col += 1
    print()
    row += 1
##9*9乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('{}X{}={}\t'.format(i, j, i*j), end="")
        j += 1
    print()
    i+=1
# 打印直接三角形
row1 = 1
while row1 <= 7:
    col= 1
    while col <= row1:
        print("*"/t, end="")
        col += 1
    print()
    row1 += 1
# 打印倒立的直角三角形
row2 = 7
while row2 >= 1:
    col2 = 1
    while col2 <= row2:
        print("*",end = "\t")
        col2 += 1
    print()
    row2 -= 1
# 打印等腰三角形
row3 = 1
while row3 <= 5:
    col3 = 1
    while col3 <= 5-row3:
        print(" ",end= "")
        col3 += 1
    col4 = 1
    while col4 <= 2 * ro3 - 1:
        print("*",end = " ")
        col4 += 1
    print()
    row3 += 1
'''
for循环
代码格式：
for 临时变量 in 序列:
    代码块1
    代码块2
    ......
特点：遍历操作，一次的取集合容器中的每个值
'''
#示例1
nameObject = "mia.chen"
for i in nameObject:
    print(i)
'''
range()函数：此函数可以生成一个数据集合列表
说明：
    1 range(起始，结束，步长) 步长不能为0
    1.1 起始：默认为0
    1.2 步长：默认为1
    1.3 结束：不包含结束值
''' 
'''
break、contiune的学习
1 break：代表中断结束，满足条件直接结束本层循环
2 continue：结束本次循环，继续进行下次循环(当continue的条件满足的时候，本次循环剩下的语句不在执行，直接进行下一次循环)
'''
# break eg:计算1~50的累加和，当大于200时循环结束
sum = 0
for item in range(1, 51):
    if sum > 200:
        break
    sum += item
    print("sum = {}".format(sum))
#continue eg:求出奇数
for item1 in range(1, 51):
    if item1 % 2 == 0:
        continue
    print(item1)
#break eg : 遍历到“m”时结束循环
str1 = "我是mia.chen"
for item2 in  str1:
    if item2 == "m":
        break
    print(item2, end = "")
#break eg : 不遍历“m”
str1 = "我是mia.chen"
for item2 in  str1:
    if item2 == "m":
        continue
    print(item2)
#使用for进行9*9乘法表输出
for rowFor in range(1,10):
    for colFor in range(1, rowFor):
        print("{}X{}={}/t",format(rowFor, colFor, colFor*rowFor), end = " ")
    print()
#其他的循环结构 --- 注意事项
# for ..... else
for item in range(1, 11):
    print(item, end = " ")
    if item ==5:
        break
else:
    print("上面的循环只要出现break，那么else就不会执行了")
#
# while ..... else
#练习题：
'''
1 猜年龄小游戏，有三点需求
    1.1 允许用户最多尝试三次
    1.2 每尝试三次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或者y，就继续让其猜三次，以此往复，如果回答N或者n，就退出程序
    1.3 猜对了，就直接退出
2 小王身高1.75，体重80.5kg，根据BMI公式（体重除以身高的平方）帮小王计算他的BMI指数，并根据BMI指数：
    低于18.5：过轻
    18.5-25：正常
    25-28：过重
    28-32：肥胖
    高于32：严重肥胖
用if-elif判断并打印结果
'''
#1 猜年龄小游戏
times = 1
import random
randomAge = random.randint(17, 19)
while times <= 3:
    age = int(input("请输入您猜的年龄：")) 
    if age == randomAge:
        print("恭喜您猜对了！")
        break
    elif age < randomAge or age > randomAge:
        times += 1
print("您三次还没猜对，请问是否继续玩？答Y或者y：继续，答N或者n：退出")
answer =input("请输入您的答案：")
timesAnswer = 1
if answer == "Y" or answer == "y":
    while timesAnswer <= 3:
        age = int(input("请输入您猜的年龄：")) 
        if age == randomAge:
            print("恭喜您猜对了！")
            break
        elif age < randomAge or age > randomAge:
            timesAnswer += 1
elif answer == "N" or answer == "n":
    print("退出程序")
