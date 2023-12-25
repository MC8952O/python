'''
接口自动化测试引入pytest用例管理框架
1 用例管理框架的分类
    1.1 python pytest unittest
    1.2 java testng junit
2 作用：
    2.1 找到用例
        1 模块名以test_或者_test开头
        2 类名必须以Test开头,并且不能init方法
        3 用例方法必须以test开头
    2.2 执行用例
    2.3 判断结果
    2.4 生成报告
3 安装插件：pip install -r 插件文件路径
    3.1 pytest本身
    3.2 pytest-html 简单的html报告
    3.3 pytest-xdist 多线程执行
    3.4 pytest-ordering 控制用例执行顺序
    3.5 pytest-rerunfailures 失败用例重跑
    3.5 pytest-base-url 设置基础路径
    3.6 allure-pytest 生成allure报告
4 运行测试用例的三种方式
    4.1 命令行
        -v 输出更详细的信息
        -s 输出调试信息
    4.2 主函数
        import pytest
        if __name__ =='__main__':
        pytest.main()
    4.3 结合pytest.ini全局配置文件执行
        根目录下新增 pytest.ini 文件 
5 pytest的前后置、固件、夹具
    5.1 每个用例之前和之后
        def setup(self):
            print('用例之前')
        def teardown(self):
            print('用例之后')
    5.2 类之前 类之后
        def setup(self):
            print('类之前')
        def teardown(self):
            print('类之后')
6 使用fixtrue 固件结合 contest.py文件实现前后置

        
'''