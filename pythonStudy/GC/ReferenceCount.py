'''
python 垃圾回收机制
1 引用计数机制为主
    1 typedef struct object{
        int ob_refcnt;
        struct_typeobject * ob_type;
    }PyObject;
    2 缺点：
        2.1 维护引用计数会消耗资源
        2.2 循环引用 导致内存泄漏
2 标记清楚和分代收集辅
3 GC的主要任务
    3.1 为新生成的对象分布内存
    3.2 识别那些垃圾对象
    3.3 从垃圾对象那回收内存

'''
import gc
import sys
import psutil
import os
def showMenmSize(tag):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss/1024/1024
    print('{}创建对象内存使用了{}MB'.format(tag, memory))
# 验证循环使用的情况
def func():
    showMenmSize('初始化')
    a = [i for i in range(100000)]
    b = [i for i in range(10000)]
    a.append(b)
    b.append(a)
    # print(sys.getrefcount(a))
    # print(sys.getrefcount(b))
    showMenmSize('创建列表对象a b 之后')
    # del a
    # del b
func()
gc.collect() #手动释放
showMenmSize('完成之后的')

# 查看对象引用情况
'''a= []
print(sys.getrefcount(a)) # 2
b = a
print(sys.getrefcount(a)) #3
c = b
d=c
print(sys.getrefcount(a)) #5'''
