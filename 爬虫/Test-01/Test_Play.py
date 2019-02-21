import requests
import pymysql
from bs4 import BeautifulSoup
import time
import sched
import os
import configparser as e
'''base_dir=os.path.dirname(__file__)
file_dir=base_dir+'/mysql.ini'
cf=e.ConfigParser()
cf.read(file_dir)
host=cf.get("mysqlconf","host")
port=cf.get("mysqlconf","port")
db_name=cf.get("mysqlconf","db")
user=cf.get("mysqlconf","user")
password=cf.get("mysqlconf","password")
print(host,port,db_name,user,password)
'''
def create_table():
    #建立链接
    con=pymysql.connect(host="127.0.0.1",
                        user="root",
                        #port=3306,
                        password="666888",
                        db="test")
    sql = '''create table if not exists article(
     id int not null auto_increment,
     article_title text,
     article_author text,
     article_content text,
     primary key ('id')
     )'''
    cursor=con.cursor()#创立游标
    try:
        cursor.execute(sql)
        con.commit()
        print('create table success')
    except:
        con.rollback()
        print('create table is faile')
    finally:
        cursor.close()
        con.close()
def insert_table(article_title,article_author,article_content):
    #建立连接
    conn=pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="666888",
        port=3306,
        db="test",
        charset="utf8"
    )

    query_sql="select * from article where article_title=%s;"
    sql="insert into article(article_title,article_author,article_content) values(%s,%s,%s);"
    cursor=conn.cursor()
    try:
        quer_value=(article_title,)
        cursor.execute(query_sql,quer_value)
        result=cursor.fetchall()
        if len(result)==0:
            value=(article_title,article_author,article_content)
            cursor.execute(sql,value)
            conn.commit()
            print('--------------{%s} insert table success----------'% article_title)
            return True
        else:
            print('---------------{%s} is exists---------'% article_title)
            return False
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def get_html_data():
    url="https://meiriyiwen.com/random"
    response=requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    article = soup.find('div', id='article_show')
    article_title = article.h1.string
    print('article_title=%s' % article_title)
    article_author = article.find('p', class_='article_author').string
    print('article_author=%s' % article.find('p', class_='article_author').string)
    article_contents = article.find('div', class_='article_text').find_all('p')
    article_content = ''
    for content in article_contents:
        article_content = article_content + str(content)
        print('article_content=%s' % article_content)
    insert_table(article_title,article_author,article_content)

get_html_data()