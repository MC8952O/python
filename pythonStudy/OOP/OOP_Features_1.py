class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        '''吃东西'''
        print('{}正在吃东西'.format(self.name))
    def drink(self):
        '''喝水'''
        print('{}喝水中'.format(self.name))
class Dog(Animal):
    def wwj(self):
        '''旺旺叫''' 
        print('{}正在旺旺叫'.format(self.name))
class Cat(Animal):
    def mmj(self):
        '''喵喵叫'''
        print('{}正在喵喵叫'.format(self.name))
xiaoHuang = Dog('小黄')
print(xiaoHuang.name)
xiaoHuang.eat()
xiaoHuang.drink()
xiaoHuang.wwj()
print('--------------小猫咪-----------------')
erFu = Cat('二福')
print(erFu.name)
erFu.eat()
erFu.drink()
erFu.mmj()
