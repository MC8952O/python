 
#1 猜年龄小游戏
import random
times = 1
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

for item in answer:
    if item == "Y" or item == "y":
        timesAnswer = 1
        while timesAnswer <= 3:
            age = int(input("请输入您猜的年龄：")) 
            if age == randomAge:
                print("恭喜您猜对了！")
                break
            elif age < randomAge or age > randomAge:
                timesAnswer += 1
    elif item == "N" or item == "n":
        print("退出程序")
        break
