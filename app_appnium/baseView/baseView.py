# coding:utf-8
from selenium.webdriver.support.ui import WebDriverWait
class BaseView(object):

    def __init__(self,driver):

        self.driver=driver

    def find_element(self,*loc):

        return self.driver.find_element(*loc)

    def save_screenshot(self,tupian):

        self.driver.save_screenshot(tupian)

    def get_screenshot_as_file(self,weizhi):

        self.driver.get_screenshot_as_file(weizhi)

    def switch_to_context(self):

        contexts = self.driver.contexts

        return self.driver.switch_to.contexts(contexts[0]),self.driver.switch_to.contexts(contexts[1])

    def webdriver(self,*loc):

        return WebDriverWait(self.driver,3).until(lambda x:x.find_element(*loc))

    def swith_to_alert(self):

        return self.driver.switch_to.alert.accept()