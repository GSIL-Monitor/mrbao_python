# coding:utf-8
from common.appnium_desired import appnium_desired
from common.common_fun import Common
from selenium.webdriver.common.by import By
from data_shuju import DB
import logging


class Loginview(Common):

    def login_action(self,mobile):
        logging.info('---- Login ----')
        self.check_tiaoguo()
        self.input_mobile(mobile)
        self.send_yanzhengma()
        yanzhengma=DB()
        yanzhengma=yanzhengma.get_YanZhengMa(mobile)
        self.shuruyanzhengma(yanzhengma)
        self.click_login()
        logging.info('---- login success ----')

if __name__ == '__main__':
    driver=appnium_desired()

    A=Loginview(driver)

    A.login_action('18621512473')