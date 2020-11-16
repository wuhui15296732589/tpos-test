#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/9/28


from common import common_public
import json
from common import configHttp
from common.Log import MyLog

log = MyLog.get_log()
logging = log.logger




def code(data):
    '''
    注册获取验证码
    :return:

    '''

    try:
        confighttp = configHttp.ConfigHttp()
        confighttp.set_url('api_002')
        data1 = {'HEAD': common_public.App_head(),
                 "BODY":data}
        confighttp.set_data(data1)
        confighttp.post()
        return confighttp.post()
    except BaseException as ex:
        logging.error(ex)



if __name__ == '__main__':
    s = code({'type':'1','mobile':'1340000003'})
    print(s)