#!/usr/bin/python  
#coding:utf-8  

""" 
@author: DengKele
@contact: 891786333@qq.com 
@software: PyCharm 
@file: LoginPage.py 
@time: 2018/9/12 18:48 
"""  
from BasePage import *
from  selenium.webdriver.common.by import By

class LoginPage(Page):
    url='/news/'

    username_loc=(By.NAME,'username')
    password_loc=(By.NAME,'password')
    submit_loc=(By.NAME,'Submit')

    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()


    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    loginPass_loc=(By.LINK_TEXT,'我的空间')
    loginFail_loc=(By.NAME,'username')


    def type_loginPasshint(self):
        return self.find_element(*self.loginPass_loc).text

    def type_loginFailhint(self):
        return self.find_element(*self.loginFail_loc).text