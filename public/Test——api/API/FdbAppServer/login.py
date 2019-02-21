# coding: UTF-8
import json
import logging

import requests

from CanShuPaiXu1 import Paixu
from common.data_shuju import DB


class Login_in(object):
    #登录验证
    def __init__(self):
        self.houseId = []  # 获取房源id
        self.userID = ''
        self.token = 'QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA='
    def send_verifcode(self, mobile):
        # 发送验证码
        base_url = "http://118.178.242.96:8371/FffdAppServer/user/send_verifycode.rest"  # f发送验证码   请求参数"mobile": "15921135537"
        logging.info('huo qu url :%s' % base_url)
        try:
            dict1 = {"mobile": mobile}
            json_dict = json.dumps(dict1, ensure_ascii=False)
            A = Paixu()
            B = A.get_canshu(dict1,'pingguo')
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
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]  # 获取请求头头信息
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
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

    def bindIdentity(self,realName,idCard):
        #88、提交实名认证（v1.0）
        #realName;//真实姓名
        #idCard;//身份证号
        url = 'http://118.178.242.96:8371/FffdAppServer/account/bindIdentity.rest'
        logging.info('current url is %s' % url)
        dict1 = {"realName": realName,"idCard":idCard}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return response.json()

    def getSupportBankList(self):
        #86、获取支持银行列表（v1.0）
        url = 'http://118.178.242.96:8371/FffdAppServer/account/getSupportBankList.rest'
        logging.info('current url is %s' % url)
        dict1 = {"": ""}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return response.json(),response.status_code

    def getCardBin(self,bankCardNo):
        #87、获取银行卡开户行（v1.0）
        url = 'http://118.178.242.96:8371/FffdAppServer/account/getCardBin.rest'
        logging.info('current url is %s' % url)
        dict1 = {"bankCardNo":bankCardNo}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return response.json(),response.status_code

    def bindBankcard(self,bankCardNo):
        #89、提交绑定银行卡（v1.0）
        #bankcardNo;//银行卡号      bankCode;//银行编号       bankName;//银行名称        mobile;//银行卡预留手机号         cardType;//CC=贷记卡，DC=借记卡，SCC=准贷记卡，PC=预付
        url = 'http://118.178.242.96:8371/FffdAppServer/account/getCardBin.rest'
        logging.info('current url is %s' % url)
        dict1 = {"bankCardNo": bankCardNo,"bankCode":"sfsf","bankName": "招商银行","mobile":"18717777777","cardType":"DC",}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def queryTradeInfo(self,orderNo,bizType):
        #98、获得交易记录详情[v1.0新增]
        url = 'http://118.178.242.96:8371/FffdAppServer/account/queryTradeInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"orderNo":orderNo,"bizType":bizType}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def  realname_register(self,name,idCard):
        #3实名登记
        url = 'http://118.178.242.96:8371/FffdAppServer/user/realname_register.rest'
        logging.info('current url is %s' % url)
        dict1 = { "realName": name,"idCard": idCard}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        json_dict.encode('utf-8').decode('latin1')
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return response.json()
D = Login_in()
#D.getCardBin("4392268328103388")
print(D.login_in("18621512473"))
#D.login_in("18621512473")