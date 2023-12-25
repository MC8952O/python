'''
变量命名规则：
1 只能包含字母、数字、"_" ;不能以数字开头
2 变量名不能包含空格，单词之间使用"_"连接
3 不能使用python关键字  
4 字符串
    4.1 字符串连接 +
    4.2 字符串 转大写 upper()   
    4.3 字符串 转小写 lower()     
    4.4 字符串 首字母大写 title()  
    4.5 字符串 去右边空格 rstrip()  
    4.6 字符串 去左边空格 lstrip()   
    4.7 字符串 去所有空格 strip()                                                                                                                                                                        
'''
message = 'hello python'
print(message)
message = 'hello word'
print(message)
name = 'ada loveace'
print(name.title())
print(name.upper())
print(name.lower())
first_name = 'mia'
last_name = 'chen'
name = first_name +'.'+ last_name
print(name.title())
print('\t{}'.format(name))
print('{}\n'.format(name))
rstripstr = '你好     '
print(rstripstr)
stripstr = rstripstr.rstrip()
print(rstripstr)
tryName = 'Eric'
print('"Hello{},would you like to learn some Python today"'.format(tryName))
tryname = 'mia Chen'
print(tryname.lower())
print(tryname.upper())
print(tryname.title())
abertperson = 'Einstein'
abertSay  = "A person who never made a mistake never tried anything"
print('Albert {} once said,"{}"'.format(abertperson, abertSay))
personName = ' \tmia chen '
print(personName)
print(personName.rstrip())
print(personName.lstrip())
print(personName.strip())
age = 23
message = "Happy " + str(age )+ "re Birthday"
print(message)

