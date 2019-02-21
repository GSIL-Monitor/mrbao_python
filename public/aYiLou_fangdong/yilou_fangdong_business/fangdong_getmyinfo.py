# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')

import logging.config
from read_Yaml_Config import Read_Yaml_Config
from request_bane import Request_
import time
import random
import functools

con_log='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

self_Request=Request_()
self_Read_Yaml_Config=Read_Yaml_Config()

def zhuangshi_canshu(canshu):#装饰函数
    BD_zhuli = [1,2,3,12,18,21,23,26]
    guanjia = [1,2, 3, 4, 6, 7, 13, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 39, 40, 41]
    def zhuangshi_getMyInfo(func):
        '''获取我的页面数据'''
        @functools.wraps(func)
        def wrapper(*args, **kw):
            startTime = time.time()
            response = func(*args, **kw)
            endTime = time.time()
            yingXingTime = (endTime - startTime)
            logger.info('%s 的运行时间为%s' % (func.__name__, yingXingTime))
            data_response = response['data']
            if data_response==None:
                return
            permissions = data_response['permissions']
            for i in range(len(permissions)-1):
                for j in range(len(permissions)-1):
                    if permissions[j]>permissions[j+1]:
                        permissions[j],permissions[j+1]=permissions[j+1],permissions[j]
            if permissions==BD_zhuli and permissions !=None:
                logging.info("BD的权限正确")
                return
            if permissions==guanjia and permissions!=None:
                logging.info("管家的权限正确")
                return
        return wrapper
    return zhuangshi_getMyInfo

def getMyInfo():
    '''我的页面'''
    send_url = self_Read_Yaml_Config.get_peizhi_(name='wode', yaml_ming='yilou_fangdong.yaml')
    send_url = send_url['getMyInfo']
    logging.info('url is %s' % send_url)
    send_dict = {"":"" }
    response = self_Request.request_post(base_url=send_url, dict_data=send_dict)
    return response

def editUserSetting(allowBdAssistant=1):
    '''设置助理线下收款权限&BD助理设置'''
    send_url = self_Read_Yaml_Config.get_peizhi_(name='wode', yaml_ming='yilou_fangdong.yaml')
    send_url = send_url['editUserSetting']
    logging.info('url is %s' % send_url)
    send_dict = {"allowBdAssistant": allowBdAssistant}
    response = self_Request.request_post(base_url=send_url, dict_data=send_dict)
    return response

@zhuangshi_canshu('BD_zhuli')
def switch_account(accountId):
    '''点击切换账号'''
    send_url = self_Read_Yaml_Config.get_peizhi_(name='wode', yaml_ming='yilou_fangdong.yaml')
    send_url = send_url['switch_account']
    logging.info('url is %s' % send_url)
    send_dict = {"accountId": accountId}
    response = self_Request.request_post(base_url=send_url, dict_data=send_dict)
    return response

def zhuangshi_canshu(mobile):
    def zhuangshi_getIdentityList(func):
        '''装饰getIdentityList'''
        def wrapper(*args, **kw):
            startTime = time.time()
            response = func(*args, **kw)
            endTime = time.time()
            yingXingTime = (endTime - startTime)
            logger.info('%s 的运行时间为%s' % (func.__name__, yingXingTime))
            data_response = response['data']
            currentIdentity = data_response['currentIdentity']#测试房东信息
            userIdentityList = data_response['userIdentityList']#BD助理房东信息
            if mobile!=None:
                for key, value in enumerate(userIdentityList):
                    if mobile in value['userMobile']:
                        data_result = userIdentityList[key]
                        if data_result['subAccountId'] == None:
                            return
                        if data_result['subAccountId'] != None:
                            subAccountId = data_result['subAccountId']
                            return subAccountId  # 返回房东id
                if mobile==currentIdentity['userMobile']:
                    return currentIdentity['subAccountId']#返回测试房东id
        return wrapper
    return zhuangshi_getIdentityList

@zhuangshi_canshu(mobile='17400050001')#18217111076
def getIdentityList():
    '''获取身份列表'''
    send_url = self_Read_Yaml_Config.get_peizhi_(name='wode', yaml_ming='yilou_fangdong.yaml')
    send_url = send_url['getIdentityList']
    logging.info('url is %s' % send_url)
    send_dict = {"": ""}
    response = self_Request.request_post(base_url=send_url, dict_data=send_dict)
    return response

if __name__ == '__main__':
    #getMyInfo()
    #editUserSetting(allowBdAssistant=1)
    #switch_account(1)
    getIdentityList()
    print(getIdentityList())


