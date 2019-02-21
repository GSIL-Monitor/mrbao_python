# coding: utf-8
import requests
import csv
import json
from bs4 import BeautifulSoup
user_agent= 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT 10.0)'
headers={'User_agent':user_agent}
uri="http://seputu.com/"
response=requests.get(url=uri,headers=headers)
#print(response.text)
result=response.text
soup=BeautifulSoup(result,from_encoding='utf-8')
content=[]
for mulu in soup.find_all('div',class_="mulu"):
    h2=mulu.find('h2')
    if h2!=None:
        h2_title=h2.string
        list=[]

        for a in mulu.find(class_="box").find_all('a'):
            href=a.get('href')
            box_title=a.get('title')
            list.append({'href':href,'box_title':box_title})

            print(list)
        content.append({'title':h2_title,'content':list})
#with open('qiye.json','w') as fp:
    #json.dump(content,fp=fp,indent=4)


