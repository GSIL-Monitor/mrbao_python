# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_operation_flow')
sys.path.append('d:\\Python_study\PYREQUESTS\\aYiLou_fangdong\\yilou_fangdong_business_parameters')
from startEnd import StartEnd
from fuangYuanXinXi import FuanYuan
import logging.config
import unittest
log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

class Test_api_fangyuan__(StartEnd,FuanYuan):
    '''房源'''

    def test_queryEstate01(self):
        '''小区区号success'''
        response = self.queryEstate()
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_queryEstate_01 success')

        except:
            logging.info("test_queryEstate_01发生错误")

    def test_queryEstate02(self):
        '''小区区号特殊字符success'''
        response = self.queryEstate(xiaoqu_Name='111!!!')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_queryEstate_02 success')

        except:
            logging.info("test_queryEstate_02发生错误")
    def test_queryEstate03(self):
        '''小区区号数字success'''
        response = self.queryEstate(xiaoqu_Name='111')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_queryEstate_03 success')

        except:
            logging.info("test_queryEstate_03发生错误")

    def test_queryEstate04(self):
        '''小区区号数字加字母success'''
        response = self.queryEstate(xiaoqu_Name='111www')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_queryEstate_04 success')

        except:
            logging.info("test_queryEstate_04发生错误")
    def test_myHouseContractCount_01(self):
        '''首页待办事项success'''
        response = self.myHouseContractCount()
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_myHouseContractCount_01 success')

        except:
            logging.info("test_myHouseContractCount_01发生错误")

    def test_myHouseList1_01(self):
        '''房源列表success'''
        response = self.myHouseList1()
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_myHouseList1_01 success')

        except:
            logging.info("test_myHouseList1_01 发生错误")

    def test_getJointRentHouseDetail_01(self):
        '''未找到有效房屋'''
        response = self.getJointRentHouseDetail(23123)
        try:

            self.assertEqual(response['message'], "未找到有效房屋")
            logging.info('test_getJointRentHouseDetail_01 success')

        except:
            logging.info("test_getJointRentHouseDetail_01 发生错误")

    def test_getJointRentHouseDetail_02(self):
        '''success'''
        response = self.getJointRentHouseDetail(1404)
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_getJointRentHouseDetail_02 success')

        except:
            logging.info("test_getJointRentHouseDetail_02 发生错误")

    def test_getJointRentHouseDetail_03(self):
        '''未找到有效房屋'''
        response = self.getJointRentHouseDetail('')
        try:

            self.assertEqual(response['message'], "房源ID不能为空")
            logging.info('test_getJointRentHouseDetail_03 success')

        except:
            logging.info("test_getJointRentHouseDetail_03 发生错误")

    def test_getJointRentHouseDetail_04(self):
        '''服务繁忙，请稍后重试'''
        response = self.getJointRentHouseDetail('dfgd')
        try:

            self.assertEqual(response['message'], "服务繁忙，请稍后重试")
            logging.info('test_getJointRentHouseDetail_04 success')

        except:
            logging.info("test_getJointRentHouseDetail_04 发生错误")

    def test_getJointRentHouseDetail_05(self):
        '''特殊字符-服务繁忙，请稍后重试'''
        response = self.getJointRentHouseDetail('====')
        try:

            self.assertEqual(response['message'], "服务繁忙，请稍后重试")
            logging.info('test_getJointRentHouseDetail_05 success')

        except:
            logging.info("test_getJointRentHouseDetail_05 发生错误")
    def test_getJointRentHouseDetail_06(self):
        '''未找到有效房屋'''
        response = self.getJointRentHouseDetail('9999')
        try:

            self.assertEqual(response['message'], "未找到有效房屋")
            logging.info('test_getJointRentHouseDetail_06 success')

        except:
            logging.info("test_getJointRentHouseDetail_06 发生错误")

    def test_listJointRentRoom_01(self):
        '''success'''
        response = self.listJointRentRoom('1404')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_listJointRentRoom_01 success')

        except:
            logging.info("test_listJointRentRoom_01 发生错误")

    def test_listJointRentRoom_02(self):
        '''房源ID不能为空'''
        response = self.listJointRentRoom('')
        try:

            self.assertEqual(response['message'], "房源ID不能为空")
            logging.info('test_listJointRentRoom_01 success')

        except:
            logging.info("test_listJointRentRoom_01 发生错误")
    def test_listJointRentRoom_03(self):
        '''服务繁忙，请稍后重试'''
        response = self.listJointRentRoom('dfgd')
        try:

            self.assertEqual(response['message'], "服务繁忙，请稍后重试")
            logging.info('test_getJointRentHouseDetail_04 success')

        except:
            logging.info("test_getJointRentHouseDetail_04 发生错误")

    def test_listJointRentRoom_04(self):
        '''特殊字符-服务繁忙，请稍后重试'''
        response = self.listJointRentRoom('====')
        try:

            self.assertEqual(response['message'], "服务繁忙，请稍后重试")
            logging.info('test_listJointRentRoom_04 success')

        except:
            logging.info("test_listJointRentRoom_04 发生错误")

    def test_houseDetail_01(self):
        '''success'''
        response = self.houseDetail(2759)
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_houseDetail_01 success')

        except:
            logging.info("test_houseDetail_01 发生错误")


    def test_houseDetail_02(self):
        '''未找到有效房源'''
        response = self.houseDetail(9090)
        try:

            self.assertEqual(response['message'], "未找到有效房源")
            logging.info('test_houseDetail_01 success')

        except:
            logging.info("test_houseDetail_01 发生错误")

    def test_houseDetail_03(self):
        '''服务繁忙，请稍后重试'''
        response = self.houseDetail('ytuyt')
        try:

            self.assertEqual(response['message'], "服务繁忙，请稍后重试")
            logging.info('test_houseDetail_03 success')

        except:
            logging.info("test_houseDetail_03 发生错误")

    def test_houseDetail_04(self):
        '''特殊字符-服务繁忙，请稍后重试'''
        response = self.houseDetail('=-=-=')
        try:

            self.assertEqual(response['message'], "服务繁忙，请稍后重试")
            logging.info('test_houseDetail_04 success')

        except:
            logging.info("test_houseDetail_04 发生错误")

    def test_houseDetail_05(self):
        '''参数id不能为 null'''
        response = self.houseDetail('')
        try:

            self.assertEqual(response['message'], "参数id不能为 null")
            logging.info('test_houseDetail_05 success')

        except:
            logging.info("test_houseDetail_05 发生错误")

    def test_myHouseEstate_01(self):
        '''参数为空'''
        response = self.myHouseEstate('')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_myHouseEstate_01 success')

        except:
            logging.info("test_myHouseEstate_01 发生错误")

    def test_myHouseEstate_02(self):
        '''有效参数'''
        response = self.myHouseEstate(1404)
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_myHouseEstate_02 success')

        except:
            logging.info("test_myHouseEstate_02 发生错误")
if __name__ == '__main__':
    unittest.main()