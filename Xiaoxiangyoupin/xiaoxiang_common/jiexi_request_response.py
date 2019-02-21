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
    result = {'heads':
                  {'code': 200, 'message': 'success'},
              'body': {'data':
                           [{'groupName': '我的服务', 'typeNum': 2, 'childs':
                               [{'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/144x156_863270671025704960.png', 'gotoUrl': 'bsdlks://polymerShopCar/h5-dev.xiaoxiangyoupin.com/polymerShopCar/', 'typeName': '淘宝订单', 'status': '1'},
                                {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/144x156_863272686904676352.png', 'gotoUrl': 'bsd://xxyp/mine/coupon', 'typeName': '优惠券', 'status': '1'},
                                {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/144x156_863271348548407296.png', 'gotoUrl': 'https://cdn.xiaoxiangyoupin.com/dev/activity/huiyuan/index.html', 'typeName': '新人专享', 'status': '1'},
                                {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/1125x180_890791791639400448.png', 'gotoUrl': 'bsd://xxyp/mine/yuyue', 'typeName': '我的预约', 'status': '1'},
                                {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/144x156_863271593269268480.png', 'gotoUrl': 'bsd://xxyp/mine/accountManagement', 'typeName': '账户管理', 'status': '1'},
                                {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/144x156_863271632221769728.png', 'gotoUrl': 'bsdlk://cdn.basestonedata.com/app/service/cs1.html', 'typeName': '联系客服', 'status': '1'},
                                {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/144x156_863483933306654720.png', 'gotoUrl': 'bsdlk://cdn.basestonedata.com/app/service/qa.html', 'typeName': '常见问题', 'status': '1'},
                                {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/144x156_863272231747194880.png', 'gotoUrl': 'bsd://xxyp/mine/setting', 'typeName': '设置', 'status': '1'}]},
                                {'groupName': '福利', 'typeNum': 1,
                                'childs': [{'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/420x225_865091470636355584.png', 'gotoUrl': 'bsdlks://cdn.basestonedata.com/dev/lovercard-v2/index.html', 'typeName': '情侣卡', 'status': '1'}, {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/420x225_871219373715492864.png', 'gotoUrl': 'bsdlks://cdn.basestonedata.com/dev/asset_authorization/index.html', 'typeName': '资产证明授权', 'status': '1'},
                                 {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/420x225_865091106432356352.png', 'gotoUrl': 'bsdlks://cdn.basestonedata.com/dev/facecard/index.html', 'typeName': '小象颜值卡', 'status': '1'}, {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/280x150_865091842742423552.png', 'gotoUrl': 'bsdlk://cdn.xiaoxiangyoupin.com/dev/baihua2nd/index.html',
                                  'typeName': '邀请好友', 'status': '1'}]}, {'groupName': '借款','typeNum': 3, 'childs': [{'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/400x220_865366436464300032.png', 'gotoUrl': 'bsd://xxyp/loan/creditCard', 'typeName': '小象钱包', 'status': '1'}, {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/600x330_865365155536441344.png', 'gotoUrl': 'bsd://xxyp/loan/cashLoan', 'typeName': '小象金融', 'status': '1'}, {'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/540x300_1536052071509.png', 'gotoUrl': 'bsd://goodsList?bannerId=762', 'typeName': '测试福利', 'status': '1'}, {'imgUrl': 'https://dev.xiaoxiangyoupin.com/img/255x258_867486807267217408.png', 'gotoUrl': 'bsdlks://baidu.com', 'typeName': '某某福利', 'status': '1'}]}, {'groupName': '商城', 'typeNum': 4, 'childs': [{'imgUrl': 'http://cdn.xiaoxiangyoupin.com/dev/upload/manager/540x300_1536051903949.png', 'gotoUrl': 'bsd://goodsList?bannerId=762', 'typeName': '减压哈哈', 'status': '1'}]}]}}
    print(type(result))
    jiexi_json1(result,"groupName")