'''
1 字符串及常用方法
    1.1 capitalize() 将字符串的第一个字符转换为大写
    1.2 endswtih() 检查字符串是否以指定的字符串结尾
    1.3 startswith() 检查字符串是否以指定的字符串开头
    1.4 find() 检测字符串中是否包含子字符串
    1.5 isalnum() 检测字符串是否由字母和数字组成
    1.6 isalpha() 检测字符串是否只由字母组成
    1.7 isdigit() 检测字符串是否只由数字组成
    1.8 islower() 检测字符串是否由小写字母组成
    1.9 join() 将列表中的字符串连接成一个字符串
    2.0 lower() 将字符串中的大写字母转换为小写字母
    2.1 upper() 将字符串中的小写字母转换为大写字母
    2.2 swapcase() 将字符串中的大小写字母进行转换
    2.3 lstrip() 删除字符串左侧的空白字符
    2.4 rstrip() 删除字符串右侧的空白字符
    2.5 strip() 删除字符串两侧的空白字符
    2.6 split() 将字符串按照指定的字符分割成列表
    2.7 title() 将字符串中的每个单词的首字母转换为大写
    2.8 replace(old, new, coount = None) 将字符串中的指定字符串替换为指定的字符串 old:被替换的字符串 new:替换的字符串 count:替换的次数,无表示全部替换
    2.9 count() 统计字符串中指定字符串出现的次数
2 列表及常用方法
3 元组及常用方法
4 字典及常用方法
5 共有操作
6 序列(集合)
    6.1 定义：就是一组按照顺序排列的值
    6.2 分类：字符串、列表、元组
    6.3 优点：支持索引和切片的操作
    6.4 特征: 第一个正索引为0，指向的是左端，第一个索引为负数时，指向的是右端
    6.5 切片: 可以根据下标获取序列兑现的任意部一部分 [start:end:step]  start:开始位置，end:结束位置，step:步长 默认为1
'''
# 1 字符串及常用方法
strTest1 = "hello python"
# 打印字符串
print(type(strTest1))
for i in strTest1:
    print(i, end = " ")
# 首字母大写
print("首字母大写：{}".format(strTest1.capitalize()))
# 去除空格
strTest2 = '   hello mia.chen   '
print('去除空格：{}'.format(strTest2.strip()))
strTest3 = '   hello mia.chen  '
print('去除左边空格：{}'.format(strTest3.lstrip()))
strTest4 = '   hello mia.chen  '
print('去除右边空格：{}'.format(strTest4.rstrip()))