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

log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

class ShiMing(Request_,Read_Yaml_Config,DB):
    '''
    '''
    def bindIdentity(self,realName,idCard):
        '''
        提交实名认证
        :return: 
        '''
        send_url=self.get_peizhi_(name='shiming',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['bindIdentity']
        logging.info('url is %s' % send_url)

        send_dict={'realName':realName,'idCard':idCard}

        response=self.request_post(base_url=send_url,dict_data=send_dict)
        #logging.info(response)
        return response
    def getSupportBankList(self):
        '''
         #86、获取支持银行列表
        :return: 
        '''
        send_url=self.get_peizhi_(name='shiming',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['getSupportBankList']
        logging.info('url is %s' % send_url)

        send_dict={'':''}

        response=self.request_post(base_url=send_url,dict_data=send_dict)
        #logging.info(response)
        return response

    def getCardBin(self,bankCardNo):
        '''
        #87、获取银行卡开户行
        :return: 
        '''
        send_url=self.get_peizhi_(name='shiming',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['getCardBin']
        logging.info('url is %s' % send_url)

        send_dict={"bankCardNo": bankCardNo}

        response=self.request_post(base_url=send_url,dict_data=send_dict)
        #logging.info(response)
        return response

    def realname_register(self,name,idCard):
        '''
        #3实名登记
        :return: 
        '''
        send_url=self.get_peizhi_(name='shiming',yaml_ming='yilou_fangdong.yaml')
        send_url=send_url['realname_register']
        logging.info('url is %s' % send_url)

        send_dict={ "realName": name,"idCard": idCard}

        response=self.request_post(base_url=send_url,dict_data=send_dict)
        #logging.info(response)
        return response

if __name__ == '__main__':
    A=ShiMing()
    A.bindIdentity('12321',1312321321)
    A.getSupportBankList()
    A.getCardBin(121321321)
    A.realname_register('22','33')
