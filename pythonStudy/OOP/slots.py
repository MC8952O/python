'''
__slots__学习
作用：
    限制要添加的实例属性
    节约内存空间
在继承关系中使用 __slots__
    子类未声明 __slots__时，那么是不会继承父类的slots，此时子类可以随意赋值
    子类申明了 __slots__时，继承父类的__slots__,也就是子类__slots__的范围未 自身的slots+父类的slots
'''
class Student:
    __slots__ = ('name', 'age')
    def __str__(self):
        return '{}...{}'.format(self.name, self.age)
xw = Student()
xw.name = '小王'
xw.age = 20
#xw.score = 89
#print(xw.__dict__) #所有可用属性存贮在该字典中,但是占用内存空间较大， 使用slots之后，student累实例已经不能创建不在slots定义的属性，同时 实例中不存在__dict__魔术方法
print(xw)
class SubStudent(Student):
    pass
mia = SubStudent()
mia.sex = 'nv'
mia.works = '测试工程师'
print(mia.sex,mia.works)