'''
私有化属性学习
1 定义：把特定的一个属性隐藏起来，不能让类的外部及进行直接调用
2 不允许派生类继承该属性
3 私有化的实列属性不能在外部直接访问，可以在类当内部随意使用
4 子类不能继承父类的私有化属性
5 私有化属性定义方式：__属性名称
'''
class Person:
    def __init__(self):
        '''构造函数'''
        #私有化name属性
        self.__name = 'mia'
        self.age = 30
    def __str__(self):
        return '{} up'.format(self.__name)
#xl = Person()
#print(xl)
class Students(Person):
    def peintInfo(self):
        print(self.__name)
    pass
xh = Students()
print(xh)