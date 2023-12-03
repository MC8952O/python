'''
多态学习
1 定义：定义时的类型和运行时的类型不一样，此时就成为多态，同一个方法对不同的子类有不同德子类对象有不同的表现形式
2 要素：继承、重写、父类引用指向子类对象
3 作用:增加程序的灵活性
4 类属性和实例属性
    4.1 类属性：就是类对象拥有德属性，他被所有类对象的实例对象所共有，类对象和是实例对象都可以访问类属性
    4.2 实例属性：实例对象所拥有的属性，只能通过实例对象来访问，不能通过类对象访问
    4.3 类属性修改：只能通过类对象修改，实例对象不能修改 
5 类方法与实例方法
    5.1 类方法：类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数，一般可以通过类对象和实例对象去访问
    5.2 实例方法：实例对象所拥有的方法，只有实例对象可以访问，一般通过实例对象去访问
6 静态方法
    6.1 静态方法：不需要实例对象和类对象就可以访问的方法，需要通过修饰器@staticmethod来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象（形参没有self和cls）
    6.2 为什么需要静态方法：静态方法一般用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作
'''
import time
class Animal:
    '''基类'''
    def say(self):
        '''说话'''
        print('我是动物：')
class Dog(Animal):
    '''子类(派生类)：鸭子'''
    def say(self):
        '''重写父类的方法'''
        print('我是小狗：')
class Duck(Animal):
    '''子类(派生类)：鸭子'''
    def say(self):
        '''重写父类的方法'''
        print('我是小鸭子：')
class Bird(Animal):
    '''子类(派生类)：小鸟'''
    def say(self):
        '''重写父类的方法'''
        print('我是小鸟：')
def commonInvoke(obj):
    '''公共方法'''
    obj.say()
listAniamls = [Dog(),Duck(),Bird()]
for item in listAniamls:
    '''循环调用函数'''
    commonInvoke(item)

'''huashen = Dog()
huashen.say()
duck = Duck()
duck.say()'''
class Student:
    '''学生类'''
    # 类属性
    name = '张三' # 类属性 就是student对象所拥有的
    def __init__(self, age): #实例属性
        self.age = age
lm = Student(18)
Student.name = '王五'
lm.name = '李四'  #通过对象访问类属性
print(lm.name) 
print(lm.age) #通过对象访问实例属性
print('--------通过类对象Student访问属name---------')
print(Student.name)#通过类对象修改属性
Student.name = '王五'
print(lm.name)
class People:
    country = 'The UK' #类属性
    def __init__(self,name):
        self.name = name
    @classmethod
    def getCountry(cls):
        '''类方法'''
        return cls.country # 访问类属性
    @classmethod
    def changeCountry(cls, data):
        '''使用类方法修改类属性'''
        cls.country = data
    @staticmethod
    def getCountry():
        '''静态方法'''
        return People.country
    @staticmethod
    def gettime():
        '''获取时间静态方法'''
        return time.time()

print(People.getCountry()) # 通过类对象引用
#通过实例对象引用
mia = People('Mia.chen')
print('{}run往{}'.format(mia.name, mia.getCountry()))
#通过类对象修改属性
People.changeCountry('The USA')
print(People.country)
print('--------修改类属性---------')
#通过实例对象修改类属性
mia.changeCountry('China')
print('{}目前{}'.format(mia.name, mia.getCountry()))
print('--------类对象调用静态方法---------')
print(People.getCountry())
print('--------实例对象调用静态方法---------')
print(mia.getCountry)  #一般情况下不会通过实例访问静态方法
#调用静态方法获取时间
print(People.gettime())



