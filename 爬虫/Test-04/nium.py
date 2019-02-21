from selenium import webdriver
from selenium.webdriver.common.by import By
import _thread
def play(url,time):
    browser=webdriver.Firefox()
    browser.get(url)
    print(browser.page_source)
    browser.implicitly_wait(time)
    browser.maximize_window()
    browser.close()
    print("Is OK")
try:
    _thread.start_new_thread(play,("www.baidu.com",10,))
    _thread.start_new_thread(play,("www.baidu.com",8,))
except:
    print('123')

while 1:
    pass