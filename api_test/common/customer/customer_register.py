from common import common_public
import  requests,json


from common.Log import MyLog
log = MyLog.get_log()
logging = log.logger




def code(self,type,mobile):
    '''
    注册获取验证码
    :return:

    '''

    url= common_public.URL() +'api_002'
    data1 = {"HEAD":common_public.App_head(),
            "BODY":{"type":type,"mobile":mobile}}
    logging.info('请求地址：'+url+','+'请求参数：'+data1)
    data = json.dumps(data1)
    respons = requests.post(url = url , data = data)
    result = respons.json()
    return result





# def register(self,):
#     '''
#     手机号注册商户
#     :return:
#     '''
#     logging.info('---------------------start:手机号注册商户-------------------------')
#     url = common_public.URL() + 'api_001'
#     data1 = {"HEAD":common_public.App_head(),
#              "BODY":{"code":"6666","password":"123456","mobile":self.mobile,
#                      "firPassword":"123456","type":"1","accountType":"1"}}
#     logging.info('请求地址：'+url)
#     logging.info('请求参数：'+data1)
#     data = json.dumps(data1)
#     respons = requests.post(url= url,data = data)
#     result = respons.json()
#     assert result['HEAD']['MSG'] =='操作成功'
#     logging.info('-----------------end:手机号注册成功----------------------------------')
