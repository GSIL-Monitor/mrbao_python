# coding: UTF-8
import json
import logging

import requests

from CanShuPaiXu1 import Paixu

LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='API.log',level=logging.INFO,format=LOG_FORMAT)

class Login_in(object):
    #登录验证
    def __init__(self):
        self.houseId = []  # 获取房源id
        self.userID = ''
        self.token = 'QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA='
    def channel_list(self):
        # 获得账户各平台注册情况
        url = 'http://118.178.242.96:8371/FffdAppServer/user/channel_list.rest'
        logging.info('current url is %s' % url)
        dict1 = {"": ""}  # 请求参数为空
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def  account_reg(self,channelTag,account):
        #渠道平台账户注册
        url = 'http://118.178.242.96:8371/FffdAppServer/channel/account_reg.rest'#channelTag 渠道标识：1、百姓网，2、安居客，3、房多多，4、赴集，5、豆瓣，6、五八,account 账号(小号)
        logging.info('current url is %s' % url)
        dict1 = { "channelTag":channelTag,"account":account}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        result=response.json()
        regJobId=result["data"]["regJobId"]
        print(response.json())
        return regJobId

    def account_reg_check(self,regJobId):
        #渠道平台账户注册检查
        url = 'http://118.178.242.96:8371/FffdAppServer/channel/account_reg_check.rest'
        logging.info('current url is %s' % url)
        dict1 = { "regJobId":regJobId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def account_state_check(self,channelTag,account):
        #渠道平台账户注册
        #channelTag 渠道标识：1、百姓网，2、安居客，3、房多多，4、赴集，5、豆瓣，6、五八
        #account 账号
        url = 'http://118.178.242.96:8371/FffdAppServer/channel/account_state_check.rest'
        logging.info('current url is %s' % url)
        dict1 = {"channelTag":channelTag,"account":account}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def account_login(self,account,channelTag):
        #51、渠道平台账户登录[v1.3修改]
        #请求参数{"channelTag":"渠道标识","account":"账号"}  channelTag 渠道标识：1、百姓网，2、安居客，3、房多多
        url = 'http://118.178.242.96:8371/FffdAppServer/channel/account_login.rest'
        logging.info('current url is %s' % url)
        dict1 = {"account":account, "channelTag": channelTag}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def h5_urls(self):
        #61、获取H5对应的路径 >
        url = 'http://118.178.242.96:8371/FffdAppServer/develop/h5_urls.rest'
        logging.info('current url is %s' % url)
        dict1 = {"": ""}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def channel_list1(self,Id):
        #获得房源同步平台情况   请求参数{ "bizType":1,"id":"出售ID或出租ID","noPublishChannel":1}
        #bizType 1、出租；2、出售             noPublishChannel 0、获取已发布过的平台；1、获取所有平台
        url = 'http://118.178.242.96:8371/FffdAppServer/house/publish_rent.rest'
        logging.info('current url is %s' % url)
        dict1 = {"id":Id,"bizType":1,"noPublishChannel":1}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def updateDND(self, userID, startTime, endTime):
        # 更新免打扰模式  请求参数{"userId": 111,"startTime":"开始时间","endTime":"结束时间","type":1}
        # type;//0 关闭 1 开启
        url = 'http://118.178.242.96:8371/FffdAppServer/user/getVirtualMobileInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"userId": userID, "startTime": startTime, endTime: "结束时间", "type": 1}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getDNDInfo(self):
        #获取免打扰详情
        url = 'http://118.178.242.96:8371/FffdAppServer/userContact/getDNDInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"":""}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def checkIdentity(self, idCard):
        # 146、校验身份证(v1.1新增)
        # 请求参数{ "idCard":"320xxx",}
        url = 'http://118.178.242.96:8371/FffdAppServer/system/getConfigInfo.rest'
        dict1 = {"idCard": idCard}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def allot_xphone(self, bizType, id, channelTag):
        # 160、分配渠道小号 [v1.3新增]
        # 请求参数{"bizType":1、出租；2、出售, "id":"出售ID或出租ID","channelTag":"1百姓网 2安居客 3房多多 4赶集 5豆瓣 6五八 7爱屋吉屋 8嗨住 9一楼租房"}
        url = 'http://118.178.242.96:8371/FffdAppServer/user/allot_xphone.rest'
        dict1 = {"bizType": bizType, "id": id, "channelTag": channelTag}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def channel_group_list(self, bizType, houseRentId):
        # 161、获得房源同步平台情况 小号分组详情 [v1.3新增]
        # 请求参数{"bizType":1、出租；2、出售, "houseRentId":"出租ID",}
        url = 'http://118.178.242.96:8371/FffdAppServer/user/allot_xphone.rest'
        dict1 = {"bizType": bizType, "houseRentId": houseRentId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def rentHouseList4ff(self):
        # 162、获取待发布一楼租房列表 <V1.3新增>
        url = 'http://118.178.242.96:8371/FffdAppServer/house/rentHouseList4ff.rest'
        dict1 = {"": ""}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def publishRentHouseToff(self, rentIds):
        # 163、发布到一楼租房 <V1.3新增>
        # 请求参数{"rentIds":"1,2,3",}
        url = 'http://118.178.242.96:8371/FffdAppServer/house/publishRentHouseToff.rest'
        dict1 = {"rentIds": rentIds}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def addAssistant(self, name, mobile):
        # 170、添加助理账号 v1.3新增 >
        # 请求参数{}"name":"姓名","mobile":"手机号"
        url = 'http://118.178.242.96:8371/FffdAppServer/user/addAssistant.rest'
        dict1 = {"name": name, "mobile": mobile}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def delAssistant(self, userId):
        # 171、删除助理账号 v1.3新增 >
        # 请求参数{"userId":1}
        url = 'http://118.178.242.96:8371/FffdAppServer/user/delAssistant.rest'
        dict1 = {"userId": userId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getAssistantList(self):
        # 172、获取全部助理账号列表 >
        url = 'http://118.178.242.96:8371/FffdAppServer/user/getAssistantList.rest'
        dict1 = {"": ""}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getOrderList(self):
        # 176、房东年付订单列表[v1.3新增]
        url = 'http://118.178.242.96:8371/FffdAppServer/fdnf/getOrderList.rest'
        dict1 = {"": ""}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getOrderDetail(self):
        # 177、房东年付订单详情[v1.3新增]
        # 请求参数{}
        url = 'http://118.178.242.96:8371/FffdAppServer/fdnf/getOrderDetail.rest'
        dict1 = {"": ""}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())


