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
            代码块2
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