import requests
import json
import time

#r=requests.get('http://www.baidu.com/timeline.json')
'''r=requests.get('https://github.com/timeline.json')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
#print(r.content)
print(r.json())
dict={'key1':'value1','key2':'value2'}
i=requests.get('http://www.baidu.com',params=dict)
print(i.url)
print(i.content)
i={'key1':'value1','key2':'value2'}
r=requests.post('http://httpbin.org',data=i)
print(r.text)
url="http://127.0.0.1:8001/get_event_list/"
r=requests.get(url)               #get
a=requests.post(url)              #post
b=requests.put(url)#put
c=requests.delete(url)#delete
d=requests.head(url)#head
e=requests.options(url)#options
print(r.status_code)
print(r.url)
print(r.content)
print(a.content)
print(b.content)
print(c.content)
print(d.content)
print(e.content)
#r.raise_for_status()

#url="http://10.7.248.52:7777/house/getUserHouseNum.rest"
#r=requests.post(url)
#print(r.text)
#send_verifycode_url="http://10.7.248.63:7777/user/send_verifycode.rest"
#i={'mobile':'18501787063'}
#r=requests.post(send_verifycode_url,data=i)
#print(r.status_code)
#print(r.json())
#print(r.text)
response=requests.get("http://ww.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
print('--------------------')
print(response.content)
print(response.content.decode("utf-8"))
print("==================")
data={'name':'mrbao','age':2}
response=requests.get('http://httpbin.org/get',params=data)
#response=requests.get('http://httpbin.org/get?name=mrbao&age=23')
try:
    print(response.text)
except:
    print("run is false")
print("-----------------------------")
response=requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
print("------------------------------------------------------------")

data={
    "name":"baotao",
    "age":23
}
response=requests.post("http://httpbin.org/post/post",data=data)
print(response.text)
#print(json.loads(response.text))
#print(response.json())
print("--------------------")
response=requests.get("http://www.baidu.com")
if response.status_code==requests.codes.ok:
    print("Is Ok")
    print(response.content)

print("---------------------------")
#files={"files":open("git.jpeg","rb")}
#response=requests.post("http://httpbin.org/post",data=files)
#print(response.text)
response=requests.get("http://www.baidu.com")
print(response.cookies)
for key,value in response.cookies.items():
    print(key+"="+value)

print('------------------------------')
s=requests.session()
url="http://httpbin.org/cookies/set/sessioncookie/123456"
s.get(url)
responer=s.get("http://httpbin.org/cookies")
print(response.text)
print(response.cookies)'''
url="http://10.7.252.89:8888/getDoorBaseInfo.rest"
t=time.time()
print(t)
print(int(t))
print(int(round(t*1000)))
time1=int(round(t*1000))
doorId=76
para={'_t':time1,'doorId':doorId}
response=requests.post(url,data=para)
print(response.text)
print(response.status_code)
print(response.url)


