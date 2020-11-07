#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/10/27
from common import Common
import  requests,json,os
import logging
import logging.config


CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
session = requests.Session()
class Customer_register():
    def __init__(self,mobile):
        self.mobile = mobile

    def code(self):
        '''
        注册获取验证码
        :return:
        '''
        logging.info('---------------start------------:开始获取验证码------------------------')
        url= Common.URL() +'api_002'
        data1 = {"HEAD":Common.App_head(),
                "BODY":{"type":"1","mobile":self.mobile}}
        logging.info('请求地址：'+url+','+'请求参数：'+data1)
        data = json.dumps(data1)
        respons = requests.post(url = url , data = data)
        assert respons.status_code == 200
        logging.info('---------------------end------------验证码获取成功---------------------')



    def register(self):
        '''
        手机号注册商户
        :return:
        '''
        logging.info('---------------------start:手机号注册商户-------------------------')
        url = Common.URL() + 'api_001'
        data1 = {"HEAD":Common.App_head(),
                 "BODY":{"code":"6666","password":"123456","mobile":self.mobile,
                         "firPassword":"123456","type":"1","accountType":"1"}}
        logging.info('请求地址：'+url)
        logging.info('请求参数：'+data1)
        data = json.dumps(data1)
        respons = requests.post(url= url,data = data)
        assert respons.status_code ==200
        logging.info('-----------------end:手机号注册成功----------------------------------')



def login(mobile,password):
    '''
    账号密码登录
    :return:BODY:{"customerInfo":{"customerId":32,"bindState":10,"authState":1,"bankState":1,
    "actnState":1,"examineState":0,"agreementState":1,"signTime":"20201027","policyId":0,
    "mobile":"15600000033","realName":"监督活动","idCard":"142703199110162789","pendIncome":0,
    "depositAmount":null},
    "token":"vqtQipq6K72Hw9NZf6DQor15cjcpQkXcw9Gxw6ZkulNrIRRQiLpTDOb6RZ4WlAR99ZQIFTEC1rGvbAJXmNzwChkm8XGpQPjOXF5zS0ZCpqY=",
    "isVip":false,"isBuyVip":false}}
    '''
    logging.info('----------------start:商户登录------------------------')
    url = Common.URL() + 'api_004'
    data1 = {"HEAD":Common.App_head(),
             "BODY":{"password":password,"accountType":"1","mobile":mobile}}
    logging.info('请求地址：'+url)

    data = json.dumps(data1)
    logging.info('请求参数：' + data)

    respons = session.post(url=url, data= data)
    logging.info('----------------end:返回值------------------------')
    logging.info(respons.text)
    assert respons.status_code == 200
    print(respons.cookies)
    coolies = requests.utils.dict_from_cookiejar(respons.cookies)
    print(coolies)

    result = respons.json()
    logging.info('----------------end:登录成功------------------------')
    return result['BODY']


def ID_upload_positive(customerid):
    '''
    身份证正面上传
    :return:图片地址
    '''
    logging.info('------start:上传身份证正面-----------')

    url = Common.URL()+'api_007'
    dir = os.getcwd()+r'\img\positive.jpg'
    data1 = {"HEAD":Common.App_head(),"BODY":{"id":customerid,"bizType":"idImg","imageType":'1'}}
    data = json.dumps(data1)
    # 上传文件单独构造成以下形式
    # 'img' 上传文件的键名
    # 'demo' 上传到服务器的文件名，可以和上传的文件名不同
    # open('D:/demo.jpg') 打开的文件对象，注意文件路径正确
    # 'image/jpeg' Content-Type类型

    files = {
        'REQ_MESSAGE':(None,data),
        'idPicture':('positive.jpg',open(dir,'rb'),'image/jpg')
    }
    logging.info('url:'+url)
    logging.info('data:'+data)


    respons = requests.post(url = url,files=files)

    logging.info('respons:'+respons.text)
    assert respons.status_code == 200
    result = respons.json()
    logging.info('return:'+result['BODY']['imgPath'])
    logging.info('--------------------end:上传身份证正面----------------')
    return result['BODY']['imgPath']


