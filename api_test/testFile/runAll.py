#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/10/27


import unittest
import os
import time
from testFile.readConfig import ReadConfig
from common import HTMLTestRunner
from result import resule_path as result
from testCase import result_path as test
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


testdir = test.result_path()
resultPath = result.result_path()
readconfig = ReadConfig()


def allClass():
    suite = unittest.TestLoader().discover(
        start_dir=testdir,
        pattern='test_*.py',
        top_level_dir=None
        )                                           #批量获取测试模块
    return suite


def getNowTime():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))


fileName = os.path.join(resultPath,getNowTime() +'result.html')

def run():

    fp = open(fileName,'wb')


    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='接口自动化测试详情'
    )


    runner.run(allClass())
    fp.close()


def send_mail(file_name):
    #读取文件
    f = open(file_name,'rb')
    mail_body = f.read()
    f.close()


    #邮件对象
    body = MIMEText(mail_body, 'html', 'utf-8')
    # msg['Subject'] = Header("自动化报告", 'utf-8')
    # smtp = smtplib.SMTP_SSL(readconfig.get_email('mail_host'),readconfig.get_email('mail_port'))
    #
    # smtp.login(readconfig.get_email('mail_user'),readconfig.get_email('mail_pass'))
    # smtp.sendmail(readconfig.get_email('sender'),readconfig.get_email('receiver'),msg.as_string())
    # smtp.quit()
    msg = MIMEMultipart()
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = Header(readconfig.get_email('sender'))
    msg['To'] = Header(readconfig.get_email('receiver'))
    #msg['To'] = ';'.join(readconfig.get_email('receiver'))
    msg['date'] = getNowTime()
    msg.attach(body)

    #附件
    att = MIMEText(mail_body,'base64','utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    #发送邮件（接收人可以设置多个收件人， 用列表形式添加[]）
    try:
        smtp = smtplib.SMTP
        smtp.connect(readconfig.get_email('mail_host'))
        smtp.login(readconfig.get_email('mail_user'),
                   readconfig.get_email('mail_pass'))
    except:
        smtp = smtplib.SMTP_SSL(readconfig.get_email('mail_host'),
                                readconfig.get_email('mail_port'))
        smtp.login(readconfig.get_email('mail_user'),
                   readconfig.get_email('mail_pass'))

    smtp.sendmail(readconfig.get_email('sender'),
                  readconfig.get_email('receiver'),
                  msg.as_string())
    smtp.quit()




def new_report():
    lists=os.listdir(resultPath)
    lists.sort(key=lambda fn: os.path.getmtime(resultPath+"\\"+fn))
    file_new=os.path.join(resultPath,lists[-1])
    return file_new




if __name__ == '__main__':
    run()
    file = new_report()
    send_mail(file)



