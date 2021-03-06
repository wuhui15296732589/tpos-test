﻿#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/9/28

import requests,json
from common import Common
from decimal import Decimal
url = 'http://47.112.191.144:8180/tpos-api-web-srv/api_075'             #tpos
#url='http://47.112.186.194:8180/kpos-api-web-srv/api_075'               #kpos

amount1 = 1000009             #交易金额（分）
rate1 = 0.58                #交易费率（%）
defee = 300                 #单笔手续费（分）
merchantCode = '77910589355309D'                    #商户号
terminalSn = '20201111000010090003'                 #sn号
activityId = 'H0441'                                 #押金类型（H0421 = 39     H0441 = 69      H0422 = 99      H0423 = 139）(押金类型对应交易金额则为押金支付交易)
voucherId =''                                       #sim扣费（MKA_0024），不填为不扣费
voucherFee = ''                                   #sim扣费金额：3600，不填为不扣费
payCardAttr = '1'                                 #交易卡类型（1:借记卡 2:贷记卡 3：无卡）
quickPassPay = '0'                                #交易类型0:普通交易 1：云闪付优惠 2：小额双免优惠
serverCode = '10001'                               #交易编码交易编码10001：刷卡 10002：微信10003:NFC 10004：支付宝 10005：银联二维码

headers = {
	'Content-Type': 'application/json',
	'User-Agent': 'PostmanRuntime/7.26.3',
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br'
	}
data = {
    "bizType":"P01",
    "body":{
        "addFee":"0",
        "amount":amount1 - int(amount1 * rate1 *0.01) - defee,
        "cardNo":"625809******6046",
        "d0Rate": str(rate1) +"|0|0|1900|0|0|00",
        "dfFee":defee,
        "fee": int(amount1 * rate1 *0.01),
        "merchantCode":str(merchantCode),
        "orgId":"200114152525",
        "payBankName":"广发银行股份有限公司",
        "payCardAttr":payCardAttr,
        "payCardType":"IC",
        "payMerchantCode":"84361105999000H",
        "payMerchantName":"南宁市荣瑞钢材批发部",
        "payOrderId":Common.payorderID(),
        "payRetCode":"00",
        "payRetMsg":"00+成功",
        "payTermnalCode":"23568861",
        "quickPassPay":quickPassPay,
        "refNo":"005265472458",
        "serverCode":serverCode,
        "settleDate":Common.dataTime(),
        "settleType":"D0",
        "t1Rate":str(rate1) +"|0|0|1900|0|0|00",
        "terminalCode":"14192710",
        "terminalSn":terminalSn,
        "tradeAmount":str(amount1),
        "transDate":Common.dataTime(),
        "transId":"5265432472458",
        "transNo":"472458",
        "transState":"S",
        "transTime":Common.datatime_hour(),
        "activityId":activityId,
        "enPayBankNo":'3B74B0C5E5C4119B1EAB4E9E6C831305',
        "voucherId":voucherId,
        "voucherFee":voucherFee
    },
    "head":{"localDate":"20200331", "localNo":"767409", "localTime":"092309"},
    "sign":
    "FVbkZ6ut753ZQ67LjnPU7KQ3k2GRlfa7oZYBhfdxXWbMq61BCYHlBDNm7PBGVViqhUaZIFavPdepmYf1s464F/yF2UFclkM7fyw3PhOAUXUHkkGrdaRQ4Zh6rNzrIdChjvBAEYLw0PaIVLmShnUSS+8OGSqYgytXsY+fY8FATn0="}
ss = json.dumps(data)
respons =requests.post(url,data=ss,headers= headers)
print(respons.text)
