from appium import webdriver
import yaml
import logging
import logging.config
from selenium.common.exceptions import NoSuchElementException as A

with open('../config/desired_caps.yaml','r') as stream:
    data=yaml.load(stream)

CONF_LOG='../config/logging.conf'
logging.config.fileConfig(CONF_LOG)
logger=logging.getLogger('logging_info')
desired_caps={}
desired_caps['platformName'] =data['platforName']
desired_caps['udid'] = data['udid']
desired_caps['platforVersion'] = data['platforName']
desired_caps['deviceName'] = data['deviceName']
#desired_caps['app'] = data['app']
desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
desired_caps['noReset'] = 'False'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
def check_yuansu():
    logger.info("checking yuanshu")
    try:
        element=driver.find_element_by_id('com.yilou.fangdong:id/tv_jump')

    except A:
        logger.info("element is not found")
    else:
        element.click()
check_yuansu()