from testCase.myunit import StartEnd
from common import common_public


s = common_public.get_xls('testCase.xls','register')

class test_customer_code(StartEnd):
     def test_mobile_less_11(self):

         pass

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
    s = common_public.get_xls('testCase.xls','register')
    print(s)
    print(s[0][2])