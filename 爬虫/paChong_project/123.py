from urllib.parse import urljoin
import re
from bs4 import BeautifulSoup
import requests
def reuqest():
    url="http://baike.baidu.com/view/284853.html"
    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT 10.0)'
    headers = {'User-Agent': user_agent}
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        result=response.text.encode('utf-8')
    results=_get_new_urls(url,result)
    return results
def _get_new_urls(url, results):
    '''
    抽取新的URL集合
    :param page_url:下载页面的URL 
    :param soup: 
    :return: 
    '''
    new_urls = set()
    soup=BeautifulSoup(results,'html.parser',from_encoding='uft-8')
    links = soup.find_all('a')  # href=re.compile(r'/view/\d+.htm')
    for link in links:
        # 提取href属性
        new_url = link.get('href')
        # 拼接完整网址
        new_full_url = urljoin(url, new_url)
        new_urls.add(new_full_url)
        print(new_urls)
    print(new_urls)
if __name__=='__main__':
    reuqest()