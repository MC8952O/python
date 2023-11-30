class Animal:
    '''
    定义动物类
    '''
    def run(self, name, distance):
        self.name  = name
        self.distance = distance
        print('{}跑了{}米'.format(self.name, self.distance))
        '''
        run实例方法
        '''
        #print('self内存地址是：{}'.format(id(self)))
dog = Animal()
#print('dog内存地址是：{}'.format(id(dog)))
dog.run('shorthair', '100m')