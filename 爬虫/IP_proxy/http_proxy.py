#coding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pymysql
import json
#from http.server import BaseHTTPRequestHandler,HTTPServer,HTTPStatus
url='http://www.xicidaili.com/nn/'
def proxy(page):
    driver=webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    try:
        WebDriverWait(driver,10).until(
            EC.visibility_of(driver.find_element(By.CLASS_NAME,'next_page'))
        )
    except:
        print("系统错误")
        time.sleep(4)
    page_num=0
    ip_list1=[]
    ip_web=[]
    ip_list2=[]
    while page_num<page:
        js = "window.scrollTo(0,document.body.scrollHeight);"
        driver.execute_script(js)
        time.sleep(4)
        page_content = driver.page_source
        soup = BeautifulSoup(page_content, 'html5lib')
        #print(page_content)
        wrapper=soup.find('div',id='wrapper')
        body=wrapper.find('div',id='body')
        ip_list=body.find('table',id='ip_list')
        ip_list=ip_list.find('tbody')
        ip_proxy = ip_list.find_all('tr')
        for result in ip_proxy:
            #ip_proxy1=result.find_all('td')
            ip_proxy2= re.compile('<td>(.*?)</td>')
            result2 = ip_proxy2.findall(str(result))
            ip_list2.append(result2)
            ip_list1.append({'data':result2})
        try:
            next_page=WebDriverWait(driver,10).until(
                EC.visibility_of(driver.find_element(By.CLASS_NAME,'next_page'))
            )
            next_page.click()
            page_num +=1
            print(driver.current_url)
            web_address=driver.current_url
            ip_web.append(web_address)
        except:
            print("系统错误")
        print("已经抓取了%s" % page_num)
        break
    print(ip_list1)
    print(ip_web)
    driver.close()
    with open('ip.json','wb')as fp:
        #json.dump(ip_list1,fp)
        fp.write((json.dumps(ip_list1).encode("utf-8")))
        fp.close()
    return ip_list2

if __name__=='__main__':
    proxy(20)