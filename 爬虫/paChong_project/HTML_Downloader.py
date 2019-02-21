# coding:utf-8
import requests
class HtmlDownloader():
    def download(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT 10.0)'
        headers={'User-Agent':user_agent}
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            response.encoding='utf-8'
            return response.text
        return None