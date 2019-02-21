# -*- coding: UTF-8 -*-
import json
import jsonpath
def jiexi_data(result_data,key_name):
    '''
    :param result_data: 
    :param key_name: key值
    :return: 
    '''
    if isinstance(result_data,dict):
        key=result_data.keys()#获取result_data key
        if 'heads'and'body' in key:
            heads=result_data['heads']
            code=heads['code']#获取code值
            message=heads['message']#获取message
            body = result_data['body']
            key_zhi = body[key_name]
            return code,message,key_zhi
        else:
            pass

def jiexi_json(result_data,key_name):#解析接口返回值
    '''
    :param result_data: 
    :param key_name: key值
    :return: 
    '''
    global value_name
    t={}
    if isinstance(result_data,list):
        for elemnet in result_data:
            jiexi_json(elemnet,key_name)
    elif isinstance(result_data,dict):
        key = result_data.keys()  # 获取result_data key
        if key_name in key:#判断key_name是否在key集合中
            value_name=result_data[key_name]#在就赋值给value_name
            #print(value_name)
            t['value']=value_name
            #print(value_name)
        else:#判断key_name是否在key集合中
            for x_key in key:
                 jiexi_json(result_data[x_key], key_name)#执行递归


            '''for x_key in key:#不在就遍历key值
                if isinstance(result_data[x_key],list):#判断result[x_key]是否是list
                    for elemnet in result_data[x_key]:#是就遍历list中的值
                        jiexi_json(elemnet, key_name)#在次进行递归
                elif isinstance(result_data[x_key],dict):#判断result[x_key]是否是dict
                    key=result_data[x_key]#获取key
                    if key_name in key:#判断key是否在集合中
                        value_name = result_data[key_name]#在就把velue值赋予value_name
                        print(value_name)
                        '''

#解析接口data并且与输入的Value做对不
def jiexi_data_duibi(result_data,key_name,value_name):
    pass
def jiexi_json1(result_data,key_name):#解析接口返回值
    '''
    :param result_data: 
    :param key_name: key值
    :return: 
    '''
    global value_name
    if isinstance(result_data,list):#判断类型是不是list
        for elemnet in result_data:
            jiexi_json(elemnet,key_name)
    elif isinstance(result_data,dict):#判断类型是不是dict
        key = result_data.keys() # 获取result_data key
        print(key)
        if key_name in key:#判断key_name是否在key集合中
            value_name=result_data[key_name]#在就赋值给value_name
            print(value_name)
        else:#判断key_name是否在key集合中
            for x_key in key:
                 jiexi_json(result_data[x_key], key_name)#执行递归
    else:
        print('%s不知道是什么'%result_data)

if __name__ == '__main__':
    pass
