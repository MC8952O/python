import requests
class RequestUtil:
    '''发送请求包'''
    #定义发送请求的变量
    sess = requests.session()
    def all_send_request(self, **kwargs):
        '''发送请求'''
        res = RequestUtil.sess.request(**kwargs)
        return res
