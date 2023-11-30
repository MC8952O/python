'''
1 析构方法
    1.1 __del__方法：当对象被删除或者被销毁时，python解释器会默认调用__del__方法
    1.2 当在某个作用域下面，没有被使用【引用】的情况下，解释器会默认调用__del__方法，进行删除释放内存空间
2 单继承
3 多继承
4 重写父类方法
5 调用父类方法
7 多态
8 类属性和实例属性
9 类方法和静态方法
'''
class Animal:
    def __init__(self,name, age):
        '''构造初始化方法'''
        self.anme = name
        self.age = age
        print('Animal类的构造方法被调用')
    def __del__(self):
        print('Animal类的析构方法被调用,对象被销毁')
        print('{}被销毁了'.format(self.name))
cat = Animal('ErFu', 1.5)
print('*'*20)
input('程序暂停中，等待输入')
dog = Animal('顿顿', 0.7)
del dog
print(cat.name)
input('请等待输入')
