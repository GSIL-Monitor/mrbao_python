# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong_businessa\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong_businessa\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong_businessa\yilou_fangdong_business')
import logging.config
from yilou_zuke_read_yaml import Read_Yaml_Config
from data_shuju import DB
from yilou_zuke_request import Request_

con_log='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

class Login(Request_,Read_Yaml_Config,DB):
    '''
    zuke登录
    '''
    def login(self,mobile):
        '''
        denglu
        :param mobile: 
        :return: 
        '''
        send_url=self.get_peizhi_('Login',yaml_ming='yilou_zufang.yaml')
        send_url=send_url['send_verifcode']#获取发送验证码url
        logging.info('url is %s'%send_url)
        dict_send={'mobile':mobile}
        response=self.request_post(send_url,dict_send)#发送验证码
        logging.info(response)

        yanzhengma=self.get_YanZhengMa(mobile)#获取验证码
        dict_login={'mobile': mobile, 'verifyCode':yanzhengma}
        login_url=self.get_peizhi_('Login',yaml_ming='yilou_zufang.yaml')
        login_url=login_url['login_in']
        logging.info(login_url)
        response=self.request_post(login_url,dict_login)#点击登录
        data_content=response
        logging.info(data_content)

        ticket_token=data_content['data']['ticket']#获取ticket
        logging.info('token is %s'%ticket_token)

        self.write_yaml(yaml_name='u_token',yaml_zhi=ticket_token,yaml_ming='zuke_token.yaml')
        logging.info('----login end----')
        return data_content,ticket_token

    def send_verifcode(self,mobile):
        '''发送验证码'''
        send_url=self.get_peizhi_('Login',yaml_ming='yilou_zufang.yaml')
        send_url=send_url['send_verifcode']
        logging.info('url is %s' % send_url)
        dict_send = {'mobile': mobile}
        response = self.request_post(send_url, dict_send)  # 发送验证码
        logging.info(response)
        return response

    def shuru_yanzhengma(self,mobile,Code):
        '''输入验证码'''
        dict_send = {'mobile': mobile, 'verifyCode': Code}
        send_url=self.get_peizhi_('Login',yaml_ming='yilou_zufang.yaml')
        send_url=send_url['login_in']
        logging.info('url is %s' % send_url)
        response = self.request_post(send_url, dict_send)  # 发送验证码
        logging.info(response)
        return response

if __name__ == '__main__':
    A=Login()
    A.login('17400220022')
    #A.send_verifcode('18621509417')
    #A.shuru_yanzhengma('大幅度给对方','')
