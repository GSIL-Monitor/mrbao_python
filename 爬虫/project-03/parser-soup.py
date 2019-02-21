# coding:utf-8
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from urllib.parse import urljoin
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
        time.sleep(3)
    js="window.scrollTo(0,document.body.scrollHeight);"
    driver.execute_script(js)
    print(driver.current_url)
    #html_content=driver.page_source
    page_num = 0
    job_name = []
    while page_num<11:
        js = "window.scrollTo(0,document.body.scrollHeight);"
        driver.execute_script(js)
        time.sleep(5)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        job_content = soup.find('div', class_='job-list')
        job_content = job_content.find_all('div', class_='job-primary')
        # print(job_content)
        '''
        soup=BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        job_content=soup.find('div',class_='job-list')

        job_content=job_content.find_all('div',class_='job-primary')
        #print(job_content)
        '''
        for content in job_content:
            jop_title=content.find('div',class_='job-title').string#获取岗位名称
            jop_xinzhi=content.find('span',class_='red').string#获取岗位薪资
            #jop_title=jop_title.string
            company_text=content.find('div',class_='company-text').h3
            company_text=company_text.find('a').string#获取公司名

            vline=content.find('div',class_='company-text').p
            vline=vline.string#获取公司行业

            info_primary=content.find('div',class_='info-primary')
            address=info_primary.p
            address=address.string#获取公司地址

            info_primary=info_primary.find('h3',class_='name')
            ka=info_primary.find('a').get('ka')
            href=info_primary.find('a').get('href')
            #print(ka)
            #print(href)
            new_url=urljoin("https://www.zhipin.com/c101020100",href)#岗位跳转网址
            new_url=new_url+"?"+"ka="+ka
            #print(new_url)
            job_name.append((jop_title, company_text,vline,address,jop_xinzhi, new_url))
            #print(job_name)
            '''
                        try:
                nex_page=WebDriverWait(driver,10).until(
                    EC.visibility_of(driver.find_element(By.CLASS_NAME,'next'))
                )
                nex_page.click()
                #html_content = driver.page_source
                page_num+=1
                time.sleep(5)
            except:
                print("报错了")
            #print("已经抓取了%s"%page_num)'''

        #page_num += 1
        #print("已经抓取了%s" % page_num)
    print(job_name)
open("测试工程师",1)
