import unittest
import logging

from api.login_api import LoginApi
from utils import assert_common,read_login_data
from parameterized import parameterized


class TestIHRMLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    def setUp(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def tearDown(self) -> None:
        pass
    @parameterized.expand(read_login_data())

    def test01_login(self,mobile,password,http_code,success,code,message):
        #调用封装的登录接口
        response = self.login_api.login(mobile,password)
        #接收返回的json数据
        jsonData = response.json()
        #调试输出登录接口返回的数据，日志输出只能用作为{}占位符
        logging.info("接口返回的数据为：{}".format(jsonData))
        #断言
        assert_common(self,response,http_code,success,code,message)








