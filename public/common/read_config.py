# -*- coding: UTF-8 -*-
import os
import logging.config
import configparser as con
con_log='../config/logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()
base_dir=os.path.dirname(os.path.dirname(__file__))
file_dir=base_dir+"/config/db_confif.ini"
cf=con.ConfigParser()
cf.read(file_dir)
print(cf.get("header","pingguo"))

class Read_Config(object):
    '''
    读取yaml配置类
    '''
    def __init__(self,configparser):

        self.configparser=configparser

    def get_ini_peizhi(self,name,name2):
        '''
        获取配置        
        :param name: 父类名
        :param name2: 子类名
        :return: 
        '''
        try:
            if name!=None:
                logging.info('name is %s'%name)
        except :
            logging.info('name is not Null')
        else:
            cf=self.configparser.ConfigParser()
            cf.read(file_dir)
            name2=cf.get(name,name2)
        return name2
if __name__ == '__main__':
    A=con
    data=Read_Config(A)
    print(data.get_ini_peizhi('header','pingguo1'))
