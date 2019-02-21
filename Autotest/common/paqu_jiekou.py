# -*- coding: UTF-8 -*-
import requests
import re
import time
from bs4 import BeautifulSoup
import pymysql


def paqu_jiekou(page_num):
    jekou = {}
    page = 1
    con=pymysql.connect(host='127.0.0.1',user='root',password='666888',port=3306,db='lianxi',charset='utf8')
    cur=con.cursor()

    while page_num < 11829798:
        base_url = "http://wiki.superjia.com/confluence/pages/viewpage.action"  # 登陆url
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip",
            "Accept-Language": "h-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
            "Cookie": "JSESSIONID=712940E2A8C223D5FAA56C3A8708EF04;gr_user_id=0557ef18-0bde-46de-b8f6-f4973ee9d830;doc-sidebar=300px",
            "Host": "wiki.superjia.com",
        }
        data = {'pageId': page_num}  # 11165574
        result = requests.post(url=base_url, headers=header, params=data)
        if result.status_code == 404:
            page_num += 1
            continue
        else:
            result_data = result.text
            soup = BeautifulSoup(result_data, 'html.parser')
            page_content = soup.find('div', class_='aui-page-panel')
            api_content = page_content.find('div', class_='pagetitle with-breadcrumbs')
            api_content1 = api_content.find('h1', class_='with-breadcrumbs')

            api_name = api_content1.find('a').string  # 获取接口名

            jekou['api_name'] = api_name  # 加入接口名
            api_result = page_content.find('table', class_='confluenceTable')

            if hasattr(api_result,'find')==False:
                page_num += 1
                continue
            else:
                request_data = api_result.find('tbody')  # 获取请求参数
                if hasattr(request_data.find('script'),'string')==False:
                    page_num += 1
                    continue
                else:
                    reauest_data = request_data.find('script').string
                    reauest_data = str(reauest_data)
                    reauest_canshu = re.sub('[\<\!CDATA\[\]\>]', '', reauest_data)
                    reauest_canshu = reauest_canshu.replace('&quot;', '')  # 接口请求参数
                    reauest_canshu=reauest_canshu.replace('\n','')
                    reauest_canshu=reauest_canshu.replace('\t','')
                    reauest_canshu=reauest_canshu.strip()
                    jekou['reauest_canshu'] = reauest_canshu  # 加入请求参数
                    api_result1 = re.compile('&lt;PORT&gt;</span>(.*?)</td><td class="confluenceTd" colspan="1">')
                    api_url = api_result1.findall(str(api_result))  # 获取接口地址
                    if api_url[0] !=None:
                        jekou['api_url'] = api_url# 加入接口地址
                    else:
                        jekou['api_url'] ='1'

                    api_desc = page_content.find('div', class_='wiki-content')
                    api_desc = api_desc.find('span').string  # 获取接口描述
                    jekou['api_desc'] = api_desc  # 加入接口描述
                    sql="INSERT INTO `lianxi`.`apitest_modules_interface` ( `api_name`, `api_url`, `api_canshu`, `api_response`, `api_desc`, `module_id`) VALUES ( %s, %s, %s, 1,%s, '一楼APP实名登记', '7');"\
                        %( jekou['api_name'], jekou['api_url'], jekou['reauest_canshu'],jekou['api_desc'])
                    cur.execute(sql)
                    print(jekou)
                    print(page_num)
                    page_num += 1
                    page += 1
                    print("正在爬取第%d页" % page)

def insert_sql():
    ''''''
def selcte_sql():
    sql='select * from lianxi.apitest_enveronment;'
    con=pymysql.connect(host='127.0.0.1',user='root',password='666888',port=3306,db='lianxi',charset='utf8')
    cur=con.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    print(type(result))
    print(result)
def paqu_login():
    ''''''
    login_url = "http://wiki.superjia.com/confluence"
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip",
        "Accept-Language": "h-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=B8F4133717EA089D2D998A41D6BE571E;gr_user_id=0557ef18-0bde-46de-b8f6-f4973ee9d830;doc-sidebar=300px",
        "Host": "wiki.superjia.com"}
    data = {'login': '%E7%99%BB%E5%BD%95&', 'os_username': 'mrbao', 'os_password': 'baotao19901224',
            'os_destination': ''}
    response = requests.post(url=login_url, headers=header, data=data)

    response_cookie = re.compile("Cookie': 'JSESSIONID=(.*?); Path=/confluence',")
    response_cookie = response_cookie.findall(str(response.headers))
    return response_cookie[0]

paqu_jiekou(11165574)
