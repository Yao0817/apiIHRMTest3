"""执行添加员工信息的测试用例"""
import logging
import unittest

import pymysql

import app
from api.emp_api import EmpApi
from utils import assert_common, read_add_emp_data, read_query_emp_data, read_modify_emp_data, read_delete_emp_data, \
    DBUtils
from parameterized import parameterized

class TestIHRMEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 创建一个员工信息的实例化对象
        cls.emp_api = EmpApi()

    def setUp(self) -> None:
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def tearDown(self) -> None:
        ...
    @parameterized.expand(read_add_emp_data())
    def test01_add_emp(self,username,mobile,success,code,message,http_code):
        response = self.emp_api.add_emp(username,mobile)
        jsonData = response.json()
        logging.info("添加员工接口数据为:{}".format(jsonData))
        assert_common(self, response,http_code,success, code, message)
        #获取员工ID保存在全局变量
        app.EMP_ID = jsonData.get("data").get("id")
        logging.info("员工ID：{}".format(app.EMP_ID))
    @parameterized.expand(read_query_emp_data())
    def test02_query_emp(self, success, code, message, http_code):
        response = self.emp_api.query_emp()
        jsonData = response.json()
        logging.info("查询员工接口的返回数据为：{}".format(jsonData))
        assert_common(self, response, http_code,success, code, message)

    @parameterized.expand(read_modify_emp_data)
    def test03_modify_emp(self, username, success, code, message, http_code):
        # 调用修改员工接口
        response = self.emp_api.modify_emp(username)
        # 获取修改员工接口的返回json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("修改员工接口的返回数据为:{}".format(jsonData))
        # #建立连接
        # conn = pymysql.connect("182.92.81.159",'readuser','iHRM_user_2019','ihrm')
        # #获取游标
        # cursor = conn.cursor()
        # #执行查询语句，查询出添加的员工的username 是不是修改的username
        # sql ="select username from bs_user where id={}".format(app.EMP_ID)
        # cursor.execute(sql)
        # #获取执行结果
        # result =cursor.fetchone()[0]
        # logging.info("数据库中查询出的员工的用户名是：{}".format(result))
        # self.assertEqual(username,result)
        # cursor.close()
        # conn.close()
        with DBUtils() as db_utils:
            sql = "select username from bs_user where id={}".format(app.EMP_ID)
            db_utils.execute(sql)
            #获取执行结果
            result = db_utils.fetchone()[0]
            logging.info("数据库中查询出的员工的用户名是：{}".format(result))

        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_delete_emp_data)
    def test04_delete_emp(self, success, code, message, http_code):
        # 调用删除员工接口
        response = self.emp_api.delete_emp()
        # 获取修改员工接口的返回json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("删除员工接口的返回数据为:{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)
