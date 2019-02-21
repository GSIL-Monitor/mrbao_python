#coding:utf-8

import logging.config
import re
import pymysql
from CanShuPaiXu1 import Paixu
from read_Yaml_Config import Read_Yaml_Config

con_log=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

datapeizhi=Read_Yaml_Config()
data=datapeizhi.get_peizhi('mysqlconf',yaml_ming='yilou_fangdong.yaml')

test_data=datapeizhi.get_peizhi('test_mysql',yaml_ming='yilou_fangdong.yaml')
beta_data=datapeizhi.get_peizhi('beta_table',yaml_ming='shujuku.yaml')
class DB(Paixu):
    '''
    数据库封装
    '''
    def get_YanZhengMa(self,mobile):
        #beta_获取短信验证码
        sql=" select content  from fyb_sms where mobile="+mobile+";"
        conn=pymysql.connect(host=data['host'],user=data['user'],password=data['password'],port=data['port'],db=data['db_name'],charset=data['charset'])#l链接数据库
        cur=conn.cursor()#获取游标
        cur.execute(sql)#查询SQL
        result=cur.fetchall()#查询结果z
        #print(result)
        #logging.info(" Select result is %s "% result)
        content=re.compile('验证码是：(.*?)，请妥善保管，10分钟内有效。')
        content=content.findall(str(result))
        try:
            yanzhengma = content.pop()
            if yanzhengma is None:
                logging.info("yanzhengma is None")
            else:
                logging.info("shoujihao shi %s de yanzhengma wei %s" % (mobile,yanzhengma))
            return yanzhengma
        except:
            logging.info("yanzhengma is None")

    def select_sql(self,a,b):
        #查询数据操作
        sql="select"+a+"from"+b+";"
        conn=pymysql.connect(host=data['host'],user=data['user'],password=data['password'],port=data['port'],db=data['db_name'],charset=data['charset'])#链接数据库
        cur=conn.cursor()#获取游标
        cur.execute(sql)#查询sql
        result=cur.fetchall()#获取查询结果
        #print(result)
        return str(result)

    def get_UserId(self,shuzi,mobile='',doorId=''):
        '''
        beta获取userid,realname
        :param shuzi: 0
        :param mobile: 
        :return: 
        '''
        swith_state={
            0:'userId',
            1:'realname',
            2:'doorId'
        }

        con = pymysql.connect(host=data['host'], user=data['user'], password=data['password'], port=data['port'],
                              db=data['db_name1'], charset=data['charset'])
        if shuzi==0:
            sql='select '+ swith_state[0] +' from fdb_user where mobile ='+mobile+';'
            cur = con.cursor()
            cur.execute(sql)
            result1 = cur.fetchall()
            result1 = result1[0][0]
            logging.info('%s is %s'%(swith_state[0],result1))
            return result1

        elif shuzi==1:
            sql='select '+ swith_state[1] +' from fdb_user where mobile ='+mobile+';'
            cur = con.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            result = result[0][0]
            logging.info('%s is %s' % (swith_state[1], result))
            return result

class Test_Db(Paixu):
    def _select(self,db_name,library_name):
        '''测试环境查询'''
        sql='select * from' + library_name +';'
        conn = pymysql.connect(host=test_data['host'], user=test_data['user'], password=test_data['password'], port=test_data['port'],
                               db=db_name, charset=test_data['charset'])  # l链接数据库
        cur=conn.cursor()#获取游标

        cur.execute(sql)#执行sql

        result=cur.fetchall()
        logging.info(result)
        print(len(result))

    def select_room_data(self,report_date,hasLock='1'):
        '''
        测试环境查询
        :param report_date: 日期往前减多少天
        :return: 
        '''
        #sql='select viewCount from fdb_report_day_house_view where  reportDate = '+report_date+';'
        sql="select viewCount from report_beta.fdb_report_day_house_view where reportDate="+report_date+ " and hasLock = "+ hasLock+";"
        logging.info(sql)
        conn = pymysql.connect(host=data['host'], user=data['user'], password=data['password'], port=data['port'],
                                charset=data['charset'])  # l链接数据库
        cur=conn.cursor()#获取游标

        cur.execute(sql)#执行sql

        result=cur.fetchall()
        logging.info(result[0][0])
        return result[0][0]

if __name__ == '__main__':
    a=Test_Db()
    #print(a.get_YanZhengMa("18621512473"))
    b=DB()
    b.get_YanZhengMa("18621509417")
    #print(a.get_UserId(shuzi=1,mobile='18621512473'))
    #report_date=a.get_time2(day=-7)[5]
    #report_date="\'"+report_date+'\''
    #print(a.select_room_data(report_date=report_date))



