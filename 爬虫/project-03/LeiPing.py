# coding:utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urljoin
import time
import csv
import pymysql
import re
url="https://www.liepin.com/"
def open_(username,password,postion,page,x):
    driver=webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    ''' try:
        close_=WebDriverWait(driver,10).until(
            EC.visibility_of(driver.find_element(By.CLASS_NAME,'guider-close png_bg home-sprite'))
        )
        close_.click()
    except:
        print("NO FIND")
    time.sleep(3)'''
    try:
        login=WebDriverWait(driver,10).until(
            EC.visibility_of(driver.find_element(By.LINK_TEXT,"马上登录"))
        )
        login.click()
    except:
        print("服务繁忙")
    time.sleep(4)
    if username==18501787063:
        driver.find_element(By.XPATH,'html/body/div[2]/div[1]/div/div/section[1]/div[1]/form/div[1]/input').clear()
        driver.find_element(By.XPATH,'html/body/div[2]/div[1]/div/div/section[1]/div[1]/form/div[1]/input').send_keys(username)
        driver.find_element(By.XPATH,'html/body/div[2]/div[1]/div/div/section[1]/div[1]/form/div[2]/input').clear()
        driver.find_element(By.XPATH,'html/body/div[2]/div[1]/div/div/section[1]/div[1]/form/div[2]/input').send_keys(password)
        driver.find_element(By.XPATH,'html/body/div[2]/div[1]/div/div/section[1]/div[1]/form/input[3]').click()
        time.sleep(2)
    elif username!=18501787063:
        print("请输入正确的用户名")
    else:
        print("服务繁忙，请稍后重试")
    driver.find_element(By.XPATH,'html/body/div[3]/div[1]/div[1]/div/a/em').click()
    driver.find_element(By.XPATH,'html/body/div[3]/div[1]/div[2]/div[1]/form/input[5]').click()
    driver.find_element(By.XPATH,'html/body/div[3]/div[1]/div[2]/div[1]/form/input[5]').send_keys(postion)
    driver.find_element(By.XPATH,'html/body/div[3]/div[1]/div[2]/div[1]/form/button').click()
    now_handels=driver.current_window_handle
    driver.switch_to_window(now_handels)
    time.sleep(4)
    job=[]
    page_num=0
    while page_num<page:
        html_content=driver.page_source
        #print(html_content)
        soup=BeautifulSoup(html_content,'html5lib')
        clearfix=soup.find('div',class_='wrap clearfix')
        content=clearfix.find('div',class_='feeds-panel')
        content1=content.find('div',class_='feeds')
        job_content=content1.find('ul',class_='sojob-list')
        job_content=job_content.find_all('div',class_='sojob-item-main clearfix')
        for result in job_content:
            company_name=result.find('p',class_='company-name')
            company_name=company_name.string#获取公司名称
            job.append(company_name)
            #print(company_name)
            company_web=re.compile('<a href="(.*?)" target="_blank" title=".*?">')
            company_web=company_web.findall(str(result))#获取该公司当前招聘WEB
            #print(company_web)
            for result1 in company_web:
                job.append(result1)
            company_postion=re.compile('<h3 title="招聘软件测试工程师">(.*?)</h3>')
            company_postion=company_postion.findall(str(result))#获取当前职位
            for result2 in company_postion:
                job.append(result2)
            field_financing=re.compile('<p class="field-financing"><span>(.*?)</span></p>')
            field_financing=field_financing.findall(str(result))#获取公司行业信息
            for result3 in field_financing:
                job.append(result3)
            postion_web=result.find('a',class_='job-info')
            postion_web=postion_web.string#获取职位具体信息
            postion_web=re.compile('<a href="(.*?)" target="_blank" class="job-info">')
            postion_web=postion_web.findall(str(result))
            #job.append(postion_web)

            postion_xinzhi=result.find('p',class_='condition clearfix')
            postion_xinzhi=postion_xinzhi.string#获取职位薪资、学历要求、经验要求
            postion_xinzhi=re.compile('<p class="condition clearfix" title="(.*?)">')
            postion_xinzhi=postion_xinzhi.findall(str(result))
            for result4 in postion_xinzhi:
                job.append(result4)
        try:
            x +=1
            next_page=WebDriverWait(driver,10).until(
                EC.visibility_of_element_located(driver.find_element(By.LINK_TEXT,x))
            )
            next_page.click()
            print(driver.current_url)
            page_num +=1
        except:
            print("系统错误")
            break
        print("已经抓取了%s" % page_num)
    print(job)
open_(18501787063,'dabaoaiying1314','测试工程师',2,1)




