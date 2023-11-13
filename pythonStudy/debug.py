'''
1 猜年龄小游戏，有三点需求
    1.1 允许用户最多尝试三次
    1.2 每尝试三次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或者y，就继续让其猜三次，以此往复，如果回答N或者n，就退出程序
    1.3 猜对了，就直接退出
'''
import random
randomAge = random.randint(17, 19)
times = 1
while times <= 1:
    for i in range(1,4):
        age = int(input("请输入您猜测的年龄："))
        if age != randomAge:
            i += 1 
        elif age == randomAge:
            print("恭喜您猜对了！")
            times = 2
            break
    else:
        print("您三次还没猜对，请问是否继续玩？答Y或者y：继续，答N或者n：退出")
        answer = input("请输入您的答案：")
        if answer == "Y" or answer == "y":
            times = 1
        elif answer == "N" or answer == "n":
            break
    