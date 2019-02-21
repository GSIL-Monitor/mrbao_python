# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_operation_flow')
sys.path.append('d:\\Python_study\PYREQUESTS\\aYiLou_fangdong\\yilou_fangdong_business_parameters')
from startEnd import StartEnd
from Business_process import Create_house
import logging.config
import unittest
log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

class Test_fangyuan_business(StartEnd,Create_house):
    '''房源业务流程'''

    def test_rented_house(self):
        '''创建合租房屋success'''
        response = self.rented_house(estateName='中粮海景壹号')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_rented_house_01 success')

        except:
            logging.info("test_rented_house_01发生错误")

    def test_rented_house_create_apply(self):
        '''创建房源并且填写房间信息，且申请装锁成功'''
        response = self.rented_house_create_apply(estateName='中粮海景壹号')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_rented_house_create_apply success')

        except:
            logging.info("test_rented_house_create_apply_01发生错误")

    def test_rented_house_delete(self):
        '''创建房源并且删除房屋'''
        response = self.rented_house_delete(estateName='中粮海景壹号')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_rented_house_delete success')

        except:
            logging.info("test_rented_house_delete_01发生错误")

    def test_rented_house_create(self):
        '''创建房源并且填写房间信息，且申请装锁成功并且删除'''
        response = self.rented_house_create(estateName='中粮海景壹号')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_rented_house_create success')

        except:
            logging.info("test_rented_house_create_01发生错误")

    def test_whole_rent(self):
        '''创建整租房屋'''
        response = self.whole_rent(estateName='中粮海景壹号')
        try:

            self.assertEqual(response['message'], "success")
            logging.info('test_rented_house_create success')

        except:
            logging.info("test_rented_house_create_01发生错误")

if __name__ == '__main__':
    unittest.main()
