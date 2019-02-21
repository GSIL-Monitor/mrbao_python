# coding: UTF-8
import json
import logging

import requests

from CanShuPaiXu1 import Paixu

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='API.log',level=logging.INFO, format=LOG_FORMAT)
class FangYuan(object):
    def __init__(self):
        self.token = ""
        self.houseId = []
        self.rentId = []
    def publish_rent(self,A):
        #14、发布整租 [v1.4修改]>
        #请求参数{"subEstateId":"子划分ID","buildingId":"楼栋ID","building":"楼栋名称","room":"室号","bedroomSum":"室","livingRoomSum":"厅","wcSum":"卫","spaceArea":"面积","price":"租金","floor":"当前楼层","layers":"总楼层","decorateType":"装修等级","ventilation":"朝向","memo":"描述","houseEquipment":"房屋配置，多个用英文逗号隔开"，"payMethod":"付款方式","housePlan":"户型图"}
        #decorateType 装修等级：1、毛坯；2、简装；3、精装；4、豪装      ventilation 朝向：1、东，2、西，3、南，4、北，5、南北，6、东西，7、东南，8、东北，9、西南，10、西北
        #房屋配置：1、床，2、沙发，3、洗衣机，4、空调，5、电视，6、冰箱，7、热水器，8、宽带，9、可做饭，10、阳台，11、独立卫生间
        #payMethod 付款方式：1、押一付一，2、押一付三，3、半年付，4、年付，5、面议
        url = 'http://118.178.242.96:8371/FffdAppServer/house/publish_rent.rest'
        logging.info('current url is %s' % url)
        dict1 = {A}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def publish_joint_rent_house(self, c):
        # 55、发布合租房子信息[v1.4修改]
        url = 'http://118.178.242.96:8371/FffdAppServer/house/publish_joint_rent_house.rest'
        logging.info('current url is %s' % url)
        dict1 = {c}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def publish_joint_rent_room(self, B):
        # 56、发布合租房间信息[v1.4修改]
        # 请求参数{ "houseId":"房子ID","roomType":1,"spaceArea":"面积","ventilation":"朝向","genderRequirement":1,"payMethod":"付款方式","price":"租金","houseEquipment":"房屋配置，多个用英文逗号隔开","roomName":"房间备注名"}
        # roomType 房间类型：1、主卧，2、次卧
        # ventilation 朝向：1、东，2、西，3、南，4、北，5、南北，6、东西，7、东南，8、东北，9、西南，10、西北
        # decorateType 装修等级：1、毛坯；2、简装；3、精装；4、豪装
        # Integer genderRequirement 性别要求：1、男女不限，2、限女生，3、限男生，4、限夫妻
        # Integer payMethod 付款方式：1、押一付一，2、押一付三，3、半年付，4、年付，5、面议
        # 房屋配置：1、床，2、沙发，3、洗衣机，4、空调，5、电视，6、冰箱，7、热水器，8、宽带，9、可做饭，10、阳台，11、独立卫生间
        url = 'http://118.178.242.96:8371/FffdAppServer/house/publish_joint_rent_room.rest'
        logging.info('current url is %s' % url)
        dict1 = {B}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def check_house_info(self,subEstateId,buildingId,building,room):
        #54、检查房子信息 >
        # 请求参数{"subEstateId":"子划分ID","buildingId":"楼栋ID","building":"楼栋名称","room":"室号"}
        url = 'http://118.178.242.96:8371/FffdAppServer/house/publish_rent.rest'
        logging.info('current url is %s' % url)
        dict1 = {"subEstateId":subEstateId,"buildingId":buildingId,"building":building,"room":room}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def get_last_house(self,rentType,subEstateId,buildingId,room):
        #63、获得最后录入或复制的房屋信息[v1.4新增]                       rentType Integer 类型：1、整租，3、合租
        url = 'http://118.178.242.96:8371/FffdAppServer/house/publish_rent.rest'
        logging.info('current url is %s' % url)
        dict1 = {"rentType":rentType,"subEstateId":subEstateId,"buildingId":buildingId,"room":room}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def copy_house(self,houseResourceId,rentType):
        #64、复制房屋信息[v1.4新增]
        #houseResourceId;//房源列表中的id，房间id
        #rentType;//房源列表中的1整租，3合租
        url = 'http://118.178.242.96:8371/FffdAppServer/house/copy_house.rest'
        logging.info('current url is %s' % url)
        dict1 = {"houseResourceId":houseResourceId,"rentType":rentType}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getUserHouseNum(self):
        #70、获取房东房源数量 >
        url = 'http://118.178.242.96:8371/FffdAppServer/house/getUserHouseNum.rest'
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

    def myHouseCount(self):
        # 81、我的房子统计 >
        url = 'http://118.178.242.96:8371/FffdAppServer/house/myHouseCount.rest'
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

    def listUserContact(self,userID):
        #22获取用户个人详情   请求参数{"userId ": 1}
        url = 'http://118.178.242.96:8371/FffdAppServer/user/getUserInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"userId": userID }
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def add_hxim_friend(self, userHxId, agentHxId):
        # 62、新增环信好友关系 >
        # 请求参数{"userHxId":"房东环信ID","agentHxId":"经纪人环信ID"}
        url = 'http://118.178.242.96:8371/FffdAppServer/user/add_hxim_friend.rest'
        logging.info('current url is %s' % url)
        dict1 = {"userHxId": userHxId, "agentHxId": agentHxId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getVirtualMobileInfo(self,userID):
        #获取小号详情   请求参数{"userId ": 1}
        url = 'http://118.178.242.96:8371/FffdAppServer/user/getVirtualMobileInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"userId": userID}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getMyInfo(self):
        #获取"我的"信息
        url = 'http://118.178.242.96:8371/FffdAppServer/userContact/getMyInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"":"" }
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def downHouse(self,id):
        #同步下架房源  请求参数{"id":20,"bizType":1,"channelTagListStr":"1,2,3"}     id;//房源列表中的id      bizType;//1出租，2出售     channelTagListStr;//渠道标识：1、百姓网，2、安居客，3、房多多
        url = 'http://118.178.242.96:8371/FffdAppServer/house/downHouse.rest'
        logging.info('current url is %s' % url)
        dict1 = {"id":id,"bizType":1,"channelTagListStr":"1,2,3"}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def get_task_count(self,id):
        #50、获得房源进行中任务数 >
        #请求参数 {"id": 111,"bizType": 1} id 出租ID或出售ID   bizType 类型：1、出租；2、出售
        url = 'http://118.178.242.96:8371/FffdAppServer/channel/account_state_check.rest'
        logging.info('current url is %s' % url)
        dict1 = {"id": id,"bizType": 1,"channelTag":"3"}
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