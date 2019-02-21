# -*- coding: UTF-8 -*-
import pymysql
class DB:
    '''数据库有封装'''
    def __init__(self):
        self.__host='127.0.0.1'#ip
        self.__port=3306#端口
        self.__user='root'#用户名
        self.__password='666888'#密码
        self.__db_name='autotest'#库民
        self.__charset='utf8'

    def db_select(self,sql_name):
        con=pymysql.connect(host=self.__host,port=self.__port,user=self.__user,password=self.__password,
                            db=self.__db_name,charset=self.__charset)#获取数据库连接
        cur=con.cursor()#获取数据库游标
        cur.execute(sql_name)#执行测试
        result = cur.fetchall()#获取执行结果
        return result
    def db_update(self):
        pass
    def db_delete(self):
        pass
    def db_insert(self):
        pass
if __name__ == '__main__':
    A=DB()
    sql_name='select * from autotest.apitest_modules_interface;'
    b=A.db_select(sql_name)
    print(type(b))
    for i in b:
        print(i)
