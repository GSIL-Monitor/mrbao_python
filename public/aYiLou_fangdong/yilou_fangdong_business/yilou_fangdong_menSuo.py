# -*- coding: UTF-8 -*-
import logging.config

from CanShuPaiXu1 import Paixu
from common.data_shuju import DB
from read_Yaml_Config import Read_Yaml_Config
from request_bane import Request_

con_log=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

class MenSuo(Read_Yaml_Config,DB,Request_,Paixu):
    '''
    门锁
    '''
    def getNewDoorPWD(self,doorId,mobile,name):
        '''
        创建临时密码
        :param doorId: 门锁ID
        :return: 
        '''
        effectiveTime=self.get_time2()[1]
        expirationTime=self.get_time2()[2]

        send_url=self.get_peizhi('mensuo',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['addDoorGuestPwd']#获取门锁密码接口

        logging.info('url is %s'%send_url)

        send_dict={'doorId':doorId,'effectiveTime':effectiveTime,'expirationTime':expirationTime,'mobile':mobile,'name':name,'times':1}
        logging.info(send_dict)

        response=self.request_post(send_url,send_dict)

        return response

    def listDoorInfo(self,houseId):
        '''
        获取房源门锁列表
        :param houseId: 
        :return: 
        '''
        send_url=self.get_peizhi('mensuo',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['listDoorInfo']
        logging.info('url is %s' % send_url)
        send_dict={'houseId':houseId}
        logging.info(send_dict)
        response=self.request_post(send_url,send_dict)
        return response

    def getDoorBaseInfo(self,doorId):
        '''
        获取门锁基本信息
        :param doorId: 门锁id
        :return: 
        '''
        send_url=self.get_peizhi('mensuo',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['getDoorBaseInfo']
        logging.info(send_url)
        send_dict={'doorId':doorId}
        logging.info(send_dict)
        response=self.request_post(send_url,send_dict)
        return response

    def listDoorTempPWD(self,doorId):
        '''
        获取门锁临时密码列表
        :param doorId: 门锁id
        :return: 
        '''
        send_url=self.get_peizhi('mensuo',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['listDoorTempPWD']
        logging.info(send_url)
        send_dict={'doorId':doorId}
        logging.info(send_dict)
        response=self.request_post(send_url,send_dict)
        return response

    def listDoorOpen(self,doorId):
        '''获取门锁开门记录'''
        send_url = self.get_peizhi('mensuo', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['listDoorOpen']
        logging.info(send_url)
        send_dict = {'doorId': doorId}
        logging.info(send_dict)
        response = self.request_post(send_url, send_dict)
        logging.info(response)
        return response

if __name__ == '__main__':
    A=MenSuo()
    B=Paixu()
    #A.getNewDoorPWD(doorId=20789,mobile='18621512473',name='鲍涛2')
    A.listDoorInfo(1436)
    A.getDoorBaseInfo(20835)
    A.listDoorOpen(20997)
