# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
'''response=requests.get("http://www.weather.com.cn/weather/101190401.shtml")
response.encoding='utf-8'
r=response.headers
jar=requests.cookies.RequestCooloeJar()
print(r['connection'])
print(r.get('content-type'))
print(r)
for i,j in r.items():
    print(i,j)
r1=response.text
print(r)
#print(r1)
'''
url="http://www.weather.com.cn/weather/101190401.shtml"
def get_content(url):
    response=requests.get(url)
    response.encoding='utf-8'

    return response.text
def get_data(html):
    final=[]
    soup=BeautifulSoup(html,'html5lib')
    body=soup.body#获取body部分
    data=body.find('div',id='7d')#找出id为7d的div
    input1=data.find_all('input')
    ul=data.find('ul')
    li=ul.find_all('li')#获取所有的li
    for day in li :
        temp=[]
        date=day.find('h1').string#找到日期
        temp.append(date)
        inf=day.find_all('p')
        temp.append(inf[0].string) #第一个P标签中的(天气状况)加到temp中
        if inf[1].find('span')is None:
            temperature_highest=None
        else:
            temperature_highest=inf[1].find('span').string #找到最高温
            temperature_highest=temperature_highest.replace('℃','')
        temperature_lowest=inf[1].find('i').string#找到最低温
        temperature_lowest=temperature_lowest.replace('℃','')
        temp.append(temperature_highest)#添加最高温
        temp.append(temperature_lowest)#添加最低温
        final.append(temp)#将temp加到final中
    return final
'''写入文件CSV'''
def write_data(data,name):
    file_name=name
    with open(file_name,'a',errors='ignore',newline='') as f:
        f_csv=csv.writer(f)
        f_csv.writerows(data)
if __name__=='__main__':
    url = "http://www.weather.com.cn/weather/101190401.shtml"

    html=get_content(url)
    result=get_data(html)

    write_data(result,'weather.csv')