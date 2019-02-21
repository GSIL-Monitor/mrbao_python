# coding=utf-8
import re
from bs4 import BeautifulSoup
class HtmlParaser():
    def parser_url(self,url,response):
        pattern=re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls=pattern.findall(response)
        if urls!=None:
            #将urls 进行去重
            return list(set(urls))
        else:
            return None

    def parser_json(self,page_url,response):
        '''
        解析响应
        :param page_url: 
        :param response: 
        :return: 
        '''
