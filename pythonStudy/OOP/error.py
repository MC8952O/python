'''
异常处理语法
try:
    可能出现错误的代码块
    # 用一个try代码块可以捕获多个不同类型的异常
except:
    出现错误后执行的代码块 
    #except:在捕获错误异常的时候，需要根据具体的错误类型来捕获的
else:
    没有出错的代码块
finally:
    不管有没有出错都要执行的代码
1 异常类 Exceptino: 可以捕获所有的异常，当出现的问题或者错误不确定的情况下，使用Exception
'''
# try:
#     print(b) #捕获异常的代码
#     li = [1, 2, 4]
#     print(li[10])
#     a = 10/0
#     print(a)
# except NameError as msg:
#     # 捕获异常后进行的处理
#     b = 9
#     print(b)
# except IndexError as msg:
#     print(msg)
# except ZeroDivisionError as msg:
#     print(msg)
# except Exception as result:
#     print(result)
# print('初次接触异常')
# print('开心异常处理')
def chu(s):
    return 10/int(s)
def mi(s):
    return  chu(s)*2
def main():
    try:
        mi('0')
    except  Exception as msg:
        print(msg)
main()
try:
    print('aa')
except Exception as msg:
    print(msg)
else:
    print('当try代码块没出现异常的情况下才会执行的代码')