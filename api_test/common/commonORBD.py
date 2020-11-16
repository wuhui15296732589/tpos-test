#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by HuiWu
# Create on 2020/11/10
import cx_Oracle
from testFile import readConfig as readConfig
from common.Log import MyLog
localReadConfig = readConfig.ReadConfig()

log = MyLog.get_log()
logging = log.logger

class MyORDB:


    def __init__(self):

        self.logger = logging
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            # connect to DB
            self.db = cx_Oracle.connect(localReadConfig.get_orcle_db("username"),
                                        localReadConfig.get_orcle_db('password'),
                                        localReadConfig.get_orcle_db('host'))
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except cx_Oracle.DatabaseError as ex:
            self.logger.info(str(ex))



    def executeSQL(self, sql):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed!")



if __name__ == '__main__':
    mydb = MyORDB()
    st = mydb.executeSQL('SELECT customer_id FROM t_pos')
    ss = mydb.get_all(st)
    print(ss)
