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

class Yilou_fangdong_Contract(Request_,Read_Yaml_Config):
    '''租约'''

    def click_create_contract(self,rentId):
        '''点击创建合同'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['Click_Create_contract']
        logging.info('url is %s' % send_url)
        send_dict = {'rentId': rentId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def Lessee(self,renterMobile='',renterName='',renterType=1):
        '''输入承租人'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['Lessee']
        logging.info('url is %s' % send_url)
        send_dict = {'renterMobile': renterMobile,'renterName':renterName,'renterType':renterType}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def next_step(self,day=360,mainRenterId='11078',rentId='3721'):
        '''创建合同'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['next_step']
        logging.info('url is %s' % send_url)
        deposit=random.randint(0,10000)
        paymentCycle=random.randint(1,11)
        paymentDate=random.randint(1,14)
        rental=random.randint(0,10000)
        startDate=self.get_time2()[0]
        endDate=self.get_time2(day=day)[5]
        send_dict = {'contractType': 0, 'credentialType': 1, 'monthPay': 1,'type':2,
                     'serviceFeePayer':1,'mainRenterId':mainRenterId,'rentId':rentId,
                    'deposit':deposit,'paymentCycle':paymentCycle,'paymentDate':paymentDate,
                     'rental':rental,'startDate':startDate,'endDate':endDate,'renterCount':3
                }
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def next_step_tongzhuren(self,shareRenterIdListStr=11209,day=360,mainRenterId=11078,rentId=3721):
        '''创建合同并且添加同住租客'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['next_step']
        logging.info('url is %s' % send_url)
        deposit=random.randint(0,10000)
        paymentCycle=random.randint(1,11)
        paymentDate=random.randint(1,14)
        rental=random.randint(0,10000)
        startDate=self.get_time2()[0]
        endDate=self.get_time2(day=day)[5]
        send_dict = {'contractType': 0, 'credentialType': 1, 'monthPay': 1,'type':2,
                     'serviceFeePayer':1,'mainRenterId':mainRenterId,'rentId':rentId,
                    'deposit':deposit,'paymentCycle':paymentCycle,'paymentDate':paymentDate,
                     'rental':rental,'startDate':startDate,'endDate':endDate,'shareRenterIdListStr':shareRenterIdListStr,
                     'renterCount':3
                }
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def create_bill(self,contractId):
        '''创建账单'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['Create_bill']
        logging.info('url is %s' % send_url)
        send_dict = {'contractId': contractId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def setBillPaid(self,contractId):
        '''生成账单'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['setBillPaid']
        logging.info('url is %s' % send_url)
        send_dict = {'contractId': contractId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getReleaseContractDetail(self,contractId):
        '''获取合同具体信息'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['getReleaseContractDetail']
        logging.info('url is %s' % send_url)
        send_dict = {'contractId': contractId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)

        return response

    def createReleaseContract(self,contractId,defaultFee,deposit,livingFee,otherFee,rental):
        '''选择快速退房结账后点击确认'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['createReleaseContract']
        logging.info('url is %s' % send_url)
        send_dict = {'contractId': contractId,'defaultFee':defaultFee,'deposit':deposit,'livingFee':livingFee,'otherFee':otherFee,'rental':rental}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getAllBillLivingTypes(self):
        '''获取生活费用账单类型'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['getAllBillLivingTypes']
        logging.info('url is %s' % send_url)
        send_dict = {'': ''}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def addRentBill(self,billItems,contractId,payDate):
        '''增加生活费'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['addRentBill']
        logging.info('url is %s' % send_url)
        send_dict = {'billItems': billItems,'contractId':contractId,'payDate':payDate}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def listRentBill4Landlord(self,contractId,payStatus=0,type=0,pageNo=1,pageSize=20):
        '''获取账单列表'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['listRentBill4Landlord']
        logging.info('url is %s' % send_url)
        send_dict = {'contractId': contractId,'payStatus':payStatus,'type':type,'pageNo':pageNo,'pageSize':pageSize}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

if __name__ == '__main__':
    A=Yilou_fangdong_Contract()
    #A.click_create_contract(3721)
    #A.Lessee(renterMobile='17400330093',renterName='565656')
    #A.next_step(day=360)
    #A.create_bill(3605)
    #A.setBillPaid(3605)
    #A.getReleaseContractDetail(3730)
    A.getAllBillLivingTypes()
    A.listRentBill4Landlord(3967)