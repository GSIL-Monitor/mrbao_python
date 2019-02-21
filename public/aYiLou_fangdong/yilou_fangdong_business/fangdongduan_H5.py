# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')

import logging.config
from read_Yaml_Config import Read_Yaml_Config
from request_bane import Request_
import random

con_log='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

class Fangdongduan_H5(Request_,Read_Yaml_Config):
    '''房东端H5'''
    def listUser(self,doorId):
        '''获取门锁所有有权限用户列表'''

        send_url = self.get_peizhi_(name='mensuo', yaml_ming='h5.yaml')
        send_url = send_url['listUser']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getDoorBaseInfo(self,doorId):
        '''获取门锁基本信息'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='h5.yaml')
        send_url = send_url['getDoorBaseInfo']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def unfreezeRenter(self,userId,doorId):
        '''房东解冻租客'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='h5.yaml')
        send_url = send_url['unfreezeRenter']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId,'userId':userId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def freezeRenter(self,userId,doorId):
        '''房东冻结租客'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='h5.yaml')
        send_url = send_url['freezeRenter']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId, 'userId': userId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

if __name__ == '__main__':
    A=Fangdongduan_H5()
    #A.listUser(31069)
    #A.getDoorBaseInfo(31069)
    #A.freezeRenter(userId=11209,doorId=31069)
    A.unfreezeRenter(userId=11209,doorId=31069)
    A.unfreezeRenter(userId=11209,doorId=31070)
    A.unfreezeRenter(userId=11508,doorId=31069)
    A.unfreezeRenter(userId=11508,doorId=31071)