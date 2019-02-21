# coding: UTF-8
import json
import logging
import re

import requests

from CanShuPaiXu1 import Paixu

LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='API.log',level=logging.INFO,format=LOG_FORMAT)

class  FangYuan(object):
    def __init__(self):
        self.token="QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA="
        self.houseId=[]
        self.rentId=[]
        self.houseRoom=[]

    def request_(self,url,loc):
        json_dict=json.dumps(loc,ensure_ascii=False)
        A=Paixu()
        B=A.get_canshu('pingguo',loc)
        header=B[1]
        header['u_ticket']=self.token
        response=requests.post(url,header=header,data=json_dict)
        return response


    def myHouseContractCount(self):
        #首页代办事项
        url = 'http://118.178.242.96:8371/FffdAppServer/user/myHouseContractCount.rest	'
        logging.info('current url is %s' % url)
        dict1 = {"": ""}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1,'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        print(response.status_code)
        return response.json(), response.status_code

    def myHouseList1(self):
        #获取房源列表    header 需要加入'u_ticket'字段
        url='http://118.178.242.96:8371/FffdAppServer/house/myHouseList.rest'#发房小区列表搜索  请求参数{"pageSize":20,"offset":0}
        logging.info('current url is %s' % url)
        dict1={"pageSize":20,"offset":0,}
        json_dict=json.dumps(dict1,ensure_ascii=False)
        A=Paixu()
        B=A.get_canshu(dict1,'pingguo')
        header=B[1]
        header['u_ticket']=self.token
        logging.info("now header is %s" % header)
        response1=requests.post(url,headers=header,data=json_dict)
        content=response1.json()
        try:
            houseId=content['data']['rows']
            #print(houseId)
            for result in houseId:
                    #print(result['id'])#获取房源ID
                    if result['id']!=None and result['jointRentRoomModelList']!=None:
                        self.houseRoom.append(result['id'])#获取有房间的房源
            logging.info('有房间的房源为%s' % self.houseRoom)
        finally:
            print(content)
            return content,self.houseRoom

    def getJointRentHouseDetail(self,houseId):#n参数为了获取houseId
        # 71获取合租房子详情 请求参数{“houseId”:111}
        url='http://118.178.242.96:8371/FffdAppServer/house/getJointRentHouseDetail.rest'#71获取合租房子详情 请求参数{"houseId":111}   houseId;//房子id（我的房子列表中的id）
        logging.info('current url is %s' % url)
        dict1={"houseId":houseId}
        json_dict=json.dumps(dict1,ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket']=self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        content=response.json()
        houseStatus=content['data']['houseModel']
        status=re.compile("\'houseStatus\':(.*?),")
        status=status.findall(str(houseStatus))[0]
        status=int(status)
        if status==1:
            a='待审核(未申请装锁)'
            print('房源id为 %s 的门锁安装状态是 %s!'%(houseId,a))
        elif status==2:
            a = '审核中'
            print('房源id为 %s 的门锁安装状态是 %s!' % (houseId, a))
        elif status==3:
            a = '待装锁'
            print('房源id为 %s 的门锁安装状态是 %s!' % (houseId, a))
        elif status==4:
            a = '已装锁'
            print('房源id为 %s 的门锁安装状态是 %s!' % (houseId, a))
        else:
            print('')
        print(response.json())
        return  response.json(), response.status_code
    def getJointRentHouseDetail1(self,houseId):#n参数为了获取houseId
        #71获取合租房子详情 请求参数{“houseId”:111}
        url='http://118.178.242.96:8371/FffdAppServer/house/getJointRentHouseDetail.rest'#71获取合租房子详情 请求参数{"houseId":111}   houseId;//房子id（我的房子列表中的id）
        logging.info('current url is %s' % url)
        dict1={"houseId":houseId}
        json_dict=json.dumps(dict1,ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket']=self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return  response.json(), response.status_code

    def listJointRentRoom(self,n):
        # 72获取合租房间列表   请求参数{"houseId":111}
        url = 'http://118.178.242.96:8371/FffdAppServer/house/listJointRentRoom.rest'#72获取合租房间列表   请求参数{"houseId":111}
        logging.info('current url is %s' % url)
        dict1 = {"houseId": n}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        try:
            content=response.json()
            rentId=content['data']['jointRentRoomModelList']#获取房屋详情内容
            for result in rentId:#
                self.rentId.append(result['id'])#获取房间ID
                return result['id']
            logging.info('rentId为%s'%self.rentId)
        finally:
            print(response.json())
            return response.json()

    def listJointRentRoom1(self, n):
        # 72获取合租房间列表   请求参数{"houseId":111}
        url = 'http://118.178.242.96:8371/FffdAppServer/house/listJointRentRoom.rest'  # 72获取合租房间列表   请求参数{"houseId":111}
        logging.info('current url is %s' % url)
        dict1 = {"houseId": n}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return response.json(),response.status_code

    def houseDetail(self,n):#参数为房间id
        #41获取房间详情
        '''
        :param n: 房间id
        :return: 门锁电量,门锁id,门锁联网状态,门锁联网信号
        '''
        url = 'http://118.178.242.96:8371/FffdAppServer/house/houseDetail.rest'#//房源列表中的id     bizType;//房源列表中的bizType 1出租，2出售
        logging.info('current url is %s' % url)
        dict1 = {"id": n,"bizType":1}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B=A.get_canshu(dict1,'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        result1=response.json()
        doorInfo=result1['data']['house']#获取门锁消息
        if doorInfo!=None:
            dianliang=doorInfo['doorLockInfo']['electric']#获取门锁电量
            doorId=doorInfo['doorLockInfo']['id']#获取门锁id
            zhuangyai=doorInfo['doorLockInfo']['success']#门锁联网状态
            xinhao=doorInfo['doorLockInfo']['rssi']#门锁联网信号
            fangjian=doorInfo['roomNoStr']
            logging.info('房间号是%s 的门锁id为%s,联网状态为%s,电量值为%s,'%(n,doorId,zhuangyai,dianliang))
            return dianliang, doorId, zhuangyai, xinhao, fangjian
        else:
            logging.info('房间号是%s 的房间还没有装门锁！'%self.rentId[n])
        print(response.json())

    def houseDetail1(self, n):  # 参数为房间id
        # 41获取房间详情
        '''
        :param n: 房间id
        :return: 门锁电量,门锁id,门锁联网状态,门锁联网信号
        '''
        url = 'http://118.178.242.96:8371/FffdAppServer/house/houseDetail.rest'  # //房源列表中的id     bizType;//房源列表中的bizType 1出租，2出售
        logging.info('current url is %s' % url)
        dict1 = {"id": n, "bizType": 1}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return response.json(), response.status_code

    def myHouseEstate(self):
        #82、我的房子小区列表V1.2 >
        url = 'http://118.178.242.96:8371/FffdAppServer/house/myHouseEstate.rest'
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

    def getDoorBaseInfo(self,doorId):
        #120、获取门锁基本信息(v1.0新增)  "doorId":11，门锁ID
        url = 'http://118.178.242.96:8371/FffdAppServer/door/getDoorBaseInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"doorId":doorId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return response.json(), response.status_code

    def listDoorTempPWD(self,doorId,authUserId,source):
        #121、获取门锁临时密码列表(v1.0新增)
        #请求参数 "doorId":1,门锁ID，"authUserId":授权人ID, "source":来源 1.房东 2.租客
        url = 'http://118.178.242.96:8371/FffdAppServer/door/listDoorTempPWD.rest'
        logging.info('current url is %s' % url)
        dict1 = {"doorId":doorId,"authUserId":authUserId, "source":source}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return response.json(), response.status_code

    def listDoorOpen(self,doorId,authUserId,startTime,endTime):
        #122、获取门锁开门记录(v1.0新增)
        #请求参数"doorId":1，"authUserId":1, "startTime":"开始时间 yyyy-MM-dd","endTime":"结束时间 yyyy-MM-dd"
        url = 'http://118.178.242.96:8371/FffdAppServer/door/listDoorTempPWD.rest'
        logging.info('current url is %s' % url)
        dict1 = {"doorId": doorId, "authUserId": authUserId, "startTime":startTime,"endTime":endTime }
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
        return response.json(), response.status_code

    def updateDoorPWD(self,doorId,authUserId,pwd,source):
        #Xiaoxiangyoupin、修改门锁密码(v1.0新增)
        #请求参数   String pwd密码
        url = 'http://118.178.242.96:8371/FffdAppServer/door/updateDoorPWD.rest'
        dict1 = {"doorId": doorId, "authUserId": authUserId, "pwd": pwd, "source": source}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def addDoorPWD(self,A):
        #124、创建门锁密码(v1.0新增)
        #请求参数  "doorId":门锁ID,   "authUserId":授权人ID,  "name":"被授权人姓名",   "mobile":"mobile",    "pwd":"密码",    "type":授权类型：1、房东授权；2、租客授权；3、临时密码授权,
        #"effectiveTime":""生效时间 - 只有临时密码授权可用 yyyy-MM-dd HH:mm:ss,   "expirationTime":" 生效时间 - 只有临时密码授权可用 yyyy-MM-dd HH:mm:ss",
        #"doorType":门锁类型：1、大门；2、内门    ,       source来源 1房东 2租客       times;次数
        url = 'http://118.178.242.96:8371/FffdAppServer/door/addDoorPWD.rest'
        dict1 = {A}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def delDoorPWD(self,doorId,authUserId,doorType,authId):
        #125、删除门锁密码(v1.0新增)
        # 请求参数 {"doorId":授权id,"authUserId":门锁ID,"doorType":授权人ID,"authId":门锁类型：1、大门；2、内门}
        url = 'http://118.178.242.96:8371/FffdAppServer/door/delDoorPWD.rest'
        dict1 =  {"doorId":doorId,"authUserId":authUserId,"doorType":doorType,"authId":authId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getNewDoorPWD(self,doorId,authUserId):
        #126、获取新密码(v1.0新增)
        #  请求参数{"doorId":门锁ID,"authUserId":授权人ID}
        url = 'http://118.178.242.96:8371/FffdAppServer/door/getNewDoorPWD.rest'
        dict1 = {"doorId": doorId, "authUserId": authUserId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def listDoorInfo(self,houseId,authUserId):
        #127、获取房源门锁列表(v1.0新增)
        #请求参数{"houseId":1,"rentIdList":[1,1]}   房子id  出租房源id集合
        url = 'http://118.178.242.96:8371/FffdAppServer/door/listDoorInfo.rest'
        dict1 = {"houseId": houseId, "authUserId": authUserId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def addDoor(self,houseId,rentID,doorType,roomNo):
        #128、新增门锁(v1.0新增)
        #请求参数{ "houseId":房源id,"rentID":出租房源id,"doorType":门锁类型：1、大门；2、内门,"roomNo":"房间单间号 大门为00"}
        url = 'http://118.178.242.96:8371/FffdAppServer/door/addDoor.rest'
        dict1 = {"houseId": houseId, "rentID": rentID,"doorType":doorType,"roomNo":roomNo}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def sendDoorPWDMessage(self,authId,moobile):
        #129、发送短信(v1.0新增)
        #请求参数 {"authId":授权id,"moobile":"手机号"}
        url = 'http://118.178.242.96:8371/FffdAppServer/door/sendDoorPWDMessage.rest'
        dict1 = {"authId": authId, "moobile": moobile}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def applyUrgentTempPWD(self,doorId):
        #130、申请紧急临时密码(v1.1新增)
        # 请求参数 {"authId":授权id,"userId":1,"source":1}
        url = 'http://118.178.242.96:8371/FffdAppServer/door/applyUrgentTempPWD.rest'
        dict1 = {"doorId": doorId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def openDoor(self,doorId):
        #131、一键开门(v1.1新增)
        url = 'http://118.178.242.96:8371/FffdAppServer/door/openDoor.rest'
        dict1 = {"doorId": doorId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def addDoorFeedback(self,doorId):
        #133、新增门锁问题反馈(v1.1新增)
        # 请求参数 {""doorId":1,"memo":"","doorDesc":"","imgKeyStr":"图片，逗号隔开"}
        url = 'http://118.178.242.96:8371/FffdAppServer/door/addDoorFeedback.rest'
        dict1 = {"doorId": doorId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def addEstateFeedback(self,memo):
        #134、新增小区问题反馈
        # 请求参数{"memo":" 问题描述","imgKeyStr":"图片，逗号隔开"}
        url = 'http://118.178.242.96:8371/FffdAppServer/door/addEstateFeedback.rest'
        dict1 = {"memo": memo}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def removeHouse(self,houseId):
        #136、删除房屋(v1.3新增)
        url = 'http://118.178.242.96:8371/FffdAppServer/house/removeHouse.rest'
        dict1 = {"houseId":houseId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getConfigInfo(self):
        #142、获取当前配置信息
        url = 'http://118.178.242.96:8371/FffdAppServer/system/getConfigInfo.rest'
        dict1 = {"":""}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def checkUserPerms(self,B):
        #143、检查用户是否有门锁权限(v1.1新增)
        #请求参数{"houseId":用于查找大门，非必填,"rentId":房间ID}
        url = 'http://118.178.242.96:8371/FffdAppServer/system/getConfigInfo.rest'
        dict1 = {B}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, 'pingguo')
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())
D=FangYuan()
#D.getJointRentHouseDetail1(2+00)
#D.listDoorOpen(10191,'','2018-04-02','2018-04-010')
#D.myHouseList1()
#D.getJointRentHouseDetail(1408)
D.myHouseContractCount()
