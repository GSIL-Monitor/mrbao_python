# -*- coding: utf-8 -*-d
import pymysql
conn=pymysql.connect(host="127.0.0.1",
                     user="root",
                     password="666888",
                     port=3306,
                     db="test",
                     charset="utf8"
)
cursor=conn.cursor()
sql="select * from trade;"
try:
    cursor.execute(sql)
    result=cursor.fetchall()
    #conn.commit()
    for results in result:
        print(results)
    print('select table success')
except BaseException as e:
    conn.rollback()
    print('create table false')
#finally:
    #cursor.close()
    #conn.close()
def insert_data():
    sql="insert into article(id,article_title,article_author,article_content) values (%s,%s,%s,%s)"
    value=((1,'jack','insert into ok','ok ok ok'),(2,'fire','is ok','ok'),(3,'writer','ok','ok'),(4,'hello','world','hello world'))
    cursor.execute(sql,value[3])
    cursor.execute(sql,value[0])
    cursor.execute(sql,value[1])
    cursor.execute(sql,value[2])
insert_data()
sql="select * from article;"
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for result in results:
        print(result)
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()