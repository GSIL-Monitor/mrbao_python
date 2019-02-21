# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')

import logging.config
from fangdongduan_H5 import Fangdongduan_H5
con_log='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()
Fangdongduan_H5=Fangdongduan_H5()

def getDoorBaseInfo_parameters(doorId):
    '''门锁基本信息'''
    getDoorBaseInfo = {}
    result = Fangdongduan_H5.getDoorBaseInfo(doorId)
    result_data = result['data']
    doorStatus = result_data['doorStatus']  # 门锁状态0:无效 1:有效 2:冻结
    getDoorBaseInfo['doorStatus'] = doorStatus
    validUserCount = result_data['validUserCount']  # validUserCount有效用户数量
    getDoorBaseInfo['validUserCount'] = validUserCount
    freezeUserCount = result_data['freezeUserCount']  # freezeUserCount冻结用户数量
    getDoorBaseInfo['freezeUserCount'] = freezeUserCount
    openTimes = result_data['openTimes']  # openTimes七天开门次数
    getDoorBaseInfo['openTimes'] = openTimes
    return getDoorBaseInfo

def listUser_parameters(doorId,mobile='17400220022'):
    '''获取门锁所有有权限用户列表'''
    listUser={}
    result = Fangdongduan_H5.listUser(doorId)
    result_data = result['data']['doorUserList']
    for index,value in enumerate(result_data):
        if mobile in value['mobile']:
            data_shuju=result_data[index]
            listUser['overdueFreeze']=data_shuju['overdueFreeze']#获取逾期冻结：0、否；1、是
            listUser['landlordFreeze']=data_shuju['landlordFreeze']#房东冻结：0、否；1、是
            listUser['userId']=data_shuju['userId']#用户ID
            listUser['state']=data_shuju['state']
            print(listUser)
    return listUser
if __name__ == '__main__':

    print(getDoorBaseInfo_parameters(31070))
    #listUser_parameters(31069,mobile='17400880088')
    #listUser_parameters(31071,mobile='17400880088')
    #listUser_parameters(31069, mobile='17400220022')
    listUser_parameters(31070,mobile='17400880088')
