#!/usr/bin/python  
#coding:utf-8  

""" 
@author: DengKele
@contact: 891786333@qq.com 
@software: PyCharm 
@file: function.py 
@time: 2018/9/12 20:32 
"""  
from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

'''截图'''
def insert_img(driver,filename):
    # 获取当前目录路径
    func_path=os.path.dirname(__file__)
    # print(func_path)

    # 获取上一级目录路径
    base_dir=os.path.dirname(func_path)
    # print(base_dir)

    # 将路径转化为字符串
    base_dir=str(base_dir)

    # 对路径的字符串进行替换
    base_dir=base_dir.replace('\\','/')

    # print(base_dir)
    base=base_dir.split('/Website')[0]
    # print(base)

    # 指定截图存放路径
    filepath=base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)

# 邮件发送报告
def send_email(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    user = 'bluesky.0903@163.com'
    password = "KELE622ok"

    sender = "bluesky.0903@163.com"
    receive = "891786333@qq.com"

    subject = "selenuim报告发送"
    # content = '<html><h1 style="color:red">我要自学，自学成才！</h1></html>'


    # 构建发送与接收信息
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receive

    # SSL协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("Start send email...")

    smtp.sendmail(sender, receive, msg.as_string())

    smtp.quit()
    print("Send End！")


# 查找最新报告方法
def latest_report(report_dir):
    # 报告存放位置
    report_dir = './Test_Report'

    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    lists = os.listdir(report_dir)

    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print(lists)
    print("latest report is :" + lists[-1])

    # 输出最新报告的路径
    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

if __name__ == '__main__':

    driver=webdriver.Firefox()
    driver.get("http://www.sogou.com")
    insert_img(driver,'sougou.png')
    driver.quit()