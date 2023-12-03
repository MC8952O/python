'''
property方法学习
1 定义一个类属性，实现直接方法属性的形式去访问私有的属性


'''
class Person:
    def __init__(self):
        '''构造函数'''
        self.__age = 18 # 私有化属性
    # def get_age(self):
    #     return self.__age
    # def set_age(self, age):
    #     if age < 1:
    #         print('年龄不能小于0')
    #     else:
    #         self.__age = age
    #         return self.__age
    #实现方式1 property
    # age = property(get_age, set_age)       
    # 实现方式2 使用装饰器 @property
    @property #用装饰器添加属性标识
    #提供一个get方法
    def age(self):
        return self.__age
    #提供一个setter方法
    @age.setter
    def age(self, parms):
        if parms < 0:
            print('年龄不能小于0')
        else:
            self.__age = parms

person = Person()
#print(person.get_age()) # t通过调用方法实现对私有属性的访问
#print(person.set_age(21))# 通过实例方法调用 实现私有属性的设置
print(person.age) # 通过property方Z法直接调用私有化实例属性
person.age = 25
print(person.age)
#实现方式2： 通过装饰器 @property

