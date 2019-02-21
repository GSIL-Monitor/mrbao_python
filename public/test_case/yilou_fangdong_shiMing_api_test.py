# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_operation_flow')
sys.path.append('d:\\Python_study\PYREQUESTS\\aYiLou_fangdong\\yilou_fangdong_business_parameters')
from startEnd import StartEnd
from yilou_fangdong_shiMing import ShiMing
import logging.config
import unittest
log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

class Test_api_shiming(StartEnd,ShiMing):
    """
    实名信息已存在
    """
    def test_realname_register_01(self):
        '''姓名不能为空'''
        response = self.realname_register('', '')
        try:

            self.assertEqual(response['message'], "姓名不能为空")
            logging.info('test_realname_register_01 success')

        except:
            logging.info("test_realname_register_01发生错误")

    def test_realname_register_02(self):
        '''身份证格式不合法'''

        response=self.realname_register('sdf','sf')
        try:
            self.assertEqual(response['message'], "身份证格式不合法")
            logging.info('test_realname_register_02 success')

        except:
            logging.info("test_realname_register_02发生错误")

    def test_realname_register_03(self):
        '''身份证不能为空'''

        response=self.realname_register('sdf','')
        try:
            self.assertEqual(response['message'], "身份证不能为空")
            logging.info('test_realname_register_03 success')
        except:
            logging.info("test_realname_register_03发生错误")

    def test_realname_register_04(self):
        '''姓名不能为空'''

        response=self.realname_register('','dsf')
        try:
            self.assertEqual(response['message'], "姓名不能为空")
            logging.info('test_realname_register_04 success')
        except:
            logging.info("test_realname_register_04发生错误")

    def test_realname_register_05(self):
        '''参数为空'''

        response=self.realname_register('','')
        try:
            self.assertEqual(response['message'], "姓名不能为空")
            logging.info('test_realname_register_05 success')
        except:
            logging.info("test_realname_register_05发生错误")

    def test_realname_register_06(self):
        '''身份证为空'''

        response=self.realname_register('大放送','')
        try:
            self.assertEqual(response['message'], "身份证不能为空")
            logging.info('test_realname_register_06 success')
        except:
            logging.info("test_realname_register_06发生错误")

    def test_rbindIdentity_07(self):
        '''姓名身份证匹配失败'''

        response=self.bindIdentity('大放送',320882199012243215)
        try:
            self.assertEqual(response['message'], "姓名身份证匹配失败")
            logging.info('test_realname_register_07 success')
        except:
            logging.info("test_realname_register_07发生错误")

    def test_rbindIdentity_08(self):
        '''参数 name 不能为空'''

        response=self.bindIdentity('',320882199012243215)
        try:
            self.assertEqual(response['message'], "参数 name 不能为空")
            logging.info('test_realname_register_08 success')
        except:
            logging.info("test_realname_register_08发生错误")

    def test_rbindIdentity_09(self):
        '''idCard为空'''

        response=self.bindIdentity('松岛枫','')
        try:
            self.assertEqual(response['message'], "参数 idCard 不能为空")
            logging.info('test_realname_register_09 success')
        except:
            logging.info("test_realname_register_09发生错误")

    def test_getSupportBankList_10(self):
        '''获取支持银行列表'''

        response=self.getSupportBankList()
        try:
            self.assertEqual(response['message'], "success")
            logging.info('test_realname_register_10 success')
        except:
            logging.info("test_realname_register_10发生错误")

    def test_getCardBin_11(self):
        '''获取支持银行列表'''

        response=self.getCardBin("4392268328103388")
        try:
            self.assertEqual(response['message'], "success")
            logging.info('test_realname_register_11 success')
        except:
            logging.info("test_realname_register_11发生错误")
if __name__ == '__main__':
    unittest.main()