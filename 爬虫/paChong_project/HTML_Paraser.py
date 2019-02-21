# coding:utf-8
import re
import requests
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
class HtmlParser():
    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url: 下载页面的URL
        :param html_cont: 下载的网页内容
        :return: 返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='uft-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data
    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的URL集合
        :param page_url:下载页面的URL 
        :param soup: 
        :return: 
        '''
        new_urls=set()
        links=soup.find_all('a')#,href=re.compile('href=".*?"')
        for link in links:
            #提取href属性
            new_url=link.get('href')
            #拼接完整网址
            new_full_url=urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url: 
        :param soup: 
        :return: 
        '''
        data={}
        data['url']=page_url
        title=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title']=title.get_text()
        summary= soup.find('div',class_='lemma-summary')
        data['summary']=summary.get_text()
        return data
