'''文件操作
文件默认编码格式为GPK，可以设置为utf-8
步骤：
1 打开文件： open('文件路径',类型)
2 
'''
'''#打开文件
fObj = open('D:\OS\Test\mia.txt', 'r', encoding = 'utf-8') # W模式 若文件已存在，会覆盖文档见以及内容，若不存在则新增
#读/写内容
fObj.write('你好，我是mia，正在学习python')
fObj.write('热爱学习，成为自动化测试')
fObj.close()
print('关闭的时候会保存文件内容')'''
#以二进制方式写数据
#wb
'''fObj = open('D:\OS\Test\mia.txt', 'wb') # Str---bytes
fObj.write('我是mia我热爱学习'. encode('utf-8'))
fObj.close()'''
#追加.新内容会写到已存在文件末尾
'''fObj = open('D:\OS\Test\mia1.txt', 'ab')
fObj.write('mia,你好。\r\n'.encode('utf-8'))
fObj.write('热爱学习，没毛病。'.encode('utf-8'))
fObj.close()
'''
#读文件 'r'
# read() 读取所有数据 多次读数据时会从上次一次读的位置开始继续往下读
'''fObj = open('D:\OS\Test\mia.txt', 'r', encoding='utf-8')
result = fObj.readlines()
print(result)
# 读取n个 read(n)
print(fObj.read(2))
# 读一行 readlin()
print(fObj.readline())
# readlines 读所n行
print(fObj.readlines(n))
# readlines 读所有行
print(fObj.readlines())
fObj.close()'''
# rb 以二进制性质只读
'''f = open('D:\OS\Test\mia1.txt', 'rb')
data = f.read()
print(data)
f.close()'''
# with关键字 自动关闭文件 自动释放打开关联的对象
with open('D:\OS\Test\mia2.txt', 'w') as f:
    f.write('woshi mia')