def ID_upload_back(customer):
    '''
    身份证反面上传
    :return:图片地址
    '''
    logging.info('------start:上传身份证反面-----------')


    url = Common.URL()+'api_007'
    dir = os.getcwd() + r'\img\back.jpg'
    data1 = {"HEAD":Common.App_head(),
             "BODY":{"id":customer,"bizType":"idImg","imageType":2,"accountType":"1"}}

    data = json.dumps(data1)

    files = {
        'REQ_MESSAGE':(None,data),
        'idPicture':('back.jpg',open(dir,'rb'),'image/jpg')
    }
    logging.info('url:' + url)
    logging.info('data:' + data)


    respons = requests.post(url = url, files = files)
    logging.info('respons:' + respons.text)
    assert respons.status_code == 200
    result = respons.json()
    logging.info('return:'+result['BODY']['imgPath'])
    logging.info('--------------------end:上传身份证反面----------------')
    return result['BODY']['imgPath']


def ID_upload_hold(customer):
    '''
    手持身份证照片
    :return:图片地址
    '''
    logging.info('------start:上传手持身份证-----------')


    url = Common.URL() + 'api_007'
    dir = os.getcwd() + r'\img\hold.jpg'
    data1 = {"HEAD": Common.App_head(),
             "BODY": {"id": customer, "bizType": "idImg", "imageType": 3, "accountType": "1"}}

    data = json.dumps(data1)

    files = {
        'REQ_MESSAGE': (None, data),
        'idPicture': ('hold.jpg', open(dir, 'rb'), 'image/jpg')
    }
    logging.info('url:' + url)
    logging.info('data:' + data)

    respons = requests.post(url=url, files=files)
    logging.info('respons:' + respons.text)
    assert respons.status_code == 200
    result = respons.json()
    logging.info('return:' + result['BODY']['imgPath'])
    logging.info('--------------------end:上传手持身份证----------------')
    return result['BODY']['imgPath']

def identity_check(customerid,frontpath,backpath,holdpath,token):
    '''
    身份信息确认（customerid，frontpath，backpath，holdpath）
    :return:请求respons
    '''
    logging.info('------start:身份信息确认-----------')
    head = Common.App_head()
    head['TYPE'] ='2'
    head['ACCOUNT_TYPE'] = '1'
    head['TOKEN'] = token

    url = Common.URL() + 'api_161'
    data1 = {
        'HEAD':head,
        'BODY':{"realName":Common.customer_name(),
                "expiryDateEnd":"20391026",
                "address":"山西省河津市世纪花园1单元101",
                "holdPath": holdpath,
                "frontPath": frontpath,
                "backPath": backpath,
                "idCard":Common.id_card_number(),
                "expiryDateBegin":"20191026",
                "id":customerid}
    }
    data = json.dumps(data1)
    logging.info('url:'+url)
    logging.info("requests:"+data)
    respons = requests.post(url=url,data=data)
    logging.info('result:'+respons.text)
    assert respons.status_code == 200
    logging.info('-----------------end:身份确认完成----------------')
    return data1['BODY']




#上传银行卡正面图片
def bank_card_img(customerid,token):
    '''
    银行卡图片上传
    :param token:
    :param customerid:
    :return: 图片地址
    '''
    logging.info('------------------------start:银行卡图片上传---------------------')
    head = Common.App_head()
    head['TOKEN'] = token
    dir = os.getcwd() + r'\img\bank_img.jpg'
    url = Common.URL() + 'api_007'
    data1 = {
        'HEAD': Common.App_head(),
        'BODY': {"bizType":"stCard","id":customerid}
    }

    data = json.dumps(data1)
    logging.info('data:'+data)
    files = {
        "REQ_MESSAGE":(None,data),
        'idPicture': ('bank_img.jpg', open(dir, 'rb'), 'image/jpg')
    }
    respons = requests.post(url=url,files = files)
    logging.info('respons:'+respons.text)
    logging.info('---------------------end:银行卡图片上传---------------------')
    result = respons.json()
    return result['BODY']['imgPath']




