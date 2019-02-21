#-*-coding:utf-8-*-
import json
import logging
list_A=[]
with open('ip_list.json','r',encoding='utf-8') as f:
    a=f.readlines()
    for line in a:
        print(line.strip())
    #print(json.load(f))
    #print(a)
    #for x in json.load(fp=f):
        #list_A.append(json.load(fp=f)['ip_address'][0])
        #list_A.append(json.load(fp=f)['ip_port'][0])
        ##list_A.append(json.load(fp=f)['ip_type'][0])
        #list_A.append(json.load(fp=f)['ip_time'][0])
#print(list_A)
