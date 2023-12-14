'''
OS模块 对文件进行操作
1 




'''
import os
import shutil
#修改文件名称
#print(os.rename('D:\OS\Test\mia.txt','D:\OS\Test\mia.chen.txt'))# src：源文件path+name，dst新文件path+修改后name
# 文件删除
#os.remove('D:\OS\Test\mia1.txt')
#创建文件夹
#当前目录
#os.mkdir('mia.chen1')
#删除文件夹
# os.rmdir('mia.chen1')
 # 指定路径  注意：只能创建一级目录
#os.mkdir('D:\OS\Test\mia.chenFile')
#删除指定目录的文件夹 只能删除空目录
#os.rmdir('D:\OS\Test\mia.chenFile')
#创建多级目录
#os.makedirs('D:\OS\Test\File\mia.chen')
#删除非空目录  多级删除
#shutil.rmtree('D:\OS\Test\File')
# 打印获取当前目录位置
#print(os.getcwd())
# 路径拼接 
#print(os.path)
#os.path.join(os.getcwd(), 'OOP')
# print(os.listdir('D:\OS'))
# 获取文件目录
#print(os.scandir('D:/OS'))
# with os.scandir('D:/OS') as fileList:
#     for file in fileList:
#         print(file.name)
basePath = 'd:/'
#判断文件
# for entry in os.listdir(basePath):
#     if os.path.isfile(os.path.join(basePath, entry)):
#         print(entry)
#判断目录
for entry in os.listdir(basePath):
    if os.path.isdir(os.path.join(basePath, entry)):
        print(entry)

