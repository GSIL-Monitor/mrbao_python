# coding:utf-8
from Data_Output import DataOutput
from HTML_Downloader import HtmlDownloader
from HTML_Paraser import HtmlParser
from URL_Manager import UrlManager
class SpiderMan():
    def __init__(self):
        self.manage=UrlManager()
        self.downloader=HtmlDownloader()
        self.parser=HtmlParser()
        self.output=DataOutput()

    def crawl(self,root_url):
        #添加入口url
        self.manage.add_new_url(root_url)
        #判断URL 管理器中是否有新的URL，同时判断抓取了多少个url
        while(self.manage.has_new_url() and self.manage.old_url_size()<100):
            try:
                #从url 管理器获取新的URL
                new_url=self.manage.get_new_url()
                #html下载器下载网页
                html=self.downloader.download(new_url)
                #html解析器抽取网页数据
                new_urls,data=self.parser.parser(new_url,html)
                #将抽取的url添加到url管理器中
                self.manage.add_new_urls(new_urls)
                #数据库存储器存储文件
                self.output.store_data(data)
                print("已经抓取%s个连接"% self.manage.old_url_size())
            except Exception as e:
                print("crawl failed")
        self.output.output_html()
if __name__=='__main__':
    spider_man=SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.html")



