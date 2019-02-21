#coding:utf-8
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import html5lib
import requests
import csv
import json
from urllib.parse import urljoin
from pyquery import PyQuery as pq
url="https://www.kuaidaili.com/"
new_url=set()#未抓取URL
old_url=set()#已抓取URL
ip_data = []#存储IP
ip_portData = []#存储IP端口号
ip_typeData = []#存储IP类型
ip_timeData = []#存储IP获取时间
ip_listData=[]
def ip_Proxy(x):
    driver=webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT,"免费代理").click()
    time.sleep(3)
    driver.find_element(By.XPATH,'html/body/div[1]/div[3]/div[2]/div/div[1]/a[1]').click()
    while True:
        #js = "window.scrollTo(0,document.body.scrollHeight);"
        #driver.execute_script(js)
        #time.sleep(4)
        page_content=driver.page_source
        soup=BeautifulSoup(page_content,'html5lib')
        con_body=soup.find('div',class_='con-body')
        id_list=con_body.find('div',id='list')
        listnav=id_list.find('div',id='listnav')
        ip_web=listnav.find('ul')
        li_list=ip_web.find_all('li')
        ip_href=re.compile('href="(.*?)">.*?</a>')
        ip_href=ip_href.findall(str(li_list))
        for result in ip_href:
            #print(result)
            new_url1=urljoin(url,result)
            print(new_url1)
            new_url.add(new_url1)
        try:
            x = x + 1
            nex_page = WebDriverWait(driver,10).until(
                EC.visibility_of(driver.find_element(By.XPATH,'html/body/div[1]/div[3]/div[2]/div/div[2]/div[1]/ul/li[%s]/a' % x))
            )
            nex_page.click()
            print("现在是第 %s 页" % x)
            # new_url2 = new_url.pop()
            # old_url.add(new_url2)
        except:
            print("系统错误")
            break
        return ip_listData
    # print(new_url)
ip_Proxy(2)
