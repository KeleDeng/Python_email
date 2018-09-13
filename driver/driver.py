#!/usr/bin/python  
#coding:utf-8  

""" 
@author: DengKele
@contact: 891786333@qq.com 
@software: PyCharm 
@file: driver.py 
@time: 2018/9/12 20:14 
"""
from selenium import webdriver


def browser():
    driver=webdriver.Firefox()
    # driver=webdriver.PhantomJS()
    # driver=webdriver.Chrome()
    # driver=webdriver.Ie()

    # driver.get("http://www.baidu.com")

    return driver
if __name__ == '__main__':
    browser()