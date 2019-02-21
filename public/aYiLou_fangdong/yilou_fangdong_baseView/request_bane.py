#coding: UTF-8
import yaml
import json
import requests
import logging.config
from CanShuPaiXu1 import Paixu
from read_Yaml_Config import Read_Yaml_Config

import sys

sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')

con_log=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()
data_peizhi=Read_Yaml_Config()
data_header=data_peizhi.get_peizhi('header',yaml_ming='yilou_fangdong.yaml')
data_login=data_peizhi.get_peizhi('mensuo',yaml_ming='yilou_fangdong.yaml')
token=data_peizhi.get_peizhi('u_token',yaml_ming='xiaoxiangx_dapaijiangjia.yaml')

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
            response=requests.get(base_url,headers=header,params=json_dict)
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
        try:
            #logging.info(header)
            response = requests.post(base_url, headers=header, data=json_dict)
            if response.status_code==404 or response.status_code==502:
                logging.info('Services is faile')
                return
            if response.json()['message']=="服务繁忙，请稍后重试":
                logging.info('Services are being issued')
                return
            if response.json()['message']=='签约后才能使用App，请联系您的BD协助操作':
                logging.info("签约后才能使用App，请联系您的BD协助操作")
                return
            if response.json()['message']=='前期采用邀请制，如需使用请联系客服：18616390173(同微信号)':
                logging.info('前期采用邀请制，如需使用请联系客服：18616390173(同微信号)')
                return
            if response.json()['message']=='同一号码一小时只能发五次验证码':
                logging.info('同一号码一小时只能发五次验证码')
                return
            logging.info(response.json())
        except  BaseException as e:
            logging.info(e)
        else:
            return response.json()
if __name__ == '__main__':
    #A=requests
    A=Paixu()
    B=Request_()
    effectiveTime = A.get_time2()[1]
    expirationTime = A.get_time2()[2]
    #print(data_login['send_verifcode'])
    send_dict = {'doorId': 20835, 'effectiveTime': effectiveTime, 'expirationTime': expirationTime, 'mobile': '18621512473','name': 'mrbao', 'times': 1}
    response=B.request_post(data_login['addDoorGuestPwd'],send_dict)
    print(response)
