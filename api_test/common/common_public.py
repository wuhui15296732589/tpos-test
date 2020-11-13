import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree

from testFile import readConfig
import random
import pymysql
import datetime
from common.Log import MyLog as Log


proDir = readConfig.proDir

log = Log.get_log()
logger = log.logger


# 从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    cls = []
    # get xls file's path
    xlsPath = os.path.join(proDir, xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

# 从xml文件中读取sql语句
# database = {}
# def set_xml():
#     if len(database) == 0:
#         sql_path = os.path.join(proDir, "sql.xml")
#         tree = ElementTree.parse(sql_path)
#         for db in tree.findall("database"):
#             db_name = db.get("name")
#             # print(db_name)
#             table = {}
#             for tb in db.getchildren():
#                 table_name = tb.get("name")
#                 # print(table_name)
#                 sql = {}
#                 for data in tb.getchildren():
#                     sql_id = data.get("id")
#                     # print(sql_id)
#                     sql[sql_id] = data.text
#                 table[table_name] = sql
#             database[db_name] = table
#
# def get_xml_dict(database_name, table_name):
#     set_xml()
#     database_dict = database.get(database_name).get(table_name)
#     return database_dict
#
# def get_sql(database_name, table_name, sql_id):
#     db = get_xml_dict(database_name, table_name)
#     sql = db.get(sql_id)
#     return sql

def __GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st

def __first_name():  #   随机取姓氏字典
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

def __second_name():
    # 随机取数组中字符，取到空字符则没有second_name
    second_name_list = [__GBK2312(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name

def __last_name():
    return __GBK2312()


#随机生成商户名称
def customer_name():
    name = __first_name() + __second_name() + __last_name()
    return name

#随机生成商户公司名称
def customer_name_company():
    str = '有限责任公司'
    return customer_name()+str

#随机生成身份证号码
def id_card_number():
    prefix = '14270319911017'
    last_number = random.randint(1000,9999)
    return prefix+str(last_number)


#随机生成银行卡号
def bank_number():
    prefix = '621700036000308'
    last_number = random.randint(1000,9999)
    return prefix+str(last_number)

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



def URL():
    readcon = readConfig.ReadConfig()
    baseurl = readcon.get_http('baseurl')
    port = readcon.get_http('port')
    app = readcon.get_http('app')
    url = baseurl+':'+port+app
    return url




def App_head():
    '''
    app请求头
    :return:
    '''
    header = {"MAC":"F932E16F-D688-49FC-BC2B-D21A3A6A2C2B",
              "TYPE":"1",
              "VERSION":"100",
              "IP":"10.10.47.25",
              "TOKEN":"vqtQipq6K72Hw9NZf6DQoqnlGGub5U4qpZBCjQeal3Po+P7eYbwGmVR1yuxxDBbVE6xmrTGcWdWsUWNiSEWCFg\u003d\u003d",
              "ACCOUNT_TYPE":"1"}

    return header


def APP_headers():
    headers = {'Content - Type': 'application / x - www - form - urlencoded;charset = utf - 8',
    'Content - Length': '299',
    'Host': '47.112.191.144: 8180',
    'Connection': 'Keep - Alive',
    'Accept - Encoding': 'gzip',
    'User - Agent': 'okhttp / 3.10.0',}





if __name__ == '__main__':
   logger.logger.info('000000000000000000000000000')