# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_operation_flow')
sys.path.append('d:\\Python_study\PYREQUESTS\\aYiLou_fangdong\\yilou_fangdong_business_parameters')
from startEnd import StartEnd
from fangdongduan_login__ import Login
import logging.config
import unittest
log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

class Test_api_login(StartEnd,Login):
    '''登录测试'''

    def test_login_in_01(self):
        '''前期采用邀请制，如需使用请联系客服：18616390173(同微信号)'''
        response = self.send_verifcode('18621515422')
        try:
            self.assertEqual(response['message'], "前期采用邀请制，如需使用请联系客服：18616390173(同微信号)")
            logging.info('realname_register success')
        except:
            logging.info("test_login_in_01发生错误")

    def test_login_in_02(self):
        '''发送成功'''
        response = self.send_verifcode('18621509417')
        try:
            if response['message']=='发送成功':
                self.assertEqual(response['message'], "发送成功")
                logging.info('test_login_in_02 success')
            elif response['message']=='同一号码一分钟只能发一次':
                self.assertEqual(response['message'], "同一号码一分钟只能发一次")
                logging.info('test_login_in_02 success')
        except:
            logging.info("test_login_in_02发生错误")

    def test_login_in_03(self):
        '''验证码不正确,数字'''
        response = self.shuru_yanzhengma('18621515422','12dfd')
        try:
            self.assertEqual(response['message'], "验证码不正确")
            logging.info('realname_register success')
        except:
            logging.info("test_login_in_03发生错误")

    def test_login_in_04(self):
        '''验证码不正确,数字与字符'''
        response = self.shuru_yanzhengma('18621515422','12wer')
        try:
            self.assertEqual(response['message'], "验证码不正确")
            logging.info('realname_register success')
        except:
            logging.info("test_login_in_03发生错误")

    def test_login_in_05(self):
        '''验证码不正确,字符'''
        response = self.shuru_yanzhengma('18621515422','wer')
        try:
            self.assertEqual(response['message'], "验证码不正确")
            logging.info('realname_register success')
        except:
            logging.info("test_login_in_03发生错误")

    def test_login_in_06(self):
        '''短信验证码不能为空'''
        response = self.shuru_yanzhengma('18621515422','')
        try:
            self.assertEqual(response['message'], "短信验证码不能为空")
            logging.info('realname_register success')
        except:
            logging.info("test_login_in_03发生错误")

    def test_login_in_07(self):
        '''短信验证码不能为空'''
        response = self.shuru_yanzhengma('','')
        try:
            self.assertEqual(response['message'], "手机不能为空")
            logging.info('realname_register success')
        except:
            logging.info("test_login_in_03发生错误")

    def test_login_in_08(self):
        '''短信验证码不能为空'''
        response = self.shuru_yanzhengma('18621515422','')
        try:
            self.assertEqual(response['message'], "手机不能为空")
            logging.info('realname_register success')
        except:
            logging.info("test_login_in_03发生错误")

    def test_login_in_09(self):
        '''登录成功'''
        response = self.login('18621512473')
        try:
            self.assertEqual(response['message'], "手机不能为空")
            logging.info('realname_register success')
        except:
            logging.info("test_login_in_03发生错误")
if __name__ == '__main__':
    unittest.main()