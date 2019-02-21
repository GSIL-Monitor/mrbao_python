# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_operation_flow')
sys.path.append('d:\\Python_study\PYREQUESTS\\aYiLou_fangdong\\yilou_fangdong_business_parameters')
from startEnd import StartEnd
from yilou_zuke_mensuo import Yilou_zuke_mensuo
import logging.config
import unittest
log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

class Test_zuke_mensuo(StartEnd,Yilou_zuke_mensuo):
    '''租客门锁'''
    def test_addSafeCode01(self,doorId,pwd):
        '''doorId为空'''
        response = self.addSafeCode(doorId='',pwd='')
        try:

            self.addSafeCode(response['message'], "doorId(门锁id不能为空)")
            logging.info('test_addSafeCode_01 success')

        except:
            logging.info("test_addSafeCode_01发生错误")

    def test_addSafeCode02(self, doorId, pwd):
        '''没有履约中的合同'''
        response = self.addSafeCode(doorId='21986', pwd='')
        try:

            self.addSafeCode(response['message'], "合租，该租客没有履约中签约合同，也没有履约中的同住租客合同")
            logging.info('test_addSafeCode_02 success')

        except:
            logging.info("test_addSafeCode_02发生错误")

    def test_addSafeCode03(self, doorId, pwd):
        '''门锁不存在'''
        response = self.addSafeCode(doorId='2198', pwd='')
        try:

            self.addSafeCode(response['message'], "门锁不存在")
            logging.info('test_addSafeCode_03 success')

        except:
            logging.info("test_addSafeCode_03发生错误")

    def test_addSafeCode04(self, doorId, pwd):
        '''doorId为特殊字符'''
        response = self.addSafeCode(doorId='#@###', pwd='')
        try:

            self.addSafeCode(response['message'], "服务繁忙，请稍后重试")
            logging.info('test_addSafeCode_04 success')

        except:
            logging.info("test_addSafeCode_04发生错误")

    def test_addSafeCode05(self, doorId, pwd):
        '''密码为空'''
        response = self.addSafeCode(doorId='21986', pwd='')
        try:

            self.addSafeCode(response['message'], "密码不能为空")
            logging.info('test_addSafeCode_05 success')

        except:
            logging.info("test_addSafeCode_05发生错误")

    def test_addSafeCode06(self, doorId, pwd):
        '''密码只输入一个数字'''
        response = self.addSafeCode(doorId='21986', pwd='1')
        try:

            self.addSafeCode(response['message'], "http result is null")
            logging.info('test_addSafeCode_06 success')

        except:
            logging.info("test_addSafeCode_06发生错误")

    def test_addSafeCode07(self, doorId, pwd):
        '''密码输入特殊字符@'''
        response = self.addSafeCode(doorId='21986', pwd='@')
        try:

            self.addSafeCode(response['message'], "http result is null")
            logging.info('test_addSafeCode_07 success')

        except:
            logging.info("test_addSafeCode_07发生错误")

    def test_addSafeCode08(self, doorId, pwd):
        '''密码输入7位'''
        response = self.addSafeCode(doorId='21986', pwd='2342343')
        try:

            self.addSafeCode(response['message'], "http result is null")
            logging.info('test_addSafeCode_08 success')

        except:
            logging.info("test_addSafeCode_08发生错误")

    def test_addSafeCode09(self, doorId, pwd):
        '''密码输入中文'''
        response = self.addSafeCode(doorId='21986', pwd='安全码')
        try:

            self.addSafeCode(response['message'], "http result is null")
            logging.info('test_addSafeCode_09 success')

        except:
            logging.info("test_addSafeCode_09发生错误")

    def test_addSafeCode10(self, doorId, pwd):
        '''密码输入中文'''
        response = self.addSafeCode(doorId='21986', pwd='123456')
        try:

            self.addSafeCode(response['message'], "成功添加安全码")
            logging.info('test_addSafeCode_10 success')

        except:
            logging.info("test_addSafeCode_10发生错误")


    def test_addSafeCode11(self, doorId, pwd):
        '''密码下发中，请稍后重试'''
        response = self.addSafeCode(doorId='21986', pwd='123456')
        try:

            self.addSafeCode(response['message'], "密码下发中，请稍后重试")
            logging.info('test_addSafeCode_11 success')

        except:
            logging.info("test_addSafeCode_11发生错误")

    def test_checkPwdDuplicate(self, doorId, pwd):
        '''安全码校验成功'''
        response = self.checkPwdDuplicate(doorId='21986', pwd='123456')
        try:

            self.checkPwdDuplicate(response['message'], "成功")
            logging.info('test_checkPwdDuplicate_01 success')

        except:
            logging.info("test_checkPwdDuplicate_01发生错误")


if __name__ == '__main__':
    unittest.main()