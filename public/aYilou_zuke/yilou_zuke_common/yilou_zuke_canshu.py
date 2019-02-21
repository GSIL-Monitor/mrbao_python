# -*- coding: UTF-8 -*-
#aa=os.chdir(r'E:\Python_study\PYREQUESTS')
import hashlib
import logging.config
import time
from datetime import datetime, timedelta

from read_Yaml_Config import Read_Yaml_Config

con_log=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()
data_peizhi=Read_Yaml_Config()
data=data_peizhi.get_peizhi('header',yaml_ming='yilou_fangdong.yaml')
class Paixu(object):
    '''
    参数排序
    '''
    def get_time2(self,day=1,hours=1,minutes=1):
        #获取当前时间到日
        now_A=datetime.now().strftime('%Y-%m-%d')
        #获取当前时间到秒
        now_B=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_day=(datetime.now()+timedelta(days=day)).strftime('%Y-%m-%d')
        one_hours=(datetime.now()+timedelta(hours=hours)).strftime('%Y-%m-%d %H:%M:%S')#现有时间增加一个小时
        two_minutes=(datetime.now()+timedelta(minutes=minutes)).strftime('%Y-%m-%d %H:%M:%S')
        two_minutes1 = (datetime.now() + timedelta(minutes=minutes)).strftime('%Y-%m-%d %H:%M:%S')
        return now_A,now_B,one_hours,two_minutes,two_minutes1,add_day
    def get_time(self):
        #获取毫秒时间戳
        now = time.time()
        now_time = round(now /100)
        D = str(now_time)
        return D
    def get_time1(self):
        #秒时间戳
        now = time.time()
        now_time = round(now *1000)
        E = str(now_time)
        return E
    def get_canshu(self,a,b='pingguo'):
        '''
        #a参数   b安卓和ios系统
        :param a: 
        :param b: 
        :return: 
        '''
        list_1 = []
        header={}#定制请求头
        if isinstance(a, dict) != True:
            print("%s is not dict " % a)
        try:
            for key, value in a.items():
                canshu = '%s=%s' % (key, value)
                list_1.append(canshu)
                # logging.info('wei paixu canshu is %s'% list_1)
        except:
            print("报错了")
        finally:
            C = sorted(list_1)
            logging.info('now paixu canshu is %s ' % C)
        try:
            if b =='anzhuo':
                C.append(data['anzhuo'])
            elif b == 'pingguo':
                C.append(data['pingguo'])
            else:
                logging.info('zhe li you cuowu')
            str = '&'
            seq_canshu = str.join(C)
            D=self.get_time()
            seq_canshu = seq_canshu + '&' + D
            #logging.info('The laster canshu is %s' % seq_canshu)
            #print(seq_canshu)
            md5 = hashlib.md5()
            seq_canshu_utf8 = seq_canshu.encode(encoding='utf-8')
            md5.update(seq_canshu_utf8)
            B = md5.hexdigest()
            #logging.info('qian ming zifuchuan is %s' % B)
            app_secret = {'App-Secret': B}
            #print(app_secret)
            F=Paixu()
            E=F.get_time1()
            header['App-Secret']=B
            header['User-Agent'] = data['pingguo1']
            header['App_Time'] = E
            header['os'] = data['pingguo_os']
            header['Accept'] = data['accept']
            header['Content-Type'] = data['content_type']
            header['imei'] = data['imei']
            header['Accept-Encoding'] = data['accept_encoding']
            header['Data-Type'] = data['data_type']
            header['ver'] = data['ver']
            logging.info(header)
            return B, header
        except:
            print('This is False')
if __name__ == '__main__':
    A=Paixu()
    #a={'a':Xiaoxiangyoupin,'b':'adas'}
    #A.get_canshu(a,'pingguo')
    print(A.get_time2(day=-1)[5])

    #print(aa)