# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')

import logging.config
from fuangYuanXinXi import FuanYuan
con_log=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()


class FuanYuan_Parameters(FuanYuan):
    '''接口参数获取'''
    def myHouseList_parameters(self,FangYuan_Name='汤臣一品',Room_Name='房间01'):
        '''
        获取具体房源列表参数
        :return: 
        '''
        joint_rent={}#合租
        renting_rent={}#整租
        result=self.myHouseList1()
        data_row=result['data']['rows']#获取接口返回数据
        if data_row==None:
            logging.info('获取数据错误')
        if data_row!=None:
            for index, value in enumerate(data_row):  # 遍历数据所在位置
                if FangYuan_Name in value['estateName']:  # index 列表索引  value 索引值
                    data_result = data_row[index]
                    if data_result['allRentTag'] == 0 and data_result['jointRentTag'] == 1:  # 判断房源是否为合租
                        logging.info("%s是合租" % FangYuan_Name)
                        if data_result['doorLockInfo'] != None:
                            doorLockInfo_id = data_result['doorLockInfo']['id']  # 获取大门门锁ID
                            logging.info("大门锁的ID为%s" % doorLockInfo_id)
                            joint_rent['doorLockInfo_id'] = doorLockInfo_id

                        if data_result['rentId'] != None:
                            houseId = data_result['rentId']  # 获取房源ID
                            logging.info("房源ID为%s" % houseId)
                            joint_rent['houseId'] = houseId

                        if data_result['jointRentRoomModelList'] != None:  # 获取合租房源信息
                            for room_index, room_value in enumerate(
                                    data_result['jointRentRoomModelList']):  # room_index列表索引,room_value索引值
                                if Room_Name in room_value['roomNoStr']:
                                    room_data = data_result['jointRentRoomModelList'][room_index]  # 获取对应的房间列表信息
                                    if room_data['contractId'] != None:
                                        logging.info("%s 的合同ID为 %s" % (Room_Name, room_data['contractId']))  # 获取房间合同ID
                                        joint_rent['contractId'] = room_data['contractId']

                                    if room_data['doorLockInfo'] != None:
                                        room_doorLockInfo_id = room_data['doorLockInfo']['id']  # 获取房间门锁ID
                                        logging.info("%s 锁的ID为%s" % (Room_Name, room_doorLockInfo_id))
                                        joint_rent['room_doorLockInfo_id'] = room_doorLockInfo_id

                                    if room_data['rentId'] != None:
                                        room_rentId = room_data['rentId']
                                        joint_rent['room_rentId'] = room_rentId
                                        logging.info(room_rentId)

                                    if room_data['roomNo'] != None:
                                        room_roomNo = room_data['roomNo']
                                        joint_rent['room_roomNo'] = room_roomNo

                                    if room_data['lookState'] != None:
                                        room_lookState = room_data['lookState']  # 获取房间带看状态
                                        logging.info("%s 的当前状态为%s" % (Room_Name, room_lookState))
                                        joint_rent['room_lookState'] = room_lookState

                    if data_result['allRentTag'] == 1 and data_result['jointRentTag'] == 0:  # 判断房源为整租
                        logging.info("%s是整租" % FangYuan_Name)

                        if data_result['doorLockInfo'] != None:
                            doorLockInfo_id = data_result['doorLockInfo']['id']  # 获取大门门锁ID
                            logging.info("大门锁的ID为%s" % doorLockInfo_id)
                            renting_rent['doorLockInfo_id'] = doorLockInfo_id

                        if data_result['rentId'] != None:
                            houseId = data_result['rentId']  # 获取房源ID
                            logging.info("房源ID为%s" % houseId)
                            renting_rent['houseId'] = houseId

                        if data_result['jointRentRoomModelList'] != None:  # 获取合租房源信息
                            for house_index, house_value in enumerate(
                                    data_result['jointRentRoomModelList']):  # room_index列表索引,room_value索引值
                                #logging.info(data_result['jointRentRoomModelList'][house_index])
                                house_data = data_result['jointRentRoomModelList'][house_index]  # 获取对应的房间列表信息

                                if house_data['id']!=None:
                                    logging.info("%s 的房屋ID为 %s" % (FangYuan_Name, house_data['id']))
                                    renting_rent['rentId']=house_data['id']

                                if house_data['contractId'] != None:
                                    logging.info("%s 的合同ID为 %s" % (FangYuan_Name, house_data['contractId']))  # 获取房间合同ID
                                    renting_rent['contractId'] = house_data['contractId']

                                if house_data['doorLockInfo'] != None:
                                    house_doorLockInfo_id = house_data['doorLockInfo']['id']  # 获取房间门锁ID
                                    logging.info("%s 锁的ID为%s" % (FangYuan_Name, house_doorLockInfo_id))
                                    renting_rent['house_doorLockInfo_id'] = house_doorLockInfo_id

                                if house_data['lookState'] != None:
                                    house_lookState = house_data['lookState']  # 获取房间带看状态
                                    logging.info("%s 的当前状态为%s" % (FangYuan_Name, house_lookState))
                                    renting_rent['house_lookState'] = house_lookState

                elif FangYuan_Name == None:
                    print('没有找到该房源')
            return joint_rent, renting_rent

    def myHouseList_parameters01(self,Num):
        '''房源信息列表'''
        rentId_list=[]
        result=self.myHouseList1()
        data_row = result['data']['rows']

        for result_data in data_row:
            if result_data['houseStatus']==Num and result_data['id']!=None:#房源状态对比
                logging.info(result_data['rentId'])
                rentId_list.append(result_data['rentId'])
            else:
                print('没有找到')
            return rentId_list

    def queryEstate_parameter(self,xiaoqu_Name='万科翡翠公园'):
        '''获取参数'''
        result=self.queryEstate(xiaoqu_Name=xiaoqu_Name)
        data_result=result['data']['estateList'][0]
        estateId=data_result['estateId']
        estateName=data_result['estateName']
        return estateId,estateName

    def querySubEstates_parameter(self,estateId=83505):
        '''获取参数'''
        result=self.querySubEstates(estateId=estateId)
        data_result=result['data']['subEstateList']
        if data_result[0]!=None:
            subEstateName=data_result[0]['subEstateName']
            subEstateId=data_result[0]['subEstateId']
            return subEstateName,subEstateId
        else:
            print('没有找到该房源')

    def publish_joint_rent_house_parameter(self,estateId=83505,estateName="万科翡翠公园",subEstateId=135608,subEstateName='百业路'):
        '''创建合租房屋'''
        result=self.publish_joint_rent_house(estateId=estateId,estateName=estateName,subEstateId=subEstateId,subEstateName=subEstateName)
        data_result=result['data']
        houseId=data_result['houseId']
        return houseId

    def getJointRentHouseDetail_parameter(self,houseId=''):
        '''获取合租房子详情参数'''

        result=self.getJointRentHouseDetail(houseId=houseId)
        data_result = result['data']
        #print(data_result)
        if data_result['houseModel']!=None and  data_result['houseModel']['rentIds']!=None:
            rentIds=data_result['houseModel']['rentIds']
            logging.info(rentIds)
            return rentIds
        else:
            print('no data')

if __name__ == '__main__':
    A=FuanYuan_Parameters()
    #A.queryEstate_parameter(xiaoqu_Name='汤臣一品')
    #A.querySubEstates_parameter(estateId=7783)
    A.myHouseList_parameters(FangYuan_Name='阳光公寓',Room_Name='房间01')#,Room_Name='房间01'
    #A.getJointRentHouseDetail_parameter(houseId='1571')

