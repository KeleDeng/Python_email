
#!/usr/bin/python
#coding:utf-8  

""" 
@author: DengKele
@contact: 891786333@qq.com 
@software: PyCharm 
@file: test_login.py 
@time: 2018/9/12 21:56 
"""  
import unittest
from module import function,myunit
from page_object.LoginPage import *
from time import sleep

class LoginTest(myunit.StartEnd):

    def test_login1_normal(self):
        '''正常输入用户名和密码'''
        print("test_login1_normal is start run...")
        po=LoginPage(self.driver)
        po.Login_action('51zxw',123456)
        sleep(2)

        self.assertEqual(po.type_loginPasshint(),'我的空间')
        function.insert_img(self.driver,"51zxw_login1_normal.png")
        print("test_login1_normal test end!")


    def test_login2_PasswdError(self):
        ''' 用户名正确，密码错误 '''
        print("test_login2_PasswdError is start run...")
        po = LoginPage(self.driver)
        po.Login_action('51zxw', 123422)
        sleep(2)

        self.assertEqual(po.type_loginFailhint(),'')
        function.insert_img(self.driver,"51zxw_login2_fail.png")
        print("test_login2_PasswdError is test end!")


    def test_login3_empty(self):
        '''用户名和密码为空'''
        print("test_login3_empty is start run...")
        po = LoginPage(self.driver)
        po.Login_action('', '')
        sleep(2)

        self.assertEqual(po.type_loginFailhint(),'')
        function.insert_img(self.driver,"51zxw_login3_fail.png")
        print("test_login3_empty is test end!")

if __name__ == '__main__':
    unittest.main()