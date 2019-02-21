import pymysql

def insert_table(article_title,article_author,article_content):
    #建立连接
    db=pymysql.connect(host='127.0.0.1',
                       user='root',
                       port=3306,
                       password='666888',
                       db='test',
                       charset='uft8'
    )
    #插入数据
    query_sql='select * from article where article_title=%s'
    sql='insert into article(article_title,article_author,article_content)values(%s,%s,%s)'
    #使用cursor()方法创建一个游标对象
    cursor=db.cursor()
    #执行SQL语句
    try:
        query_value=(article_title,)
        cursor.execute(query_sql,query_value)
        results=cursor.fetchall()
        if len(results)==0:
            value=(article_title,article_author,article_content)
            cursor.execute(sql,value)
            #提交事务
            db.commit()
            print('-------------{%s} insert table success--------'% article_title)
            return True
    except BaseException as e:
        db.rollback()
        print(e)
    finally:
        cursor.close()
        db.close()