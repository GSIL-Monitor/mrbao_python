# coding=utf-8
import requests

class HtmlDownloader():
    def download(self,url):
        if url is None:
            return
        user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
        header={'User-Agent':user_agent}
        response=requests.get(url,header=header)
        if response.status_code==200:
            response.encoding='utf-8'
            return response.text
        return None

