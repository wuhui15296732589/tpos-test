from common import common_public
import  requests,json


from common.Log import MyLog
log = MyLog.get_log()
logging = log.logger




def code(self,type,mobile):
    '''
    ע���ȡ��֤��
    :return:

    '''

    url= common_public.URL() +'api_002'
    data1 = {"HEAD":common_public.App_head(),
            "BODY":{"type":type,"mobile":mobile}}
    logging.info('�����ַ��'+url+','+'���������'+data1)
    data = json.dumps(data1)
    respons = requests.post(url = url , data = data)
    result = respons.json()
    return result





# def register(self,):
#     '''
#     �ֻ���ע���̻�
#     :return:
#     '''
#     logging.info('---------------------start:�ֻ���ע���̻�-------------------------')
#     url = common_public.URL() + 'api_001'
#     data1 = {"HEAD":common_public.App_head(),
#              "BODY":{"code":"6666","password":"123456","mobile":self.mobile,
#                      "firPassword":"123456","type":"1","accountType":"1"}}
#     logging.info('�����ַ��'+url)
#     logging.info('���������'+data1)
#     data = json.dumps(data1)
#     respons = requests.post(url= url,data = data)
#     result = respons.json()
#     assert result['HEAD']['MSG'] =='�����ɹ�'
#     logging.info('-----------------end:�ֻ���ע��ɹ�----------------------------------')