def add_bank_information(token,id,realname,idcard,bankmobile,img):
    '''
    添加结算卡
    :param token:token
    :param id:商户id
    :param realname:商户实名名称
    :param idcard:商户身份证号
    :param bankmobile:商户银行卡预留手机号
    :param img:银行卡图片地址
    :return:
    '''
    logging.info('----------------------start：添加银行卡确认-------------------')
    URL = Common.URL()+'api_016'
    head = Common.App_head()
    head['TOKEN'] = token
    head['TYPE'] = '2'
    data = {
        'HEAD':head,
        'BODY':{"code":"6666",
                "codeType":3,
                "accountName":realname,
                "idCard":idcard,
                "accountType":1,
                "bankMobile":bankmobile,
                "type":"1",
                "realName":realname,
                "isPublicAcc":"0",
                "bankbranchName":"中国建设银行股份有限公司北京平谷新开街支行",
                "tposBankFrontPath":img,
                "id":id,
                "account":Common.bank_number(),
                "paybankNo":"105100031442"}
    }


    data1 = json.dumps(data)
    logging.info('data:'+data1)
    respons = requests.post(url=URL,data=data1)
    logging.info('respons:' + respons.text)
    logging.info('----------------end:添加银行卡确认-----------------------')


def electronic_signature(token,customerid):
    '''
    确认函图片上场
    :param token:token
    :param customerid:商户id
    :return: 返回地址
    '''
    url = Common.URL()+'api_007'
    head = Common.App_head()
    head['TOKEN'] = token
    head['TYPE'] = '2'
    logging.info('----------------start：确认函图片上传')
    dir = os.getcwd() + r'\img\signature.jpg'
    data1 = {
        'HEAD': head,
        'BODY': {'bizType':"csAuth","accountType":"1","id":customerid,"imageType":"7"}
    }

    data = json.dumps(data1)
    logging.info('respons:' + data)
    files = {
        "REQ_MESSAGE":(None,data),
        'idPicture': ('signature.jpg', open(dir, 'rb'), 'image/jpg')
    }

    respons = requests.post(url=url, files=files)
    logging.info('respons:' + respons.text)
    result = respons.json()

    logging.info('---------------------end:确认函图片上传---------------------')
    logging.info('return:'+result['BODY']['imgPath'])

    return result['BODY']['imgPath']

def customer_information(token,customerid,electronic_signature_img,):
    url = Common.URL()+'api_418'
    logging.info('----------------start:完善商户信息-------------------')
    head = Common.App_head()
    head['TOKEN'] = token
    head['TYPE'] = '2'
    data = {
        'HEAD':head,
        'BODY':{"mercAreaId":"5211",
            "accountType":"1",
            "mercCityId":"5210",
            "manageInfoPath":electronic_signature_img,
            "type":"1",
            "merShortName":Common.customer_name_company(),
            "mccCode":"5462",
            "mercFullName":Common.customer_name_company(),
            "whetherBusiness":"2",
            "id":customerid,
            "mercAddress":"陕西省西安市应人石村",
            "mercProvId":"5200",
            "manageInfoState":"10"}}
    data1 = json.dumps(data)
    logging.info('data:'+data1)
    respons = requests.post(url,data=data1)
    logging.info('respons:' + respons.text)
    logging.info('---------------------end:完善商户信息---------------------')



if __name__ == '__main__':
    #商户注册
    # resgiter = Customer_register('15600000033')
    # sss = resgiter.code()
    # ddd = resgiter.register()



    #商户登录
    mobile = '15600000033'
    password = '123456'
    s = login(mobile,password)
    #获取登录token跟商户id

    customer = s['customerInfo']['customerId']
    token = s['token']
    #身份证图片正面上传

    img1 = ID_upload_positive(customer)
    #身份证图片反面上传

    img2 = ID_upload_back(customer)
    #手持身份证照片上传

    img3 = ID_upload_hold(customer)

    #身份信息确认
    enter = identity_check(customer,img1,img2,img3,token)
    name = enter['realName']
    card = enter['idCard']
    #银行卡图片上传
    bank_img = bank_card_img(token,customer)

    #添加银行卡确认
    add_bank_information(token,customer,name,card,mobile,bank_img)

    #确认函
    s = electronic_signature(token,customer)

    #完善商户信息
    customer_information(token,customer,s)











