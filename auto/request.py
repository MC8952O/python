'''
requests
1 常见发送请求方法
    1.1 requests.get(url, params = None, **kwargs)
    1.2 post(url, data = None, json = None, **kwargs)
        1.2.1 data与json的区别 除body传参使用json之外，其他的表单传参格式全部为data 文件使用files
    1.3 put(url, data = None, **kwargs)
    1.4 delete(url, **kwargs)
    #上述方法底层都是调用1.5 的requset方法
    1.5 requests.request(method, url,  **kwargs) 可以替代上述方法
    上述1.5方法实际调用session.request(method, url, **kwargs),这个方法可以自动关联有cookie关联的接口
    1.6 requests.session() 获取会话对象 与session.request()相似 ，但是他不能自动关联有cookie关联的皆苦
2 接受响应
    2.1 res.text() 返回文本信息
    2.2 res.json() 返回json格式
    2.3 res.content() 返回字节内容
    2.4 res.status() 返回状态码
    2.5 res.reason() 返回状态信息
    2.6 res.cookie() 返回cookie
    2.7 res.encoding() 返回编码格式
    2.8 res.headers() 返回响应头
    2.9 res.request() 返回请求数据
3接口自动化实践：正则或者json path应用
    3.1 接口自动化实现接口关联的三种方式以及提取变量的两种方式：
        3.1.1 通过类变量(全局变量)保存中间变量实现接口关联
        3.1.2 通过单独文件保存中间变量实现接口关联
        3.1.3 极限封装成和工具一样只需要通过表达式就可以实现关联
        3.1.4 正则表达式提取变量 文本格式
            re.search() 提取一个值 通过下标取值
            re.findall() 提取匹配的所有的值 通过下标取值
        3.1.5 jsonpath提取器提取变量 json格式
'''
import requests
import jsonpath
import re
class TestApi:
    '''开发者门户测试'''
    #初始化对象
    sess = requests.session()
    token = ''
    csrf_token = ''
    def get_token(self):
        '''获取token'''
        url = 'https://apim-qa.gaiaworkforce.com/api/v1/oauth'
        data = {
            'grant_type': 'client_credentials',
            'corp_id': 'mia',
            'client_secret': 'cfdf7bb00f214542ae99d166a0e814f1'
            }
        res = TestApi.sess.request(method='post',url= url, data = data)
        #res = RequestUtil().all_send_request(method = 'post', url= url, data = data)
        result = res.json()
        print(result)
        #json提取token
        value = jsonpath.jsonpath(result, '$.data')
        TestApi.token = 'Bearer ' + value[0]
    def heathcheck_api(self):
    #     '''健康检查接口'''
        url = 'https://openapi-qa.gaiaworkforce.com/demo-y/api/v1/healthcheck'
        headers = {
            'Authorization':TestApi.token,
            'X-Forwarded-For':'111.121.111.23'
            }
        res = TestApi.sess.request(method = 'get', url = url, headers = headers)
    #     res = requests.get(url, headers= hearders)
        print(res.json())
    def search_employee_level(self):
        '''查询职等'''
        url = 'https://openapi-qa.gaiaworkforce.com/hrcc/api/v1/job-position/job-levels'
        headers = {
            'tenant': 'test',
            'trace-id': 'd1af28c6-8681-4f51-aafb-102238a1530a',
            'Authorization': TestApi.token
        }
        json = {
            "valid": True,
            "culture": "ZH-CN",
            "simpleValues": [
                {}
            ],
            "category": "simpleValues",
            "jobLevelCodes": [
                {}
            ]
        }
        #res = requests.post(url, headers=hearders, json=json)
        res = TestApi.sess.request(method='post', url = url,headers=headers, json=json)
        print(res.json())
    def test_start(self):
        '''访问首页'''
        url = 'http://47.107.116.139/phpwind/'
        res = TestApi.sess.request(method='get',url = url)
        print(res.text)
        TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"',res.text).group()
    def login(self):
        '''登录'''
        url = 'http://47.107.116.139/phpwind/index.php'
        datas = {
            'm':'u',
            'c':'login',
            'a':'dorum',
            'username':'baili',
            'password':'bai123',
            'baseurl':'',
            'csrf_token':TestApi.csrf_token,
            'back_url':'http://47.107.116.139/phpwind/',
            'invite':''
        }
        headers = {
            'Accept':'application/json, text/javascript, /; q=0.01',
            'X-Requested-Wtih':'XMLHttpRequest'
        }
        # = requests.post(url, data = datas, headers=headers)
        res = TestApi.sess.request(method='post',url = url, data=datas, headers=headers)
        print(res.json())
if __name__ =='__main__':
    TestApi().get_token()
    TestApi().heathcheck_api()
    TestApi().search_employee_level()
    TestApi().test_start()
    TestApi().login()


