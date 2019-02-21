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
import csv
def open1(name,page):
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
    #print(driver.current_url)
    #print(driver.current_window_handle)
    #html_content=driver.page_source
    #print(html_content)
    job_name = []
    page_num = 0
    while page_num<10:
        js="window.scrollTo(0,document.body.scrollHeight);"
        driver.execute_script(js)
        time.sleep(5)
        #print(driver.current_url)
        html_content = driver.page_source
        soup=BeautifulSoup(html_content,'html.parser')
        job_content=soup.find('div',class_='job-list')

        job_content=job_content.find_all('div',class_='job-primary')
        #print(job_content)
        #outIn = open('boss_csv.csv', 'r')
        #csv_write = csv.writer(outIn)

        for content in job_content:
            jop_title=content.find('div',class_='job-title').string#获取岗位名称
            jop_xinzhi = content.find('span', class_='red').string  # 获取岗位薪资
            #jop_title=jop_title.string
            company_text=content.find('div',class_='company-text').h3
            company_text=company_text.find('a').string#获取公司名

            vline = content.find('div', class_='company-text').p
            vline = vline.string  # 获取公司行业

            info_primary = content.find('div', class_='info-primary')
            address = info_primary.p
            address = address.string  # 获取公司地址

            info_primary=content.find('div',class_='info-primary')
            info_primary=info_primary.find('h3',class_='name')
            ka=info_primary.find('a').get('ka')
            href=info_primary.find('a').get('href')
            #print(ka)
            #print(href)
            new_url=urljoin("https://www.zhipin.com/c101020100",href)
            new_url=new_url+"?"+"ka="+ka
            #print(new_url)
            job_name.append((jop_title, company_text,jop_xinzhi, new_url))
            #csv_write.writerow(job_name)
            #print("write now")
            #outIn.close()
            #print(job_name)
        try:
            nex_page=WebDriverWait(driver,10).until(
            EC.visibility_of(driver.find_element(By.CLASS_NAME,'next'))
            )
            nex_page.click()
            print(driver.current_url)
            page_num += 1
            #html_content = driver.page_source
            #page_num+=1
            #time.sleep(5)
        except:
            print("报错了")
            break
            #print("已经抓取了%s"%page_num)
            #break
        print("已经抓取了%s" % page_num)
    print(job_name)
    return job_name
def output_txt():
    job_name=open1("测试工程师",1)
    header=['job_title','company_text','job_xinzhi','new_url']
    with open('BOSS.csv','w',encoding='utf-8') as f:
        f_csv=csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(job_name)
if __name__=='__main__':
    output_txt()

#open("测试工程师",1)
