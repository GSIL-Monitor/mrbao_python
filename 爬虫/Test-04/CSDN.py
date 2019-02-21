# -*- coding: utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep,ctime
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
url="https://edu.csdn.net/?ref=toolbar"
try:
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    sleep(5)
    driver.find_element(By.CLASS_NAME,'chaclose').click()
    sleep(2)
except:
    print("----Open csdn is false----")
finally:
    driver.find_element(By.CLASS_NAME,'inp_srh').send_keys("python 爬虫")
    driver.find_element(By.CLASS_NAME,'btn_srh').click()
    sleep(5)
url=driver.current_url
print(url)
try:
    response=requests.get(url)
    result=response.text
    print(response.headers)
    print(response.status_code)
except:
    print("request url is false")
finally:
    soup=BeautifulSoup(result,'html5lib')
    content=soup.find('ul',class_='course_list')
    list=[]
    for li in content.find_all(class_='clearfix'):
        link_content=li.find('a')
        jpg_link=link_content.get('href')
        #print("jpg_link="+jpg_link)
        text=li.find('div',class_='c_list_con')
        text1=text.find('h3')
        text_content=text1.find('a')
        text_link=text_content.get('href')
        text_string=repr(text_content.string)
        #print('jpg_link='+jpg_link)
        #print('text_link='+text_link)
        #print("text_string="+text_string)
        list.append({'jpg_link':jpg_link,'text_link':text_link,'text_string':text_string})
with open('csdn.json','w') as fp:
    json.dump(list,fp=fp,indent=2)







