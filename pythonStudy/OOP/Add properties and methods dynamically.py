'''
动态添加属性和方法
'''
import types #导入添加方法的库
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '{}今年{}岁'.format(self.name, self.age)
student1 = Student('mia', 18)
student1.weight = 45 #动态添加属性
student1.hight = 160 #动态添加属性
Student.school = '鞍山师范学院' #动态添加类属性
@classmethod
def class_test(cls): #绑定类方法
    print('----------类方法-----------------')
'''
动态添加实例方法
'''
def printInfo(self):
    print('{}体重是：{}身高是：{}在{}上大学'.format(self.name, self.weight, self.hight, Student.school))
student1.print_stu1_Info = types.MethodType(printInfo, student1)
student1.print_stu1_Info()
# 动态添加类方法
Student.TestclassMthod = class_test
Student.TestclassMthod()
# 动态添加静态方法
@staticmethod
def staticeMethod():
    print('---------------静态方法-------------')
Student.testStaticMthod = staticeMethod
Student.testStaticMthod()
#print(str(student1.weight) +'------'+ str(student1.hight))
print(student1)
#实例访问动态类方法
student1.TestclassMthod()
student2 = Student('情绪稳定', 18)
#print(student2.weight) #报错 student2 没有weight属性
print(student2)
print(student1.school)
'''
动态添加实例方法
'''
# def printInfo(self):
#     print('{}体重是：{}身高是：{}在{}上大学'.format(self.name, self.weight, Student.school))
