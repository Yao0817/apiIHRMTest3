"""员工管理Api"""
import app
import requests


class EmpApi:
    """员工管理类"""

    def __init__(self):
        self.emp_url = app.HOST+'/api/sys/user'
        #注意：如果我们调用员工管理模块的相关接口时，先调用login_py接口
        #那么获取到的app.HEADERS是{“Content-Type":"application","Authorization":"Bearer xxx-xxx-xxxxxx"}
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        """添加员工信息"""
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-01-04",
            "formOfEmployment": 1,
            "workNumber": "12345678958",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2020-01-08T16:00:00.000Z"
        }
        return requests.post(self.emp_url, json=data, headers=self.headers)

        # 封装查询员工接口

    def query_emp(self):
        # 查询员工接口的URL结构是http://182.92.81.159/api/sys/user/12344343221
        # 所以拼接URL时需要加上“/”
        url = self.emp_url + "/" + app.EMP_ID
        # 返回查询的结果，headers是{"Content-Type":"application/json", "Authorization":"Bearer xxxx"}
        return requests.get(url, headers=self.headers)

    #封装修改员工接口
    def modify_emp(self,username):
        #修改员工的Url 应该和查询员工一样的，所以拼接的时候也需要加“/”
        url = self.emp_url +"/" + app.EMP_ID
        data = {"username":username}
        return requests.put(url,
                            json=data,
                            headers =self.headers)
    #封装删除员工接口
    def delete_emp(self):
        url = self.emp_url +"/" + app.EMP_ID

        return requests.delete(url,headers =self.headers)