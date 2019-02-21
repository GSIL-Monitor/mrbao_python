# coding: UTF-8
import json
import logging
import re

import requests

from CanShuPaiXu1 import Paixu
from common.data_shuju import DB

LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='API.log',level=logging.INFO,format=LOG_FORMAT)

class Login_in(object):
    #登录验证
    def __init__(self):
        self.houseId = []  # 获取房源id
        self.userID = ''
    def send_verifcode(self, mobile):
        # 发送验证码
        base_url = "http://118.178.242.96:8371/FffdAppServer/user/send_verifycode.rest"  # f发送验证码   请求参数"mobile": "15921135537"
        logging.info('huo qu url :%s' % base_url)
        try:
            dict1 = {"mobile": mobile}
            json_dict = json.dumps(dict1, ensure_ascii=False)
            A = Paixu()
            B = A.get_canshu(dict1, A.pingguo)
            header = B[1]  # 获取请求头信息
            # C=A.get_time()#获取时间戳
            logging.info("now header is %s" % header)
            response = requests.post(base_url, headers=header, data=json_dict)
            # print(response.json())
            return response.json()
        except:
            cuoWuXinXi = 'qing zai one miute hou zai dian ji '
            logging.info(cuoWuXinXi)

    def login_in(self, mobile):
        # 登录
        url = 'http://118.178.242.96:8371/FffdAppServer/user/login.rest'  # 登录验证  请求参数 "mobile": "15921135537","verifyCode": "2345"
        logging.info('current url is %s' % url)
        api = Login_in()
        api.send_verifcode(mobile)  # 发送验证码
        db = DB()
        yanzhnegma = db.get_YanZhengMa(mobile)  # 获取验证码
        logging.info('yanZhengMa is %s ' % yanzhnegma)
        dict1 = {'mobile': mobile, 'verifyCode': yanzhnegma}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]  # 获取请求头头信息
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        data_content = response.json()
        ticket = data_content['data']['ticket']  # 获取ticket
        userID = data_content['data']['userId']  # 获取userId
        hximUserId = data_content['data']['hximUserId']
        virtualPhone = data_content['data']['virtualPhone']  # 获取小号
        self.token = ticket  # 获取ticket
        self.userID = userID  # 获取用户id
        self.virtualPhone = virtualPhone  # 获取小号
        print(self.token)
        return ticket,userID, hximUserId, virtualPhone

    def queryEstate(self, key):#key //小区关键词
        # 发房小区列表搜索
        url = 'http://118.178.242.96:8371/FffdAppServer/house/queryEstate.rest'  # 请求参数{"cityId":2,"keyword":"上大路"}cityId; //城市id，默认2上海， keyword; //小区关键词
        logging.info('current url is %s' % url)
        dict1 = {"cityId": 2, "keyword": key}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        try:
            result=response.json()
            estateList=result['data']['estateList']
            if estateList!=None:
                estateId=re.compile("\'estateId\': (.*?)")
                estateId=estateId.findall(str(estateList))#获取小区ID
                return estateId  # 返回小区ID
            else:
                print('未获取到信息')
        finally:
            print(response.json())

    def querySubEstates(self,estateId):#estateId; //小区ID
        #获取小区子划分
        url = 'http://118.178.242.96:8371/FffdAppServer/house/querySubEstates.rest'
        logging.info('current url is %s' % url)
        dict1 = {"estateId":estateId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        result=response.json()
        try:
            subEstateList=result['data']['subEstateList']
            if subEstateList!=None:
                subEstateId=re.compile("\'subEstateId\': (.*?)")#获取子划分id
                subEstateId=subEstateId.findall(str(subEstateList))
                return subEstateId
            else:
                print('未获取到信息')
        finally:
            print(response.json())

    def getBuildingInfo(self,subEstateId):#subEstateId//子划分id
        #获取子划分楼栋号列表
        url = 'http://118.178.242.96:8371/FffdAppServer/house/getBuildingInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"subEstateId":subEstateId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())