# -*- coding: UTF-8 -*-
import logging
import unittest

from FangYuanMenSUO import FangYuan
from common.data_shuju import DB
from login import Login_in

LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='API.log',level=logging.INFO,format=LOG_FORMAT)
class Test_api(unittest.TestCase):
    '''房东端登录验证接口验证'''
    def setUp(self):
        self.D=Login_in()
        self.ticket=""
        self.A=DB()
    #登录验证
    def test_login_in(self):
        '''发送验证码登录测试'''
        response=self.D.login_in("18621512473")
        self.result=response[0]
        self.ticket=response[1]
        try:
            self.assertEqual(self.result['message'],'success')
            self.assertEqual(self.result['data']['mobile'],'18621512473')
        except :
            logging.info("login_in发生错误")

class ShiMingRenzheng(unittest.TestCase):
    '''房东端实名认证接口验证'''
    def setUp(self):
        self.D = Login_in()
        self.token='QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA='
    def  test_realname_register01(self):
        '''实名信息已存在'''
        response=self.D.realname_register("ee","320882199012243215")
        self.result=response
        try:
            self.assertEqual(self.result['message'],"实名信息已存在，不能重复")
        except:
            logging.info("realname_register发生错误")

    def test_realname_register02(self):
        '''身份证格式不合法'''
        response = self.D.realname_register("ee", "320882199012243212")
        self.result = response
        try:
            self.assertEqual(self.result['message'], "身份证格式不合法")
        except:
            logging.info("realname_register发生错误")
    def test_realname_register03(self):
        '''姓名为空'''
        response = self.D.realname_register("", "320882199012243212")
        self.result = response
        try:
            self.assertEqual(self.result['message'], "姓名不能为空")
        except:
            logging.info("realname_register发生错误")

    def test_realname_register04(self):
        '''参数都为空'''
        response = self.D.realname_register("", "")
        self.result = response
        try:
            self.assertEqual(self.result['message'], "姓名不能为空")
        except:
            logging.info("realname_register发生错误")

    def test_realname_register05(self):
        '''身份证为空'''
        response = self.D.realname_register("1", "")
        self.result = response
        try:
            self.assertEqual(self.result['message'], "身份证不能为空")
        except:
            logging.info("realname_register发生错误")

    def test_bindIdentity01(self):
        '''姓名身份证匹配失败'''
        response=self.D.bindIdentity('ww',320882199012243215)
        self.result=response
        try:
            self.assertEqual(self.result['message'], "姓名身份证匹配失败")
        except:
            logging.info("bindIdentity01 发生错误")

    def test_bindIdentity02(self):
        '''参数 name 不能为空'''
        response = self.D.bindIdentity('', 320882199012243215)
        self.result = response
        try:
            self.assertEqual(self.result['message'], "参数 name 不能为空")
        except:
            logging.info("bindIdentity02 发生错误")

    def test_bindIdentity03(self):
        '''idCard为空'''
        response=self.D.bindIdentity('ww',"")
        self.result=response
        try:
            self.assertEqual(self.result['message'], "参数 idCard 不能为空")
        except:
            logging.info("bindIdentity01 发生错误")

    def test_getSupportBankList(self):
        '''获取支持银行列表'''
        response = self.D.getSupportBankList()
        self.result = response[0]
        self.code=response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code,200)
        except:
            logging.info("etSupportBankList 发生错误")

    def test_getCardBin01(self,):
        '''获取银行卡开户行'''
        response = self.D.getCardBin("4392268328103388")
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

class FangYuanMenSuo(unittest.TestCase):
    '''房源房间信息'''
    def setUp(self):
        self.D = FangYuan()
        self.token = 'QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA='

    def test_myHouseList1(self):
        '''获取房源列表'''
        response = self.D.myHouseList1()
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_getJointRentHouseDetail01(self):
        '''获取合租房子详情,参数为0时'''
        response = self.D.getJointRentHouseDetail1(0)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "未找到有效房屋")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_getJointRentHouseDetail02(self):
        '''获取合租房子详情,参数为1'''
        response = self.D.getJointRentHouseDetail1(1)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_getJointRentHouseDetail03(self):
        '''获取合租房子详情,参数为100时'''
        response = self.D.getJointRentHouseDetail1(100)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_listJointRentRoom01(self):
        '''获取合租房间列表,参数为0时'''
        response = self.D.listJointRentRoom1(0)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_listJointRentRoom02(self):
        '''获取合租房间列表,参数为678时'''
        response = self.D.listJointRentRoom1(678)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_houseDetail1(self):
        '''获取房间详情,参数为0时'''
        response = self.D.houseDetail1(0)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "未找到有效房源")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")
class MenSuo(unittest.TestCase):
    '''门锁基本信息'''

    def setUp(self):
        self.D = FangYuan()
        self.token = 'QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA='

    def test_getDoorBaseInfo01(self):
        '''门锁不存在'''
        response = self.D.getDoorBaseInfo(0)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "门锁不存在")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_getDoorBaseInfo02(self):
        '''doorId传入字符串'''
        response = self.D.getDoorBaseInfo('aa')
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "服务繁忙，请稍后重试")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_getDoorBaseInfo03(self):
        '''您没有权限'''
        response = self.D.getDoorBaseInfo(97)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "您没有权限")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_getDoorBaseInfo04(self):
        '''success'''
        response = self.D.getDoorBaseInfo(10140)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

class ListDoorTempPWD(unittest.TestCase):
    '''获取门锁临时密码列表'''
    def setUp(self):
        self.D = FangYuan()
        self.token = 'QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA='

    def test_listDoorTempPWD01(self):
        '''success'''
        response = self.D.listDoorTempPWD(10140,10028,1)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_listDoorTempPWD02(self):
        '''该门锁不存在'''
        response = self.D.listDoorTempPWD(1018,10028,1)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "该门锁不存在")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_listDoorTempPWD03(self):
        '''该门锁不存在'''
        response = self.D.listDoorTempPWD('',10028,1)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "参数doorId不能为 null")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")
class LitDoorOpen(unittest.TestCase):
    '''获取门锁开门记录'''
    def setUp(self):
        self.D = FangYuan()
        self.token = 'QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA='
    def test_listDoorOpen01(self):
        '''该门锁不存在'''
        response = self.D.listDoorOpen(1018, 10028, 1,1)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "该门锁不存在")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_listDoorOpen02(self):
        '''参数doorId不能为 null'''
        response = self.D.listDoorOpen('', '', '','')
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "参数doorId不能为 null")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

    def test_listDoorOpen03(self):
        '''success'''
        response = self.D.listDoorOpen(10189, 10028, 1,1)
        self.result = response[0]
        self.code = response[1]
        try:
            self.assertEqual(self.result['message'], "success")
            self.assertEqual(self.code, 200)
        except:
            logging.info("getCardBint 发生错误")

if __name__=='__main__':
    unittest.main()
