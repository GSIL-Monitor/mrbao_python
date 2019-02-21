# coding:utf-8
from selenium.common.exceptions import NoSuchElementException as A
from baseView.baseView import BaseView
from common.appnium_desired import appnium_desired
import logging
from selenium.webdriver.common.by import By

class Common(BaseView):
    def check_tiaoguo(self):
        #进入app跳过广告页
        tiaoguo_id = (By.ID,'com.yilou.fangdong:id/tv_jump')  # 点击跳过
        logging.info("check tiaoguo yuanshu")
        try:
            element=self.find_element(*tiaoguo_id)

        except A :
            logging.info('element not found')

        else:
            element.click()
            logging.info('click tiaoguo success')

    def shoushi(self):
        #是否需要设置手势
        shoushiye_tiaoguo=(By.ID,'com.yilou.fangdong:id/title_right')
        logging.info('click shoushiye_tiaoguo ')
        try:
            element=self.find_element(*shoushiye_tiaoguo)

        except A:
            logging.info('click shoushiye_tiaoguo ')

        else:
            element.click()

    def check_gengxin(self):
        #是否需要更新
        gengxin_id = (By.ID, 'com.yilou.fangdong:id/cancelBtn')
        logging.info("check tiaoguo yuanshu")
        try:
            element=self.find_element(*gengxin_id)

        except A :
            logging.info('element not found')

        else:
            element.click()
            logging.info('click tiaoguo success')

    def input_mobile(self,mobile):
        #填写手机号
        mobile_id = (By.ID,'com.yilou.fangdong:id/phoneTxt')
        logging.info("check mobile_id yuanshu")
        try:
            element=self.find_element(*mobile_id)

        except A :
            logging.info('element not found')

        else:
            element.send_keys(mobile)
            logging.info('tianxie'+ mobile+'success!')

    def send_yanzhengma(self):
        #发送验证码
        sendyanzhengma_id=(By.ID,'com.yilou.fangdong:id/codeBtn')
        try:
            element=self.find_element(*sendyanzhengma_id)
        except A :
            logging.info('element not found')

        else:
            element.click()
            logging.info('send yanzhengma success!')

    def shuruyanzhengma(self,yanzhengma):
        #输入验证码
        yanzhengma_id = (By.ID, 'com.yilou.fangdong:id/codeTxt')
        try:
            element = self.find_element(*yanzhengma_id)
        except A:
            logging.info('element not found')

        else:
            element.send_keys(yanzhengma)
            logging.info('shuru yanzhengma success!')

    def click_login(self):
        #点击登录
        logging.info('Logining')
        login_id = (By.ID, 'com.yilou.fangdong:id/loginBtn')
        try:
            element = self.find_element(*login_id)
        except A:
            logging.info('element not found')

        else:
            element.click()
            logging.info('shuru yanzhengma success!')

if __name__ == '__main__':
    driver=appnium_desired()
    con=Common(driver)

    con.check_tiaoguo()
    con.check_gengxin()