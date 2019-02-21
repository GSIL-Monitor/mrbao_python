# coding:utf-8
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
def open(name,page):
    driver=webdriver.Firefox()
    url="https://www.zhipin.com/c101020100/?query=%s&page=%s"%(name,page)
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    try:
        WebDriverWait(driver,10).until(
            EC.visibility_of(driver.find_element(By.CLASS_NAME,'next'))
        )
    except:
        print("报错了")
        time.sleep(5)
    print(driver.current_url)
    print(driver.current_window_handle)
    html_content=driver.page_source
    #print(html_content)
    soup=BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
    job_content=soup.find('div',class_='job-list')
    job_content=job_content.find_all('div',class_='job-primary')
    #job_content=job_content.find_all('div',class_='info-primary')
    print(job_content)
    job_name=[]
    for content in job_content:
        info_primary=content.find('div',class_='info-primary')
        job_title=info_primary.find('div',class_='job-title').string#获取职位

        xinzhi=info_primary.find(class_='red').string#获取薪资

        info_detail=info_primary.find('div',class_='info-detail')
        tags=info_detail.find('div',class_='tags')
        #span=tags.find_all('span')
        #ceshi_type1=span.string
        #ceshi_type2=span.string
        #ceshi_type3=span.string
        name=content.find('div',class_='info-publis').h3
        name=name.string
        job_name.append((xinzhi,job_title,name))

    print(job_name)



open("测试工程师",1)
