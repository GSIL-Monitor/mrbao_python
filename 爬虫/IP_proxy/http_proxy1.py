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
import logging
LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='IP_proxy.log',level=logging.INFO,format=LOG_FORMAT)
url="https://www.kuaidaili.com/"
new_url=set()#未抓取URL
old_url=set()#已抓取URL
ip_data = []#存储IP
ip_portData = []#存储IP端口号
ip_typeData = []#存储IP类型
ip_timeData = []#存储IP获取时间
ip_listData=[]
def ip_Proxy(x,y):
    driver=webdriver.Firefox()
    driver.get(url)
    logging.info("Now open %s"% url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT,"免费代理").click()
    logging.info("xitong is clicking free's proxy")
    time.sleep(3)
    driver.find_element(By.XPATH,'html/body/div[1]/div[3]/div[2]/div/div[1]/a[1]').click()
    while x<y:
        js = "window.scrollTo(0,document.body.scrollHeight);"
        driver.execute_script(js)
        logging.info("xitong is excuxeing JS。。。。。")
        time.sleep(4)
        page_content=driver.page_source
        soup=BeautifulSoup(page_content,'html5lib')
        logging.info("print html")
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
            logging.info("huoqu url:%s"%new_url)
            #print(new_url1)
            new_url.add(new_url1)
        web_content = con_body.find('table', class_='table table-bordered table-striped')
        web_content = web_content.find('tbody')
        ip_content = web_content.find_all('tr')
        for result in ip_content:
            ip_address = re.compile('<td data-title="IP">(.*?)</td>')
            ip_address = ip_address.findall(str(result))
            for result1 in ip_address:
                ip_data.append(result1)
                ip_listData.append({'ip_address':ip_data})
            ip_port = re.compile('<td data-title="PORT">(.*?)</td>')
            ip_port = ip_port.findall(str(result))
            for result2 in ip_port:
                ip_portData.append(result2)
                ip_listData.append({'ip_port':ip_portData})
            ip_type = re.compile('<td data-title="类型">(.*?)</td>')
            ip_type = ip_type.findall(str(result))
            for result3 in ip_type:
                ip_typeData.append(result3)
                ip_listData.append({'ip_type':ip_typeData})
            ip_time = re.compile('<td data-title="最后验证时间">(.*?)</td>')
            ip_time = ip_time.findall(str(result))
            for result4 in ip_time:
                ip_timeData.append(result4)
                ip_listData.append({'ip_time':ip_timeData})
        header=['ip_address','ip_port','ip_type','ip_time']
        with open('ip_list.csv','w',encoding='utf-8') as f:#保存为CSV
            writer1=csv.writer(f)
            writer1.writerow(header)
            for i in zip(ip_data,ip_portData,ip_typeData,ip_timeData):
                writer1.writerow(i)
            f.close()
        with open('ip_list.json','w',encoding='utf-8') as f:
            json.dump(ip_listData,fp=f,indent=4)
            f.close()
        try:
            x +=1
            nex_page=WebDriverWait(driver,10).until(
                EC.visibility_of(driver.find_element(By.LINK_TEXT,x))
            )
            nex_page.click()
            logging.info("点击下一页：%s"%x)
            print("NOW current page is %s page "%x)
            #new_url2 = new_url.pop()
            #old_url.add(new_url2)
        except:
            print("系统错误")
            break
        #return ip_listData
        driver.close()
        print(new_url)
ip_Proxy(1,5)
#def get_url(url1):d
    #new_url2=url1.pop()
    #old_url.add(new_url2)
    #return new_url2
def ip_rewuest(new_url2):
    ip_data=[]
    ip_portData=[]
    ip_typeData=[]
    ip_timeData=[]
    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT 10.0)'
    header={'User-Agent':user_agent }
    response=requests.get(new_url2,headers=header)
    if response.status_code==200:
        response.encoding='utf-8'
        #print(response.text)
        response_content=response.text
        soup=BeautifulSoup(response_content,'html5lib')
        content=soup.find('div',id='content')
        web_content=content.find('div',class_='con-body')
        web_content=web_content.find('table',class_='table table-bordered table-striped')
        web_content=web_content.find('tbody')
        ip_content=web_content.find_all('tr')
        for result in ip_content:
            ip_address=re.compile('<td data-title="IP">(.*?)</td>')
            ip_address=ip_address.findall(str(result))
            for result1 in ip_address:
                ip_data.append(result1)
            ip_port=re.compile('<td data-title="PORT">(.*?)</td>')
            ip_port=ip_port.findall(str(result))
            for result2 in ip_port:
                ip_portData.append(result2)
            ip_type=re.compile('<td data-title="类型">(.*?)</td>')
            ip_type=ip_type.findall(str(result))
            for result3 in ip_type:
                ip_typeData.append(result3)
            ip_time=re.compile('<td data-title="最后验证时间">(.*?)</td>')
            ip_time=ip_time.findall(str(result))
            for result4 in ip_time:
                ip_timeData.append(result4)
        print(ip_data)
        print(ip_portData)
        print(ip_typeData)
#ip_rewuest()
'''
if __name__=='__main__':
    new_url2=ip_Proxy(1)
    print(new_url2)
    #url2=get_url(url1)
    try:
        #if new_url2 not in old_url:
        ip_rewuest(new_url2)
    except:
        print("系统错误")
    '''
