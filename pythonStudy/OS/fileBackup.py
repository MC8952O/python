def copyBigFile():
    old_file = input('请输入现需要备份的文件名称：')
    file_list = old_file.split('.')
    #构造新的文件名.备份后缀
    new_file = file_list[0]+'_备份.'+file_list[1]
    try:
        # 监视需要处理的逻辑
        with open(old_file, 'r') as old_f , open(new_file, 'w') as new_f:
            while True:
                content = old_f.read(1024) # 一次性读取1024个字符
                new_f.write(content)
                if len(content) > 1024:
                    break
    except Exception as msg:
        print(msg)
    '''#打开需要备份的文件
    old_f = open(old_file, 'r')
    #以写的模式打开新文件
    new_f = open(new_file, 'w')
    content = old_f.read()
    new_f.write(content)
    # 关闭文件
    old_f.close()
    new_f.close()'''
copyBigFile()





