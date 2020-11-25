#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/9/28

import random
import pymysql
import datetime

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st

def first_name():  #   随机取姓氏字典
    first_name_list = [
        '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
        '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
        '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
        '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
        '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
        '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
        '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    n = random.randint(0, len(first_name_list) - 1)
    f_name = first_name_list[n]
    return f_name

def second_name():
    # 随机取数组中字符，取到空字符则没有second_name
    second_name_list = [GBK2312(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name

def last_name():
    return GBK2312()


#随机生成商户名称
def customer_name():
    name = first_name() + second_name() + last_name()
    return name



class random_moblie_card:
    #随机生成商户手机号
    def customer_moblie(self):
        s = random.randint(1000,9999)
        t= str('1540000')+str(s)
        list = random_moblie_card.mysql_open(self)[0]
        if t not in list:
            return t
        else:
            return random_moblie_card.customer_moblie()

    #随机生成商户号
    def customer_card(self):
        card1 = random.randint(10000,99999)
        card2 = str('298467982')+str(card1)
        list = random_moblie_card.mysql_open(self)[1]
        if card2 not in list :
            return card2
        else:
            return random_moblie_card.customer_card()

    #查询库中已存的商户号，手机号，
    def mysql_open(self):
        db = pymysql.connect(host='120.79.180.225', port=3306, user='query', password='2wsx@WSX', db='oem3')
        cursor = db.cursor()
        sql ='SELECT mobile,customer_code from t_customer'
        cursor.execute(sql)
        data =cursor.fetchall()
        cursor.close()
        db.close()
        if data:
            list = []
            list2 = []
            for i in range(len(data)):
                list.append(data[i][0])
                list2.append(data[i][1])

            list3 = [list,list2]
            return list3


#获取当前时间(年-月-日：00000000)
def dataTime():
    time = datetime.datetime.now()
    year = str(time.year)
    if time.month < 10:
        month = str('0')+ str(time.month)
    else:
        month = str(time.month)

    if time.day <10:
        day = str('0') + str(time.day)
    else:
        day = str(time.day)

    data = str(year)+ str(month) + str(day)

    return data

#获取当前时间（时-分-秒：000000）
def datatime_hour():
    time = datetime.datetime.now()
    if time.hour < 10:
        hour = str('0')+ str(time.hour)
    else:
        hour = str(time.hour)

    if time.minute <10:
        minute = str('0')+ str(time.minute)
    else:
        minute = str(time.minute)

    if time.second <10:
        second = str('0') + str(time.second)
    else:
        second = str(time.second)


    return hour + minute + second



def payorderID():

    s = str('738465897')
    r = random.randint(10000,99999)
    return s+str(r)

def fee():
    #费率范围内随机生成
    fee = random.randint(530,601)
    return fee*0.001

def URL():
    url = "http://47.112.191.144:8180/"
    return url

def Pc_header():
    '''
    pc端请求头
    :return:
    '''
    header ={
	'Content-Type': 'application/json',
	'User-Agent': 'PostmanRuntime/7.26.3',
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br'
	}

    return header


def App_header():
    '''
    app请求头
    :return:
    '''
    header = {"MAC":"F932E16F-D688-49FC-BC2B-D21A3A6A2C2B","TYPE":"1","VERSION":"100",
                         "IP":"10.10.47.25","TOKEN":"","ACCOUNT_TYPE":"1"}

    return header

def serverCode():
    # 交易编码交易编码10001：刷卡 10002：微信10003:NFC 10004：支付宝 10005：银联二维码
    list = ['10001','10002','10003','10004','10005']
    s  = random.randint(0,len(list)-1)
    return list[s]

def amount():
    #随机生成交易金额
    return random.randint(1000,3000000)


def merchantCode_terminalSn():
    list = (["84324115499000A","00000020201022000010009104"],["84319185499000A","00005702251070000013"],
            ["94312471831253D","12345123451236020000"],["56007396276243D","20201010000111001045"],
            ["77910589355309D","20201111000010090003"],["28960228891747D","20201111000010090001"])
    s = random.randint(0,len(list)-1)
    list1 = [list[s][0],list[s][1]]
    return list1

if __name__ == '__main__':
    s = random.randint(0,2)
    print(s)

