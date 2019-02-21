# -*- coding: UTF-8 -*-
import requests
import re
import time
from bs4 import BeautifulSoup
import html5lib

login_url = "http://cf.basestonedata.com:8090/pages/viewpage.action"  # 登陆url
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip",
    "Accept-Language": "h-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Cookie": "JSESSIONID=5E9DEFE0E6E0DC54F397460C60E50B5A;crowd.token_key=63JD80wxx2kfcdrrzAs10g00;confluence-sidebar.width=388",
    "Host": "cf.basestonedata.com:8090",
}
data = {'pageId':33456205}
result = requests.get(url=login_url, headers=header, params=data)
print(result.url)
result_data = result.text
soup = BeautifulSoup(result_data, 'html.parser')
page_content = soup.find('div', class_='aui-page-panel')
#print(page_content)
jiekou_name=page_content.find('h1',class_='with-breadcrumbs')
jiekou_name=jiekou_name.find('a').string#获取接口名
print(jiekou_name)
main_content=page_content.find('div',class_='wiki-content')
print(main_content)
jiekou_address =re.compile(';">brand</span>(.*?)</p><')
jiekou_address=jiekou_address.findall(str(main_content))
print(jiekou_address[0])#获取接口地址
jiekou_desc=re.compile('">接口说明</h1><p>(.*?)</p><hr/>')
jiekou_desc=jiekou_desc.findall(str(main_content))
print(jiekou_desc[0])#获取接口说明

'''
page_content = soup.find('div', class_='aui-page-panel')

api_content = page_content.find('div', class_='pagetitle with-breadcrumbs')
api_content = api_content.find('h1', class_='with-breadcrumbs')
api_name = api_content.find('a').string  # 获取接口名
print(api_name)

api_result = page_content.find('table', class_='confluenceTable')

request_data=api_result.find('tbody')#获取请求参数
reauest_data=request_data.find('script').string
reauest_data=str(reauest_data)
reauest_canshu=re.sub('[\<\n\!CDATA\[\]\>]','',reauest_data)
reauest_canshu=reauest_canshu.replace('&quot;','')#接口请求参数
print(reauest_canshu)

api_result1 = re.compile('&lt;PORT&gt;</span>(.*?)</td><td class="confluenceTd" colspan="1">')
api_url = api_result1.findall(str(api_result))  # 获取接口地址
print(api_url[0])

response_data=api_result.find_all('tr')[3]#获取接口返回内容

api_desc=page_content.find('div',class_='wiki-content')
api_desc=api_desc.find('span').string#获取接口描述
print(api_desc)
'''
