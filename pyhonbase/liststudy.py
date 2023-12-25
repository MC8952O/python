'''
列表的学习
1 概念 ：由一系列特定顺序排列的元素组成 用[]表示 ，元素之间用"," 列表是有序集合

'''
bicycles = ['trek', 'cannondale', 'redline', 'specilized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-2])
message = 'My first bicycles was a '+ bicycles[0].title()+'!'
print(message)
names = ['mia1','mia2', 'mia3', 'mia4', 'mia5']
for name in names:
    print('{}你好'.format(name))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                