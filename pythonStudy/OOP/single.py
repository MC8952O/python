'''
单例模式
1 定义：是一种常用的软件设计模式
2 目的： 确保某一个类只有一个实例存在
'''
#创建一个单例对象 推荐基于__new__实现
class Dbdatabase:
    def __new__(cls, *args, **kwargs):
        #cls._instance = cls.__new__(cls) #不能使用自身的new方法，容易造成一个深度递归，堆栈溢出，应该调用父类的new方法
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
mysql = Dbdatabase()
print(id(mysql))
sqlsever = Dbdatabase()
print(id(sqlsever))
