# -*- coding: UTF-8 -*-
from fangdong_getmyinfo import *
from startEnd import  StartEnd
class Test_BDzhuli_fangdong_quanxian(StartEnd):
    ''''''
    @zhuangshi_canshu(mobile='18621512473')#18217111076
    def test_quanxian(self):
        '''切换至18621512473权限'''
        switch_account(getIdentityList())

if __name__ == '__main__':
    A=Test_BDzhuli_fangdong_quanxian()
    A.test_quanxian()