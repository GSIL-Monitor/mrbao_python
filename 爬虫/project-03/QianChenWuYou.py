# coding:utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from urllib.parse import urljoin
import csv
import requests
import html5lib
import re
url="http://www.51job.com/"
def _open(name,page):
    driver=webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element(By.ID,'kwdselectid').clear()
    driver.find_element(By.ID,'kwdselectid').send_keys(name)
    driver.find_element(By.CSS_SELECTOR,'.ush.top_wrap>button').click()
    try:
        WebDriverWait(driver,10).until(
            EC.visibility_of(driver.find_element(By.CSS_SELECTOR,'.bk>a'))
        )
    except:
        print("open is false")
    #print(driver.current_url)
    zhiwei_web=[]
    zhiwei_data=[]
    company_web=[]
    company_data=[]
    address1=[]
    xinzhi1=[]
    newtime1=[]
    page_num=0
    while page_num<page:
        #js = "window.scrollTo(0,document.body.scrollHeight"
        #driver.execute_script(js)
        #time.sleep(4)
        #current_url=driver.current_url
        #response=requests.get(current_url)
        #html_content=response.text
        html_content=driver.page_source
        soup=BeautifulSoup(html_content,'html5lib')
        result=soup.find('div',class_='dw_wp')
        result=result.find('div',id='resultList')

        title=result.find('div',class_='el title')
        position=title.find('span',class_='t1').string#职位名
        company=title.find('span',class_='t2').string#公司名
        address=title.find('span',class_='t3').string#工作地点
        xinzhi=title.find('span',class_='t4').string#薪资
        newtime=title.find('span',class_='t5').string#发布时间
        #result.div['class']="myclass"
        job_content=result.find_all('div',class_="el")
        #print(job_content)
        #print(type(job_content))
        #we=re.compile('<a href="(.*?)" onmousedown="" target="_blank" title="(.*?)">.*?</a><span class="t2"><a href="(.*?)" target="_blank" title="(.*?)">.*?</a></span>.*?<span class="t3">(.*?)</span><span class="t4">(.*?)</span><span class="t5">(.*?)</span>')
        #data=we.findall(str(job_content))
        #print(data)
        job_title= re.compile('<a href="(.*?)" onmousedown="" target="_blank" title="(.*?)">')#匹配职位具体信息和职位信息
        title1 = job_title.findall(str(job_content))
        #print(title1)
        for result in title1:
            zhiwei_data1=result[1]
            zhiwei_web1=result[0]
            zhiwei_data.append(zhiwei_data1)
            zhiwei_web.append(zhiwei_web1)
        _company=re.compile('<span class="t2"><a href="(.*?)" target="_blank" title="(.*?)">.*?</a></span>')#匹配公司介绍网址和公司名
        company_content=_company.findall(str(job_content))
        print(company_content)
        for result in company_content:
            company_web1=result[0]
            company_data1=result[1]
            company_web.append(company_web1)
            company_data.append(company_data1)
        _company_address=re.compile('<span class="t3">(.*?)</span>')#匹配公司地址
        company_address=_company_address.findall(str(job_content))
        company_address.pop(0)
        for result1 in company_address:
            address1.append(result1)
        #print(company_address)
        _xinzhi=re.compile('<span class="t4">(.*?)</span>')#匹配职位薪资
        xinzhi=_xinzhi.findall(str(job_content))
        xinzhi.pop(0)
        for result2 in xinzhi:
            xinzhi1.append(result2)
        #print(xinzhi)
        _newtime=re.compile('<span class="t5">(.*?)</span>')#匹配发布日期
        newtime=_newtime.findall(str(job_content))
        newtime.pop(0)
        for result3 in newtime:
            newtime1.append(result3)
        #print(zhiwei_data,zhiwei_web,company_data,company_web,address,xinzhi1,newtime1)
        #print(newtime)
        header=['zhiwei_data','zhiwei_web','company_data','company_web','xinzhi1','address1','newtime1']
        with open('QianChenWuYou.csv','w',encoding='utf-8') as f:
            write1=csv.writer(f)
            write1.writerow(header)
            for i in zip(zhiwei_data,zhiwei_web,company_data,company_web,xinzhi1,address1,newtime1):
                write1.writerow(i)
            f.close()
        try:
            nex_page=WebDriverWait(driver,10).until(
            EC.visibility_of(driver.find_element(By.LINK_TEXT,"下一页"))
            )
            nex_page.click()
            print(driver.current_url)#打印当前网址
            page_num += 1
        except:
            print("报错了")
            break
        print("已经抓取了%s" % page_num)
_open("测试工程师",2)
