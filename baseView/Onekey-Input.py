#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/12/7
from baseView import customer_register

def Onekey(mobile,password):
    #商户注册
    resgiter = customer_register.Customer_register(mobile)
    sss = resgiter.code()
    ddd = resgiter.register()
    #商户登录

    s = customer_register.login(mobile,password)
    #获取登录token跟商户id

    customer = s['customerInfo']['customerId']
    token = s['token']
    # #身份证图片正面上传
    #
    img1 = customer_register.ID_upload_positive(customer)
    # #身份证图片反面上传

    img2 = customer_register.ID_upload_back(customer)
    # #手持身份证照片上传

    img3 = customer_register.ID_upload_hold(customer)

    # #身份信息确认
    enter = customer_register.identity_check(customer,img1,img2,img3,token)
    name = enter['realName']
    card = enter['idCard']
    # #银行卡图片上传
    bank_img = customer_register.bank_card_img(token,customer)

    # #添加银行卡确认
    customer_register.add_bank_information(token,customer,name,card,mobile,bank_img)

    # #确认函
    s = customer_register.electronic_signature(token,customer)

    # #完善商户信息
    customer_register.customer_information(token,customer,s)
    #修改商户审核状态
    customer_register.set_customer_examine(mobile)




if __name__ == '__main__':
    for s in range(53,60):
        mobile = '156000000'+str(s)
        Onekey(mobile,'123456')

