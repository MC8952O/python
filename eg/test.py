'''
argparse模块
1 作用：轻松编写用户友好的命令行界面，该程序定义了需要的参数，argparse 并将找出如何解析这些参数sys.argv。argparse 还会自动申城帮助和用法信息，并在用户给出程序无效参数
2 参数说明
    2.1 prog：文件名，默认为sys.argv[0], 用来在help信息种描述程序的名称。
    2.2 usage：描述程序用途的字符串
    2.3 description：help信息前提示的信息
    2.4 epilog：help信息之后显示的信息
    2.5 parents：由ArgumentParser对象组成的列表，他们的arguments选择会被包含到新的ArgumParser对象中，累死继承
    2.6 formatter clss: help信息输出的格式，为了美观
    2.7 perifx chars： 参数前缀，默认为‘-’，最好不要修改
    2.8 add help: 是否增加-h/hel选项，默认为True，一般help信息都是必学的，设为false时，help信息不在提示 -h -help信息
    2.9 argument default： -(default:None) 设置一个全局的选项的缺省值，一般每个选项单独设置，基本没用
'''
import sys
import argparse
'''print('参数个数为：', len(sys.argv), '个参数')
print('参数列表', str(sys.argv[1:]))'''
parse = argparse.ArgumentParser(prog = '系统登录', usage= '%(prog)s [options] usage', 
                                description='my - 编写命令函执行文件', epilog= 'my - epilog')
# 添加位置参数【必选参数】
parse.add_argument('loginType', type = str, help = '系统登录类型')
#添加可选参数 使用‘--’进行表示
parse.add_argument('--user', dest = 'user', action = 'append', type = str, help= '用户名')
parse.add_argument('--pw', dest = 'psswordr', type = str, help= '密码')
#打印帮助文档
#print(parse.print_help())
#解析参数
result = parse.parse_args()
print(result)
#登录mysql 
if (result.user == 'root' and result.pwwword == 'Cxqcxq123@@.'):
    print('登录成功')
else:
    print('登录失败')