'''
re模块其它方法的学习
1 compile将正则表达式模式编写成一个正则表达式对象
2 search() 在全文中进行匹配，匹配到就返回
'''

import re
#将正则表达式 装换为reobj对象
reobj = re.compile('\d{4}')
#使用reobj对象
res = reobj.match('12322223')
print(res.group()) #1232
strA = '爱国敬业民主法制,爱国敬业民主法制'
res = re.search('爱国',strA)
print(res)
print(res.group())