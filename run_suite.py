import unittest

from script.login import TestLogin
from script.test_emp import TestIHRMEmp
from script.test_login import TestIHRMLogin
from tools.HTMLTestRunner import HTMLTestRunner
from script.test_emp import TestIHRMEmp
import app
import time
#1.初始化测试套件
suite = unittest.TestSuite()

#2.将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmp))
# suite.addTest(unittest.makeSuite(TestIHRMLogin))
# 3.使用HTMLTestRunner执行测试套件，生成测试报告
#report_path = app.BASE_DIR +"/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
report_path = app.BASE_DIR +"/report/ihrm.html"

with open(report_path,mode='wb') as f:
    #初始化HestRunner
   runner = HTMLTestRunner(f,verbosity=1,title="IHRM人力资源接口测试",description="v1.0.0")

    #使用Runner运行测试套件
   runner.run(suite)
