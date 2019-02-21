import requests
import json
url="http://www.baidu.com/"
reponse=requests.head(url)
print(reponse.headers)
url1="http://httpbin.org/get"
payload={'key1':'value1','key2':['value2','value3']}
response=requests.get(url1,params=payload)
print(response.url)
response=requests.get('https://github.com/timeline.json')
print(response.text)
print(response.content)
print(response.encoding)
url2="https://github.com/timeline.json"
response=requests.get(url2)
print(response.json())
result=response.json()
for results in result:
    print(result)

print("===========================================")


data={'key1':'value1','key2':'value2'}
response=requests.post("http://httpbin.org/post",data=data)
print(response.text)
print("++++++++++++++++++++++++++++++++++++++++")
data=(('key1','value1'),('key2','value2'))
response=requests.post("http://httpbin.org/post",data=data)
print(response.text)
print("+++++++++++++++++++++++++++++++")
#url="http://httpbin.org/post"
#files={'file':open('report.xls','rb')}
#response=requests.post(url,files=files)
#print(response.text)

url="http://example.com/some/cookie/setting/url"
response=requests.get(url)
print(response.cookies)

url='http://httpbin.org/cookies'
cookies=dict(set_cookies='working')
response=requests.get(url,cookies=cookies)
print(response.text)
print("+++++++++++++++++++++++++++++++++")

response=requests.get('http://github.com',allow_redirects=False)
print(response.status_code)




