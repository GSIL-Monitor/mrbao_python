from pymysql import connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
import pymysql

'''
pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(op)     执行一个数据库的查询命令
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
rowcount()      返回数据条数或影响行数
close()         关闭游标对象
'''

#========读取db_config.ini 文件设置=======
base_dir=str(os.path.dirname(os.path.dirname(__file__)))
#a=os.path.dirname(__file__)
#print(a)
base_dir=base_dir.replace('\\','/')
print(base_dir)
file_path=base_dir+"/db.confif.ini"
print(file_path)

cf=cparser.ConfigParser()
cf.read(file_path)

host=cf.get("mysqlconf","host")
port=cf.get("mysqlconf","port")
db=cf.get("mysqlconf","db_name")
user=cf.get("mysqlconf","user")
password=cf.get("mysqlconf","password")

#======封装mysql 基本操作======
class DB:
    def __init__(self):
        try:
            # 连接数据库
            self.conn=pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=db,
                             charset='utf8mb4',
                             cursorclass=cursors.DictCursor)
            self.cursor = self.conn.cursor()
        except OperationalError as a:
            print("mysql error %d: %s " % (a.args[0],a.args[1]))
#SELECT SQL
    def select_sql(self,sql=''):
        try:
            self.cursor.execute(sql)
            self.cursor.commit()
            result=self.cursor.fetchall()
            return  print(result)
        except:
            error="select sql is error"
            print(error)
#DELETE SQL
    def delete_sql(self,table_name):
        sql="delete table "+table_name+";"
        try:
            self.cursor.execute(sql)
            self.cursor.commit()
        except:
            self.cursor.rollback()
            print("Delete database is error")
#UPDATE SQL
#带参数的更新方法，sql='insert into testtable values(%s,%s,%s,now()',params=(6,'','')
    def update1_sql(self,sql,params):
        try:
            self.cursor.execute(sql,params)
            self.cursor.commit()
        except:
            self.cursor.rollback()
            error=" uptate is error "
            print(error)
#不带参数
    def update2_sql(self,sql):
        try:
            self.cursor.execute(sql)
            self.cursor.commit()
        except:
            self.cursor.rollback()
            error="update is error"
            print(error)
a=DB()
a.select_sql('select * from web_event;')

    #清除数据
   # def clear(self,table_name):
    #real_sql="truncate table"+table_name+";"
       # real_sql="delete from"+table_name+";"
       # with self.conn.cursor() as cursors:
           # cursors.execute("SET FOREIGN_KEY_CHECKS=0;")
            #cursors.execute(real_sql)
       # self.conn.commit()
    #插入数据
    #def insert(self,table_name,table_data):
       # for key in table_data:
           # table_data[key]="'"+str(table_data[key])+"'"
        #key=','.join(table_data.key())
       # value=','.join(table_data.values())
      #  real_sql="INSERT INTO"+table_name+"("+key+") VALUES ("+value+")"
       # #print(real_sql)
        #with self.conn.cursor() as cursors:
          #  cursors.execute(real_sql)
       # self.conn.commit()
    #关闭数据库
    #def close(self):
        #self.conn.close()

#if __name__=='__main__':
    #db=DB()
    #table_name="sign_event"
   # table_data={'id':12,'name':'红米','limit':2000,'status':1,'address':'北京会展中心','start_time':'2016-08-20 00:25:42'}
    #db.clear(table_name)
   # db.insert(table_name,table_data)
  #  db.close()
