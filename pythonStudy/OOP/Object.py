class Animal():
    def __init__(self, name, age, sex):
        #self.name = 'yuyue'
        #self.age = 18
        #self.sex = '女'
        self.name = name
        self.age = age
        self.sex = sex
    def run(self):
        print('动物会跑')
'''dog = Animal()
dog.name = 'yuyue'
dog.age =  26
dog.sex = '男'
dog.run()
cat = Animal()
cat.name = 'mia'
cat.nge = 18
cat.sex = '女'
cat.run()
print(dog.name, dog.age, dog.sex)'''
'''dog = Animal()
#输出初始值
print(dog.name, dog.age, dog.sex)
#修改初始值
dog.name = 'mia.chen'
dog.age = 18
dog.sex = '女'
print(dog.name, dog.age, dog.sex)'''
#创建对象
cat = Animal('mia.chen', 18, '女')
print(cat.name, cat.age, cat.sex)
class Dog:
    '''小狗类'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set(self):
        '''小狗坐的行为'''
        print(self.name.title()+'is now setting')
    def roll_over(self):
        '''小狗打滚的行为'''
        print(self.name.title()+'roll_over')
huahua = Dog('huahua', 2)
print(huahua.name.title())
huahua.set()
huahua.roll_over()
class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        number_served = 0
    def descrile_restaurant(self):
        print('{}是一家干净卫生的餐厅'.format(self.restaurant_name))
        print('{}是{}的餐厅'.format(self.restaurant_name, self.cuisine_type))
    def open_restaurant(self):
        print('{}营业时间为：8：00AM'.format(self.restaurant_name))
    def updat_served(self,date_number):
        self.date = date_number
    def served_add(self, add):
        self.number_served+= add
    def __str__(self):
        return '{}当前就餐人数为：{}'.format(self.restaurant_name, self.number_served)
KFC = Restaurant('KFC','works')
print('{}{}'.format(KFC.restaurant_name,KFC.cuisine_type))
KFC.descrile_restaurant()
KFC.open_restaurant()
reataurant = Restaurant('YF_KFC', 'YF_works')
reataurant.number_served = 110
print(reataurant.updat_served(20))
Restaurant.set_number_served(10)
print(reataurant)
MDL = Restaurant('MDL', 'works_w')
MDL.descrile_restaurant()
HLS = Restaurant('HLS', '窜西')
HLS.descrile_restaurant()
class User:
    def __init__(self,first_name, last_name,age, sex, employee_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.employee_id= employee_id
    def describle_user(self):
        print('姓名：{}{}\n年龄：{}\n性别：{}\n工号：{}'.format(self.first_name, self.last_name, self.age , self.sex, self.employee_id))
    def greet_user(self):
        print('{}早上好！'.format(self.last_name))
MIA = User('Chen', 'MIA', 18, '女', '2203005')
MIA.describle_user()
MIA.greet_user()