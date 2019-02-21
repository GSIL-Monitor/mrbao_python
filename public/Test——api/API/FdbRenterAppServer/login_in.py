# coding: UTF-8
import json
import logging

import requests

from common.CanShuPaiXu1 import Paixu
from common.data_shuju import DB

LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='API.log',level=logging.INFO,format=LOG_FORMAT)
class Login(object):
    #登录验证
    def __init__(self):
        self.houseId = []  # 获取房源id
        self.userID = ''
        #self.token = 'QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA='
    def send_verifcode(self, mobile):
        # 发送验证码
        base_url = "http://118.178.242.96:8371/FffdAppServer/user/send_verifycode.rest" # f发送验证码   请求参数"mobile": "15921135537"
        url='http://118.178.242.96:8103/user/send_verifycode.rest	'
        logging.info('huo qu url :%s' % base_url)
        try:
            dict1 = {"mobile": mobile}
            json_dict = json.dumps(dict1, ensure_ascii=False)
            A = Paixu()
            B = A.get_canshu(dict1, A.pingguo)
            header = B[1]  # 获取请求头信息
            # C=A.get_time()#获取时间戳
            logging.info("now header is %s" % header)
            response = requests.post(url, headers=header, data=json_dict)
            print(response.json())
            return response.json()
        except:
            cuoWuXinXi = 'qing zai one miute hou zai dian ji '
            logging.info(cuoWuXinXi)

    def login_in(self, mobile):
        # 登录
        url1 = 'http://118.178.242.96:8371/FffdAppServer/user/login.rest'  # 登录验证  请求参数 "mobile": "15921135537","verifyCode": "2345"
        url2='http://118.178.242.96:8103/user/login.rest'
        logging.info('current url is %s' % url2)
        api = Login()
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
        response = requests.post(url2, headers=header, data=json_dict)
        #print(response.json())
        data_content = response.json()
        ticket = data_content['data']['ticket']  # 获取ticket
        userID = data_content['data']['userId']  # 获取userId
        hximUserId = data_content['data']['hximUserId']
        virtualPhone = data_content['data']['virtualPhone']  # 获取小号
        self.token = ticket  # 获取ticket
        self.userID = userID  # 获取用户id
        self.virtualPhone = virtualPhone  # 获取小号
        print(self.token)
        return response.json(),ticket,userID, hximUserId, virtualPhone
A=Login()
A.login_in('18621509417')