#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/10/27




# import unittest,os
# from common import HTMLTestRunner
# from testFile import readConfig
# from common import common
# from result import resule_path
#
# path = resule_path
#
#
# resluthtml = r'\result.html'
# resultPath = path +resluthtml
#
#
# logger = common.logger
# def set_case_list(self):
#     fb = open(self.caseListFile)
#     for value in fb.readlines():
#         data = str(value)
#         if data != '' and not data.startswith("#"):
#             self.caseList.append(data.replace("\n", ""))
#     fb.close()
#
# def set_case_suite(self):
#     self.set_case_list()
#     test_suite = unittest.TestSuite()
#     suite_model = []
#
#     for case in self.caseList:
#         case_file = os.path.join(readConfig.proDir, "testCase")
#         print(case_file)
#         case_name = case.split("/")[-1]
#         print(case_name+".py")
#         discover = unittest.defaultTestLoader.discover(case_file, pattern=case_name + '.py', top_level_dir=None)
#         suite_model.append(discover)
#
#     if len(suite_model) > 0:
#         for suite in suite_model:
#             for test_name in suite:
#                 test_suite.addTest(test_name)
#     else:
#         return None
#     return test_suite
#
# def run(self):
#     try:
#         suit = self.set_case_suite()
#         if suit is not None:
#             logger.info("********TEST START********")
#             fp = open(resultPath, 'wb')
#             runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
#             runner.run(suit)
#         else:
#             logger.info("Have no case to test.")
#     except Exception as ex:
#         logger.error(str(ex))
#     finally:
#         logger.info("*********TEST END*********")
#         # send test report by email
#         # if int(on_off) == 0:
#         #     self.email.send_email()
#         # elif int(on_off) == 1:
#         #     logger.info("Doesn't send report email to developer.")
#         # else:
#         #     logger.info("Unknow state.")


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
        start_dir=test,
        pattern='test_*.py',
        top_level_dir=None
        )                                           #批量获取测试模块
    return suite


def getNowTime():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))


def run():

    fileName = resultPath+ getNowTime() +'result.html'
    fp = open(fileName,'wb')


    runner = HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='接口自动化测试详情：'
    )


    runner.run(allClass())
    fp.close()


if __name__ == '__main__':
    run()

