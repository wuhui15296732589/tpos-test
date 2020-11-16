#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/10/27


import unittest
import os
import time
from common import HTMLTestRunner
from result import resule_path as result
from testCase import result_path as test
testdir = test.result_path()
resultPath = result.result_path()


def allClass():
    suite = unittest.TestLoader().discover(
        start_dir=testdir,
        pattern='test_*.py',
        top_level_dir=None
        )                                           #批量获取测试模块
    return suite


def getNowTime():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))


def run():
    fileName = os.path.join(resultPath,getNowTime() +'result.html')


    fp = open(fileName,'wb')


    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='接口自动化测试详情'
    )


    runner.run(allClass())
    fp.close()


if __name__ == '__main__':
    run()

