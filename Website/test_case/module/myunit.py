#!/usr/bin/python  
#coding:utf-8  

""" 
@author: DengKele
@contact: 891786333@qq.com 
@software: PyCharm 
@file: myunit.py 
@time: 2018/9/12 20:23 
"""  
from driver import *
import unittest

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()