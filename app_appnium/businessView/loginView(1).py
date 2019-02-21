# coding:utf-8
import logging
from time import sleep

from common.appnium_desired import appnium_desired
from common.common_fun import Common
from common.data_shuju import DB


class Loginview(Common):
    '''
    app登录
    '''
    def login_action(self,mobile):
        '''
        :param mobile: 
        :return: 
        '''
        logging.info('---- Login ----')
        self.check_tiaoguo()
        self.input_mobile(mobile)
        self.send_yanzhengma()
        sleep(5)
        yanzhengma=DB()
        yanzhengma=yanzhengma.get_YanZhengMa(mobile)
        self.shuruyanzhengma(yanzhengma)
        self.click_login()
        logging.info('---- login success ----')

if __name__ == '__main__':
    driver=appnium_desired()

    A=Loginview(driver)

    A.login_action('18621512473')