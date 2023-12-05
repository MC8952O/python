'''
'''
#定义小狗类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        '''小狗蹲下'''
        print('{}正在蹲下'.format(self.name))
    def roll_over(self):
        '''打滚'''
        print('{}在打滚'.format(self.name))
hbg = Dog('哈巴狗', 1)
hbg.sit()
hbg.roll_over()
print(hbg.name)
class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print('{}是{}'.format(self.restaurant_name, self.cuisine_type))
    def open_restaurant(self,time):
        print('{}的营业时间是{}'.format(self.restaurant_name, time))
restaurant = Restaurant('KFC', 'deepfry')
restaurant.describe_restaurant()
restaurant.open_restaurant('9:00')
MDL = Restaurant('麦当劳', 'deepfry')
MDL.describe_restaurant()
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print('姓名：{}{}\n年龄：{}\n'.format(self.first_name, self.last_name, self.age))
    def greet_user(self):
        print('{}欢迎您的到来'.format(self.last_name))
user = User('chen','mia',18)
user.describe_user()
user.greet_user()
class Car:
    '''汽车'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '''返回描述信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    def update_odometer(self,mileage):
        '''通过函数修改属性'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print('{}{}{}修改的里程数是：{}'.format(self.year, self.make, self.model, mileage))
        else:
            print('NO!')
    def increment_odometer(self, miles):
        '''增加行驶里程数'''
        self.odometer_reading += miles
    
    def read_odometer(self):
        '''打印行驶里程数'''
        print('{}{}{}行驶的里程数是：{}'.format(self.year, self.make, self.model, self.odometer_reading))
my_new_car = Car('audi', 'A4', 2016)
print(my_new_car.get_descriptive_name())
#修改属性的值
my_new_car.odometer_reading = 20
#通过方法修改属性
my_new_car.update_odometer(10)
print(my_new_car.odometer_reading)
my_new_car.read_odometer()
print('---------------------------------------------------------')
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(300000)
my_used_car.read_odometer()
my_used_car.increment_odometer(3000)
my_used_car.read_odometer()

