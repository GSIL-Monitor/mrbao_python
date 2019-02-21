# -*- coding: UTF-8 -*-
import unittest
from Xiaoxiangyoupin.xiaoxiang_module.xiaoxiang_login import Xixoxiang_Login
from Xiaoxiangyoupin.xiaoxiang_common.startEnd import StartEnd

class Test_api_login(StartEnd,Xixoxiang_Login):
    '''登录测试'''
    def test_login_in_01(self):
        response=self.login(mobile='18501787063',verifcode='888888')
        try:
            self.assertEqual(response['heads']['message'],'success')
            self.assertIsNotNone(response['body']['token'])
            print("执行test_login_in_01")
        except:
            print ('test_login_in_01 测试未通过')

if __name__ == '__main__':
    unittest.main()