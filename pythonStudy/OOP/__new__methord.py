'''
创建对象 __new__
1 作用：创建并返回一个对象，调用一次__new__方法，就会创建一个对象
2 用途：__new__实例化对象的时候使用
'''
class Animal:
    def __init__(self):
        self.color = '红色'
    #在python中 如果不重写__new__ 默认结构如下
    def __new__(cls, *args, **kwargs):
        return super.__new__(cls, *args, **kwargs)
        
tigger = Animal()
print(tigger.color)
