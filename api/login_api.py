import requests
import app

class LoginApi():
    def __init__(self):
        self.login_url = app.HOST +"/api/sys/login"
        self.headers = app.HEADERS
        #从外部接收mobile 和password
        #为什么这么写呢？ 这是因为，如果写成一个参数data 来接收字典数据
        #那么后续进行参数化的时候，会很不方便，所以改成接收两个变量
    def login(self,mobile,password):
        #使用data来接收外部传入的mobile和password，拼接成要发送的数据
        data ={"mobile":mobile,
               "password":password
               }
        #发送登录请求
        response = requests.post(self.login_url,
                                 json=data,
                                 headers =self.headers)
        #返回响应数据
        return response
