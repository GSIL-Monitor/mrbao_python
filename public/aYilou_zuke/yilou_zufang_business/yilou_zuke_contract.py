import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_aYiLou_zuke\yilou_zuke_common')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_zuke\yilou_zuke_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_zuke\yilou_zuke_business')

import logging.config
con_log='D:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

from yilou_zuke_request import Request_
from yilou_zuke_read_yaml import Read_Yaml_Config

class Yilou_Zuke_Contract(Request_,Read_Yaml_Config):
    '''租客端合同'''

    def renter_confirm_contract(self,contractId):
        '''确认合同'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['renter_confirm_contract']
        logging.info('url is %s' % send_url)
        send_dict = {'contractId':contractId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def econtract_info(self,contractId):
        '''获取合同信息'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['econtract_info']
        logging.info('url is %s' % send_url)
        send_dict = {'contractId':contractId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getRentBillList(self,contractId):
        '''获取合同信息'''
        send_url = self.get_peizhi_(name='contract', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['getRentBillList']
        logging.info('url is %s' % send_url)
        send_dict = {'contractId':contractId}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response

    def getAccountInfo(self):
        '''获取租客信息'''
        send_url = self.get_peizhi_(name='login_interface', yaml_ming='yilou_zufang.yaml')
        send_url = send_url['getAccountInfo']
        logging.info('url is %s' % send_url)
        send_dict = {'': ''}
        response = self.request_post(base_url=send_url, dict_data=send_dict)
        return response


if __name__ == '__main__':
    A=Yilou_Zuke_Contract()
    #A.econtract_info(3946)
    A.getAccountInfo()