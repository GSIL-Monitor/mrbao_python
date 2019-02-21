import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_aYiLou_zuke\yilou_zuke_common')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_zuke\yilou_zuke_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_zuke\yilou_zuke_business')

import logging.config
con_log='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()
from yilou_zuke_request import Request_
from yilou_zuke_read_yaml import Read_Yaml_Config
from yilou_zuke_canshu import Paixu

class Yilou_zuke_mensuo(Request_,Read_Yaml_Config,Paixu):
    '''租客门锁'''

    def addSafeCode(self,doorId,pwd):
        '''设置安全码'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['addSafeCode']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId,'pwd':pwd}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def checkPwdDuplicate(self,doorId,pwd):
        '''校验安全码的唯一性'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['checkPwdDuplicate']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId, 'pwd': pwd}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def activateSafeCode(self,doorId):
        '''激活安全码'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['activateSafeCode']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def safeCodeStatusResult(self):
        '''轮询获取门锁安全码状态'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['safeCodeStatusResult']
        logging.info('url is %s' % send_url)
        send_dict = {'': ''}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def addPwdAddOrActivateSafeCode(self,doorId):
        '''引导设置小门密码、设置大门安全码、激活大门安全码'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['addPwdAddOrActivateSafeCode']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def updatePassword(self,doorId,pwd):
        '''房间增加长期密码'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['updatePassword']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId,'pwd':pwd,'type':2}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getLockBaseInfo(self,doorId,authUserId=''):
        '''获取门锁基本信息'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['getLockBaseInfo']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId, 'authUserId':authUserId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getOpenRecord(self,doorId,authUserId=''):
        '''获取门锁开门记录'''

        startTime=self.get_time2(day=-3)[5]
        endTime=self.get_time2()[0]
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['getOpenRecord']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId, 'authUserId': authUserId,'startTime':startTime,'endTime':endTime}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getLocksByHouseId(self,houseId):
        '''获取房源门锁列表'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['getLocksByHouseId']
        logging.info('url is %s' % send_url)
        send_dict = {'houseId': houseId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getNewLockPWD(self,doorId):
        '''获取新密码(旧的临时密码)'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['getNewLockPWD']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def addDoorPWD4Temp(self,doorId):
        '''创建门锁临时密码(v2.6修改)doorId（蓝牙开门时获取紧急密码'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['addDoorPWD4Temp']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def applyUrgentTempPWD(self,doorId):
        '''申请紧急临时密码(v1.1新增)doorId'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['applyUrgentTempPWD']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def setOpenNotificationConfig(self,doorId,status=0):
        '''修改开门通知设置(智能门锁) doorId   授权人ID  userId   status  0：打开 1：关闭'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['setOpenNotificationConfig']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId,'status':status}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getOpenNotificationConfig(self,doorId):
        '''查询开门通知配置(智能门锁)  doorId'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['getOpenNotificationConfig']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def deletePassword(self,doorId,doorType=1):
        '''删除门锁密码(智能门锁'''
        send_url = self.get_peizhi_(name='mensuo', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['deletePassword']
        logging.info('url is %s' % send_url)
        send_dict = {'doorId': doorId,'doorType':doorType}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response


if __name__ == '__main__':
    A=Yilou_zuke_mensuo()
    #A.addSafeCode(doorId='',pwd='')
    #A.getLocksByHouseId(1871)
    #A.getLockBaseInfo(21986)
    #A.getOpenRecord(21986)
    #A.getNewLockPWD(21986)
    #A.addDoorPWD4Temp(21986)
    #A.applyUrgentTempPWD(21986)
    #A.getOpenNotificationConfig(21986)
    #A.deletePassword(21986)
    A.checkPwdDuplicate(doorId='9990',pwd='123456')