# coding:utf-8
#app启动配置
from appium import webdriver
import logging
import logging.config
import yaml

CONF_LOG='../config/logging.conf'
logging.config.fileConfig(CONF_LOG)
logger=logging.getLogger('logging_info')

def appnium_desired():
    with open('../config/desired_caps.yaml','r') as stream:
        data=yaml.load(stream)
    desired_caps = {}
    desired_caps['platformName'] = data['platforName']
    desired_caps['udid'] = data['udid']
    desired_caps['platforVersion'] = data['platforName']
    desired_caps['deviceName'] = data['deviceName']
    # desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = 'False'
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    logger.info('app is starting')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver
if __name__ == '__main__':
    appnium_desired()