#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by HuiWu
# @Time : 2020/11/10 23:00

from testCase.myunit import StartEnd
from common import common_public
from common.customer import customer_api
from common.Log import MyLog
import unittest
log = MyLog.get_log()
logging = log.logger

s = common_public.get_xls('testCase.xls','register')

class test_customer_code(StartEnd):
     def test_mobile_less_11(self):
        u"""手机号不足11位"""

        data = s[0][2]
        result = customer_api.code(data)
        assert result['HEAD']['MSG'] == '操作shibai'






     def test_mobile_greater_11(self):
         pass

     def test_mobile_start_11(self):
         pass
     def test_mobile_start_12(self):
         pass
     def test_mobile_none(self):
         pass
     def test_type_none(self):
         pass
     def test_type_not_1(self):
         pass
     def test_parameter_correct(self):
         pass






if __name__ == '__main__':
    unittest.main()