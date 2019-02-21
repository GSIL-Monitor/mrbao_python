# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')

import logging.config

from read_Yaml_Config import Read_Yaml_Config
from data_shuju import DB
from request_bane import Request_
import random


con_log='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

class FuanYuan(Request_,Read_Yaml_Config,DB):
    '''
    房源信息
    '''

    def myHouseContractCount(self):
        '''
        获取首页待办事项
        :return: 
        '''
        send_url = self.get_peizhi_(name='fangyuan', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['myHouseContractCount']
        logging.info('url is %s' % send_url)

        send_dict = {'': ''}

        response = self.request_post(base_url=send_url, dict_data=send_dict)

        return response

    def queryEstate(self,xiaoqu_Name='万科翡翠公园'):
        '''获取estateList'''
        send_url = self.get_peizhi_(name='New_source', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['queryEstate']
        logging.info('url is %s' % send_url)

        send_dict = {'keyword': xiaoqu_Name}

        response = self.request_post(base_url=send_url, dict_data=send_dict)

        return response

    def querySubEstates(self,estateId = 83505):
        '''获取subEstateId'''
        send_url = self.get_peizhi_(name='New_source', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['querySubEstates']
        logging.info('url is %s' % send_url)

        send_dict = {'estateId': estateId}

        response = self.request_post(base_url=send_url, dict_data=send_dict)

        return response

    def publish_joint_rent_house(self,estateId=83505,estateName="万科翡翠公园",subEstateId=135608,subEstateName='百业路',roomCount=2):
        '''发布合租房子'''

        send_url = self.get_peizhi_(name='New_source', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['publish_joint_rent_house']
        logging.info('url is %s' % send_url)
        building=random.randint(0,10)
        room=random.randint(0,10)
        send_dict = {'building':building,'decorateType':3,'estateId':estateId,'estateName':estateName,
                     'houseType' : 3,'layers' : 0,'onlyOne' : 0,'payMethod' : 0,'room':room,'roomCount':roomCount,
                     'subEstateId':subEstateId,'subEstateName':subEstateName,'ventilation' : 0}

        response = self.request_post(base_url=send_url, dict_data=send_dict)

        return response

    def publish_rent(self,estateId=62,estateName="阳光公寓",subEstateId=87665,subEstateName='陆家浜路305弄',wcSum=1,houseType=2):
        '''发布整租'''
        building = random.randint(0, 10)
        room = random.randint(0, 10)
        send_url = self.get_peizhi_(name='New_source', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['publish_rent']
        logging.info('url is %s' % send_url)

        send_dict = {'bedroomSum':2,'building': 2, 'decorateType': 3, 'estateId': estateId, 'estateName': estateName,'holdYear':0,'floor':0,
                     'houseType': houseType, 'layers': 0, 'livingRoomSum':0,'loan':0,'onlyOne': 0, 'payMethod': 2, 'room': 2,
                     'subEstateId': subEstateId, 'subEstateName': subEstateName, 'ventilation': 5,'wcSum':wcSum}

        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def removeHouse(self,houseId):
        '''删除房屋'''
        send_url = self.get_peizhi_(name='New_source', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['removeHouse']
        logging.info('url is %s' % send_url)

        send_dict = {'houseId': houseId}

        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def update_rent(self,rentId,houseId=''):
        '''房间添加面积和租金'''
        send_url = self.get_peizhi_(name='New_source', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['update_rent']
        logging.info('url is %s' % send_url)
        roomName=random.randint(0,100)
        price=random.randint(0,10000)
        spaceArea=random.randint(0,10000)

        send_dict = {'houseId': houseId,'genderRequirement':1,'payMethod':2,'rentId':rentId,'roomName':roomName,'roomType':0
            ,'ventilation':3,'price':price,'spaceArea':spaceArea}

        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def applyInstallLock(self,houseId):
        '''申请装锁'''
        send_url = self.get_peizhi_(name='New_source', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['applyInstallLock']
        logging.info('url is %s' % send_url)

        send_dict = {'houseId': houseId}

        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def cancelDoorInstallApply(self,houseId):
        '''装锁审核中取消申请装锁'''
        send_url = self.get_peizhi_(name='New_source', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['cancelDoorInstallApply']
        logging.info('url is %s' % send_url)

        send_dict = {'houseId': houseId,'source':1}

        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def myHouseList1(self,*canshu):
        '''获取房源列表 '''
        send_url=self.get_peizhi_(name='fangyuan',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['myHouseList1']
        logging.info('url is %s' % send_url)

        send_dict={'pageSize':20,'offset':0}

        response=self.request_post(base_url=send_url,dict_data=send_dict)

        return response

    def getJointRentHouseDetail(self,houseId):
        '''
        71获取合租房子详情 请求参数{“houseId”:111}
        :param houseId: 
        :return: 
        '''
        send_url=self.get_peizhi_(name='fangyuan',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['getJointRentHouseDetail']
        logging.info('url is %s' % send_url)

        send_dict={'houseId':houseId}

        response=self.request_post(base_url=send_url,dict_data=send_dict)

        return response
    def listJointRentRoom(self,houseId):
        '''
        72获取合租房间列表  请求参数{“houseId”:111}
        :param houseId: 
        :return: 
        '''
        send_url=self.get_peizhi_(name='fangyuan',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['listJointRentRoom']
        logging.info('url is %s' % send_url)

        send_dict={'houseId':houseId}

        response=self.request_post(base_url=send_url,dict_data=send_dict)

        return response

    def houseDetail(self,id):
        '''
        72获取合租房间列表  请求参数{“houseId”:111}
        :param houseId: 
        :return: 
        '''
        send_url=self.get_peizhi_(name='fangyuan',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['houseDetail']
        logging.info('url is %s' % send_url)

        send_dict={'id':id,"bizType":1}

        response=self.request_post(base_url=send_url,dict_data=send_dict)

        return response

    def myHouseEstate(self,houseId):
        '''
        72获取合租房间列表  请求参数{“houseId”:111}
        :param houseId: 
        :return: 
        '''
        send_url=self.get_peizhi_(name='fangyuan',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['myHouseEstate']
        logging.info('url is %s' % send_url)

        send_dict={'houseId':houseId}

        response=self.request_post(base_url=send_url,dict_data=send_dict)

        return response

if __name__ == '__main__':
    A=FuanYuan()
    #A.myHouseContractCount()
    #A.myHouseList1()
    #A.getJointRentHouseDetail('54654')
    #A.listJointRentRoom('4234')
    #A.houseDetail('')
    #A.queryEstate(xiaoqu_Name='111www')
    #A.querySubEstates()
    #A.publish_joint_rent_house()
    #A.removeHouse(houseId=1702)
    #A.update_rent(rentId='5155',roomName='2',price='2',spaceArea='2',houseId='1718')
    #A.publish_joint_rent_house()
    #A.getJointRentHouseDetail(1871)
    A.publish_rent()
    #A.queryEstate(xiaoqu_Name='阳光公寓')
    #A.querySubEstates(estateId=62)

