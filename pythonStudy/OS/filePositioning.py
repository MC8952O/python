'''tell()--获取光变所在位置'''
# with open('D:\OS\Test\FilePositioning.txt', 'r', encoding= 'utf-8') as file_test:
#     print(file_test.read(3))
#     print(file_test.tell())
'''  truncate()----对源文件进行截取操作'''
# with open('D:\OS\Test\Truncate_file.txt', 'r') as file_truncate:
#     print(file_truncate.read())
#     print('截取之后：-------------')
# with open('D:\OS\Test\Truncate_file.txt', 'r+') as after_file:
#     after_file.truncate(100)
#     print(after_file.read())
'''seek(offset, form)  offset:偏移量单位字节，负数往左便宜，正数往右便宜 from：0 文件开头；1 当前位置偏移；2 末尾偏移 ---在文件操作过程中，需要定位到其它位置进行操作既：随意更改指针位置'''
with open('D:\OS\Test\SeekFile.txt', 'rb') as after_file:
    content = after_file.read(2)
    print(content.decode('gbk'))
    after_file.seek(-2,1)
    print(after_file.read(4).decode('gbk'))