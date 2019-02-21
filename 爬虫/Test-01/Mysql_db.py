import pymysql
import os
import configparser as e

''''#========读取db_config.ini 文件设置=======
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
password=cf.get("mysqlconf","password")'''

base_dir=str(os.path.dirname(__file__))
print(base_dir)
file_path=base_dir+"/mysql.ini"
print(file_path)
cf=e.ConfigParser()
cf.read(file_path)
host=cf.get("mysqlconf","host")
port=cf.get("mysqlconf","port")
db_name=cf.get("mysqlconf","db")
user=cf.get("mysqlconf","user")
password=cf.get("mysqlconf","password")
print(host,port,db_name,user,password)

def create_table():
    #建立数据库连接
    db=pymysql.connect(host=host,
                       user=user,
                       password=password,
                       db=db_name,
                       charset='utf8mb4'
    )
    #创建名为article数据库语句
    sql='''create table if not exists article(
    id int not null auto_increment,
    article_title text,
    article_author text,
    article_content text,
    primary key ('id')
    )'''
    #使用cursor()方法创建一个游标对象
    cursor=db.cursor()
    try:
        #执行 SQL 语句
        cursor.execute(sql)
        result=cursor.fetchall()#获取查询结果
        #提交事务
        db.commit()
        print('create table success')
    except BaseException as e:#如果发生错误则回滚
        db.rollback()
        print(e)
    finally:
        #关闭游标链接
        cursor.close()
        #关闭数据库连接
        db.close()
if __name__=='__main__':
    create_table()