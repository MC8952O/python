'''
正则表达式
1 使用re模块进行正则表达式
2 match(pattern, string, flags):尝试从字符串起始位置匹配一个规则，成功返回match对象，否则返回None，使用group()接受成功的字符串
    pattern：匹配正则的表达式
    string：要比配的字符串
    flags：标志符，用于控制正则表达式的匹配方式，大小写。多行等
    group(num)匹配对象函数来获取匹配表达式
    groups()
    匹配以'指定字符'开头的字符串
3 常用匹配规则 字符
    1. . 匹配任意1个字符除了换行符\n
    2. [abc] 匹配abc中的任意一个符号
    3. \d 匹配数字
    4. \D 匹配非数字
    5. \w 匹配单词
    6. \W 匹配非单词
4 3 常用匹配规则 匹配字符数量
    1 * 匹配前一个字符出现0或无数次，可有可无
    2 + 匹配前一个字符出现1次或者无数次 至少有1次
    3 \? 匹配前一个字符出现1次或者0次，要么有要么没有
    4 {m}匹配前一个字符出现m次
    5 {m,}匹配前一个字符至少出现m次
    6 {n, m} 匹配前一个字符出现你到m次、
5 分组匹配
    1 |：匹配左右两边任一表达式 或
    2 (ab)：分组匹配，将括号中中的字符作为一个分组
    3 \num 引用分组num匹配到的字符串
    4   (?P<名字>) 分组起别名
        (?P = name)引用别为name分组匹配到的字符串

'''
import re
# strA = 'I am mia ,I learn python ye,hello python'
# res = re.match('I am', strA, re.I)
'''
match()用法演示
res = re.match('(.*) python (.*?).*', strA, re.I|re.M)
if res:
    print(res)
    print('匹配成功')
    print(res.group(1))
    print(res.group(2))
    print(res.groups())
else:
    print('匹配失败')
    print(res.group())'''
'''
# 匹配规则'.'
res = re.match('..',strA)
print(res.group())
'''
# [] 匹配集合中的任意一个字符
# res = re.match('[a-z]', strA)
'''for i in strA:
    res = re.match('[a]', i)
    print(res.group())'''
'''strB = 'plan'
res= re.match('[acp]', strB)
if res:
    print('匹配成功')
    print(res.group())
else:
    print('匹配失败')'''
string = 'abcdefghijklmnopqrstuvwxyz9999'
res = re.search('(abcdefghi|jklmnopqrstuvwxyz9999)',string)
print(res.group())
strC = '12321-123456'
resC = re.match('([^-]*)-(\d*)',strC)
print(resC.group(0))
print(resC.group(1))
print(resC.group(2))
htmlTag = '<html><h1>测试数据</h1></html>'
resD = re.search(r'<(.+)><(.+)>(.+)</\2></\1>', htmlTag)
print(resD.group(1))
print(resD.group(2))
print(resD.group(3))
# 使用起别名的方式
htmlTag1 = '<div><h1>www.baidu.com</h1></div>'
resF = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>', htmlTag1)
print(resF.group(1))
print(resF.group(2))
