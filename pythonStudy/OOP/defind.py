#自定义异常
class Toolongstr(Exception):
    def __init__(self, leng):
        self.leng = leng
    def __str__(self):
        return 'name不超过四个字符'
def name_test():
    name = input('请输入姓名:')
    try:
        if len(name) > 4:
            raise Toolongstr(len(name))
        else:
            print(name)
    except Toolongstr as msg:
        print(msg)
    finally:
        print('执行完毕')
name_test() 