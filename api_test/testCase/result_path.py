#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by HuiWu
# @Time : 2020/11/10 23:00

import os
#获取当前目录
def result_path():
    resuilt_path = os.path.split(os.path.realpath(__file__))[0]
    return resuilt_path