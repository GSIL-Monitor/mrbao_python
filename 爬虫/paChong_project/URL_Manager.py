# -*- coding: utf-8 -*-
'''
1.判断是否有待取的URL，方法定义为：has_new_url()
2.添加新的URL到未爬取集合中，方法定义为add_new_url(url),add_new_urls(urls)
3.添加一个未爬取的URL，方法定义为get_new_url()
4.获取未爬取URL集合的大小，方法定义为new_url_size()
5.获取已经爬取的URL集合的大小，方法定义为old_url_size()
'''
class UrlManager():
    def __init__(self):
        self.new_urls=set() #未爬取URL集合
        self.old_urls=set() #已爬取URL集合

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return: 
        '''
        return self.new_url_size()!=0
    def get_new_url(self):
        '''
        获取一个未爬取的URL
        :return: 
        '''
        new_url=self.new_urls.pop()#获取一个未爬取的URL
        self.old_urls.add(new_url)
        return new_url
    def add_new_url(self,url):
        '''
        将新的URL添加到未爬取的URL集合中
        :param url: 单个URL
        :return: 
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        '''
        将新的URL 添加到未爬取的URL集合中
        :param urls: 
        :return: 
        '''
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    def new_url_size(self):
        '''
        获取未爬取URL结集合的大小
        :return: 
        '''
        return len(self.new_urls)
    def old_url_size(self):
        '''
        获取已经爬取URL集合的大小
        :return: 
        '''
        return len(self.old_urls)

