'''
魔术方法学习
1. __srt__ 直接打印对象，输出结果为一串类似id地址的信息
2.__new__   每调用一次就会生成一个新的对象


'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.age)
    def __new__(cls, *args, **kwargs):
        print('new方法被调用')
        return object.__new__(cls)
works = Person('XM', 20)
print(works)