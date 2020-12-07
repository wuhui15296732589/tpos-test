#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/11/20

from locust import TaskSet,task,HttpUser
from performance import Common
from common import Log
import json
import random

# log = Log.get_log()
# logging = log.logger


class UserBehavior(TaskSet):
    @task(1)
    def test_trans(self):
        url = 'http://47.112.191.144:8180/tpos-api-web-srv/api_075'
        amount1 = Common.amount()  # 交易金额（分）
        rate1 = Common.fee()  # 交易费率（%）
        defee = 300  # 单笔手续费（分）
        merchantCode = Common.merchantCode_terminalSn()[0]  # 商户号
        terminalSn = Common.merchantCode_terminalSn()[1]  # sn号
        activityId = 'H0441'  # 押金类型（H0421 = 39     H0441 = 69      H0422 = 99      H0423 = 139）(押金类型对应交易金额则为押金支付交易)
        voucherId = ''  # sim扣费（MKA_0024），不填为不扣费
        voucherFee = ''  # sim扣费金额：3600，不填为不扣费
        payCardAttr = random.randint(0,3)  # 交易卡类型（1:借记卡 2:贷记卡 3：无卡）
        quickPassPay = random.randint(0,2)  # 交易类型0:普通交易 1：云闪付优惠 2：小额双免优惠
        serverCode = Common.serverCode()  # 交易编码交易编码10001：刷卡 10002：微信10003:NFC 10004：支付宝 10005：银联二维码

        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.26.3',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        data = {
            "bizType": "P01",
            "body": {
                "addFee": "0",
                "amount": amount1 - int(amount1 * rate1 * 0.01) - defee,
                "cardNo": "625809******6046",
                "d0Rate": str(rate1) + "|0|0|2000|0|0|00",
                "dfFee": defee,
                "fee": int(amount1 * rate1 * 0.01),
                "merchantCode": str(merchantCode),
                "orgId": "200114152525",
                "payBankName": "广发银行股份有限公司",
                "payCardAttr": payCardAttr,
                "payCardType": "IC",
                "payMerchantCode": "84361105999000H",
                "payMerchantName": "南宁市荣瑞钢材批发部",
                "payOrderId": Common.payorderID(),
                "payRetCode": "00",
                "payRetMsg": "00+成功",
                "payTermnalCode": "23568861",
                "quickPassPay": quickPassPay,
                "refNo": "005265472458",
                "serverCode": serverCode,
                "settleDate": Common.dataTime(),
                "settleType": "D0",
                "t1Rate": str(rate1) + "|0|0|2000|0|0|00",
                "terminalCode": "14192710",
                "terminalSn": terminalSn,
                "tradeAmount": str(amount1),
                "transDate": Common.dataTime(),
                "transId": "5265432472458",
                "transNo": "472458",
                "transState": "S",
                "transTime": Common.datatime_hour(),
                "activityId": activityId,
                "enPayBankNo": '3B74B0C5E5C4119B1EAB4E9E6C831305',
                "voucherId": voucherId,
                "voucherFee": voucherFee
            },
            "head": {"localDate": "20200331", "localNo": "767409", "localTime": "092309"},
            "sign":
                "FVbkZ6ut753ZQ67LjnPU7KQ3k2GRlfa7oZYBhfdxXWbMq61BCYHlBDNm7PBGVViqhUaZIFavPdepmYf1s464F/yF2UFclkM7fyw3PhOAUXUHkkGrdaRQ4Zh6rNzrIdChjvBAEYLw0PaIVLmShnUSS+8OGSqYgytXsY+fY8FATn0="}
        ss = json.dumps(data)

        with self.client.post(url, data=ss, headers=headers) as respons:
            result = respons.json()
            if '处理成功' == result['msg']:
                respons.success()
            else:
                respons.failure(result['msg'])





class Websiteuser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
    host = 'http://47.112.191.144:8180'







if __name__ == '__main__':
    import os
    os.system("locust -f test_locust.py")
