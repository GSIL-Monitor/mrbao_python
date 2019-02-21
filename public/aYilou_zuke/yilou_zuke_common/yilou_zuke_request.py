
import yaml
import json
import requests
import logging.config
from yilou_zuke_canshu import Paixu
from yilou_zuke_read_yaml import Read_Yaml_Config

import sys

sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong_businessa\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong_businessa\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong_businessa\yilou_fangdong_business')

con_log=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()


data_peizhi=Read_Yaml_Config()
token=data_peizhi.get_peizhi('u_token',yaml_ming='zuke_token.yaml')

class Request_(Paixu):
    '''
    request封装
    '''
    def __init__(self):
        self.canshu = Paixu()
        self.count=0
        #self.request=requests
    def request_get(self,base_url,dict_data):
        '''
        get请求
        :param base_url: 
        :param dict_data: 
        :return: 
        '''
        json_dict=json.dumps(dict_data, ensure_ascii=False)
        header=self.get_canshu(dict_data)
        header=header[1]
        #print(header)
        #print(base_url)
        try:
            response=requests.post(base_url,headers=header,params=json_dict)
            logging.info(response.json())
        except:
            logging.info('resquest is False')
        else:
            return response.json()
    def request_post(self,base_url,dict_data):
        '''
        post请求
        :param base_url: 
        :param dict_data: 
        :return: 
        '''
        json_dict=json.dumps(dict_data, ensure_ascii=True)
        header=self.get_canshu(dict_data)
        header=header[1]
        if token!=None:
            header['u_ticket']=token
            #logging.info(token)
        else:
            logging.info('u_token is Null')

        #print(header)
        #print(base_url)
        try:
            logging.info(header)
            response=requests.post(base_url,headers=header,data=json_dict)
            logging.info(response.json())

            if response.json()['message']=="服务繁忙，请稍后重试":
                logging.info('Services are being issued')
        except:
            logging.info('resquest is False')
        else:
            return response.json()
if __name__ == '__main__':
    #A=requests
    A=Paixu()
    B=Request_()
    effectiveTime = A.get_time2()[1]
    expirationTime = A.get_time2()[2]
    #print(data_login['send_verifcode'])
