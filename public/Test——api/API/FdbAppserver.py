# coding: UTF-8
import json
import logging
import re

import requests

from common.CanShuPaiXu1 import Paixu
from common.data_shuju import DB

LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='API.log',level=logging.INFO,format=LOG_FORMAT)

class Test_Api(object):
    def __init__(self):
        self.url={
                        'login':'http://118.178.242.96:8371/FffdAppServer/user/login.rest',#登录验证  请求参数 "mobile": "15921135537","verifyCode": "2345"
                        'real_name':'http://118.178.242.96:8371/FffdAppServer/user/realname_register.rest',#实名认证  请求参数"realName": "姓名", "idCard": "身份证号"
             }
        self.token='QTAxd0hjbEdRQzQlQCVCMDI5OEZFRC0yRDY2LTQ5MEYtQjEwMy0zOTU4RTNDRThGQjclQCUyNTM2MTc1MSVAJTExNTIwJUAlN2IyYWI5YzE5OTVkN2ZlYWZkMTAzOWU1NDAxMGI0ZDA='
        self.houseRoom=[]
        self.userID=''
        self.rentId1=[]#房间ID
        self.contractId=[]#合同Id
        self.virtualPhone=""

    def send_verifcode(self,mobile):
        #发送验证码
        base_url="http://118.178.242.96:8371/FffdAppServer/user/send_verifycode.rest"#f发送验证码   请求参数"mobile": "15921135537"
        logging.info('huo qu url :%s'%base_url)
        try:
            dict1={"mobile":mobile}
            json_dict=json.dumps(dict1,ensure_ascii=False)
            A=Paixu()
            B=A.get_canshu(dict1,A.pingguo)
            header=B[1]#获取请求头信息
            #C=A.get_time()#获取时间戳
            logging.info("now header is %s" % header)
            response=requests.post(base_url,headers=header,data=json_dict)
            #print(response.json())
            return response.json()
        except:
            cuoWuXinXi='qing zai one miute hou zai dian ji '
            logging.info(cuoWuXinXi)

    def login_in(self,mobile):
        #登录
        url='http://118.178.242.96:8371/FffdAppServer/user/login.rest'#登录验证  请求参数 "mobile": "15921135537","verifyCode": "2345"
        logging.info('current url is %s' % url)
        api=Test_Api()
        api.send_verifcode(mobile)#发送验证码
        db=DB()
        yanzhnegma=db.get_YanZhengMa(mobile)#获取验证码
        logging.info('yanZhengMa is %s ' % yanzhnegma)
        dict1={'mobile':mobile,'verifyCode':yanzhnegma}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]  # 获取请求头头信息
        logging.info("now header is %s" % header)
        response=requests.post(url,headers=header,data=json_dict)
        print(response.json())
        data_content=response.json()
        ticket=data_content['data']['ticket']#获取ticket
        userID=data_content['data']['userId']#获取userId
        hximUserId=data_content['data']['hximUserId']
        virtualPhone=data_content['data']['virtualPhone']#获取小号
        self.token=ticket#获取ticket
        self.userID=userID#获取用户id
        self.virtualPhone=virtualPhone#获取小号
        print(self.token)
        return response.json(),userID,hximUserId,virtualPhone

    def myHouseContractCount(self):
        #首页代办事项
        url = 'http://118.178.242.96:8371/FffdAppServer/user/myHouseContractCount.rest	'
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
        print(response.status_code)

    def myHouseList1(self):
        #获取房源列表    header 需要加入'u_ticket'字段
        url='http://118.178.242.96:8371/FffdAppServer/house/myHouseList.rest'#发房小区列表搜索  请求参数{"pageSize":20,"offset":0}
        logging.info('current url is %s' % url)
        dict1={"pageSize":20,"offset":0,}
        json_dict=json.dumps(dict1,ensure_ascii=False)
        A=Paixu()
        B=A.get_canshu(dict1,A.pingguo)
        header=B[1]
        header['u_ticket']=self.token
        logging.info("now header is %s" % header)
        response1=requests.post(url,headers=header,data=json_dict)
        content=response1.json()
        try:
            houseId=content['data']['rows']
            #print(houseId)
            for result in houseId:
                    print(result['id'])#获取房源ID
                    if result['id']!=None and result['jointRentRoomModelList']!=None:
                        self.houseRoom.append(result['id'])#获取有房间的房源
            logging.info('有房间的房源为%s' % self.houseRoom)
        finally:
            print(content)

    def getJointRentHouseDetail(self,n):#n参数为了获取houseId
        # 71获取合租房子详情 请求参数{“houseId”:111}
        url='http://118.178.242.96:8371/FffdAppServer/house/getJointRentHouseDetail.rest'#71获取合租房子详情 请求参数{"houseId":111}   houseId;//房子id（我的房子列表中的id）
        logging.info('current url is %s' % url)
        dict1={"houseId":int(self.houseRoom[n])}
        T=self.houseRoom[n]
        json_dict=json.dumps(dict1,ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
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
            print('房源id为 %s 的门锁安装状态是 %s!'%(T,a))
        elif status==2:
            a = '审核中'
            print('房源id为 %s 的门锁安装状态是 %s!' % (T, a))
        elif status==3:
            a = '待装锁'
            print('房源id为 %s 的门锁安装状态是 %s!' % (T, a))
        elif status==4:
            a = '已装锁'
            print('房源id为 %s 的门锁安装状态是 %s!' % (T, a))
        else:
            print('')
        #print(response.json())

    def applyInstallLock(self,n):
        # 74申请装锁
        url='http://118.178.242.96:8371/FffdAppServer/house/applyInstallLock.rest'#74申请装锁   请求参数{ "houseId":123123}
        logging.info('current url is %s' % url)
        dict1 = {"houseId": n}
        T = self.houseRoom[n]
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        requests.post(url, headers=header, data=json_dict)
        logging.info("房间为%s的房间申请装锁成功"%T)

    def listJointRentRoom(self,n):
        # 72获取合租房间列表   请求参数{"houseId":111}
        url = 'http://118.178.242.96:8371/FffdAppServer/house/listJointRentRoom.rest'#72获取合租房间列表   请求参数{"houseId":111}
        logging.info('current url is %s' % url)
        dict1 = {"houseId": n}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        try:
            content=response.json()
            rentId=content['data']['jointRentRoomModelList']#获取房屋详情内容
            if rentId!=None:
                for result in rentId:#
                    result=result['contractBillInfo']
                    self.rentId1.append(result['rentId'])#获取房间ID
                    return result['rentId']
            logging.info('rentId为%s'%self.rentId1)
        finally:
            print(response.json())

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
        B = A.get_canshu(dict1, A.pingguo)
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
            logging.info('房间号是%s 的房间还没有装门锁！'%self.rentId1[n])
        print(response.json())

    def listRentContract4RentHouse(self,n):   #参数为房间号
        #获取租约列表    请求参数{"rentId":111}
        '''
        :param n: 请求参数{"rentId":111}
        :return: contractId合同ID
        '''
        url='http://118.178.242.96:8371/FffdAppServer/contract/listRentContract4RentHouse.rest'#100获取租约列表   请求参数{"rentId":111}
        logging.info('current url is %s' % url)
        dict1 = {"rentId":n,'pageNo':1}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        content=response.json()
        print(content)
        content=content['data']['contractList']
        if content != None:
            for result in content:   #获取contractId
                contractId = result['contractId']
                self.contractId.append(contractId)
                logging.info('rentId为%s的 contractId为%s' % (n, contractId))
                name = re.compile("\'renterName\':(.*?),")
                name = name.findall(str(content))  # 获取租客姓名
                status = re.compile("\'statusDesc\':(.*?),")
                statusc = status.findall(str(content))  # 获取合同状态
                status = re.compile("\'status\':(.*?),")
                status = status.findall(str(content))  # 状态（0.未激活，1.执行中，2.已终止，3.待租客确认，6.已作废）'
                xiaoqu = re.compile("\'estateName\':(.*?),")
                xiaoqu = xiaoqu.findall(str(content))  # 获取小区名
                louhao = re.compile("\'buildingName\':(.*?),")
                louhao = louhao.findall(str(content))  # 获取楼号
                shihao = re.compile("\'room\':(.*?),")
                shihao = shihao.findall(str(content))  # 获取室号
                logging.info('%s+%s+%s室的租客是%s ,合同id为%s,目前合同状态为%s.' % (xiaoqu, louhao, shihao, name, contractId, statusc))
                return contractId
        else:
            logging.info('%s房间暂时没有合同'%n)
        print(response.json())

    def getSupportBankList(self):
        #86、获取支持银行列表（v1.0）
        url = 'http://118.178.242.96:8371/FffdAppServer/contract/getRentContractDetail.rest'
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

    def getCardBin(self,bankCardNo):
        #87、获取银行卡开户行（v1.0）
        url = 'http://118.178.242.96:8371/FffdAppServer/account/getCardBin.rest'
        logging.info('current url is %s' % url)
        dict1 = {"bankCardNo":bankCardNo}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def bindBankcard(self,bankCardNo):
        #89、提交绑定银行卡（v1.0）
        #bankcardNo;//银行卡号      bankCode;//银行编号       bankName;//银行名称        mobile;//银行卡预留手机号         cardType;//CC=贷记卡，DC=借记卡，SCC=准贷记卡，PC=预付
        url = 'http://118.178.242.96:8371/FffdAppServer/account/getCardBin.rest'
        logging.info('current url is %s' % url)
        dict1 = {"bankCardNo": bankCardNo,"bankCode":"sfsf","bankName": "招商银行","mobile":"18717777777","cardType":"DC",}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getAccountBalance(self):
        #96、获得本人账户余额[v1.0新增]
        url = 'http://118.178.242.96:8371/FffdAppServer/account/getCardBin.rest'
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

    def queryTradeList(self,timeBegin,timeEnd):
        #97、交易记录查询[v1.0新增]
        #timeBegin 开始日期yyyy-MM-dd
        #timeEnd 结束日期yyyy-MM-dd
        #pageSize 每一页查询多少条数据
        #pageNo 当前第几页，默认为1
        #groupMode 是否分组模式 1、按月分组
        url = 'http://118.178.242.96:8371/FffdAppServer/account/queryTradeList.rest'
        logging.info('current url is %s' % url)
        dict1 = { "timeBegin":timeBegin,"timeEnd":timeEnd,"pageSize":10,"pageNo":1,"groupMode":1}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getRentContractDetail(self,n):
        #102获取合同详情   请求参数{"contractId": 111}
        url='http://118.178.242.96:8371/FffdAppServer/contract/getRentContractDetail.rest'#102获取合同详情   请求参数{"contractId":111}
        logging.info('current url is %s' % url)
        dict1 = {"contractId": self.contractId[n]}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        content=response.json()
        try:
            statusDesc=content['data']['statusDesc']
            if statusDesc!=None:
                logging.info("合同ID为%s的状态为%s"%(self.contractId[0],statusDesc))
            else:
                print("暂未获取到信息")
        finally:
            print(response.json())

    def addRentContract(self,AA):
        #103创建合同
        ''''请求参数
         "type":1,   出租类型 1.整租 2.合租
        "contractType":1,     合同类型 0, 新签电子合同、1, 纸质合同补录、2, 第三方合同补录
        "roomNo":房间号      "renterName":租客姓名     "renterIdCardNo":"租客身份证",
        "credentialType":1,     "renterMobile":"租客手机号",
        "startDate":"2017-12-01",    "endDate":"2018-12-01",
        "paymentCycle":付租方式（月）  "paymentDate":收租日期(号)
        "deposit":房屋押金（分）,     "rental":房屋租金（分）,   "rentId":出租房源id,
        credentialType：证件类型 1.身份证 2.护照 3.港澳往返内地通行证 4.台湾往返内地通行
        '''
        url = 'http://118.178.242.96:8371/FffdAppServer/contract/addRentContract.rest'
        logging.info('current url is %s' % url)
        dict1 = {AA}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def updateContract(self,BB):
        #103、编辑更新租赁合同 v1.3新增 >
        '''
        :param BB:
        :return:
        "contractId":合同id,   "contractType":合同类型,     "startDate":"2017-12-01",    "endDate":"2018-12-01",
        "paymentCycle":支付周期（月）,     "paymentDate":交租日期,    "deposit":押金（分）,  "rental":租金（分
        '''
        url = 'http://118.178.242.96:8371/FffdAppServer/contract/addRentContract.rest'
        logging.info('current url is %s' % url)
        dict1 = {BB}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getReleaseContractDetail(self,contractId):
        #105、解约合同详情 v1.3修改 >
        '''
        :param contractId: 合同ID
        :return:
        '''
        url = 'http://118.178.242.96:8371/FffdAppServer/contract/getReleaseContractDetail.rest'
        logging.info('current url is %s' % url)
        dict1 = {"contractId":contractId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def createReleaseContract(self,contractId,deposit,rental,defaultFee,livingFee,otherFee,remark,):
        #106、创建解约合同 >
        '''
        :param contractId:合同id
        :param deposit:押金
        :param rental:租金
        :param defaultFee:违约金
        :param livingFee:水电煤
        :param otherFee:其他
        :param remark:备注
        :return:releaseContractId;解约合同id
        '''
        url = 'http://118.178.242.96:8371/FffdAppServer/contract/createReleaseContract.rest'
        logging.info('current url is %s' % url)
        dict1 = {"contractId": contractId,"deposit":deposit,"rental":rental,"defaultFee":defaultFee,"livingFee":livingFee,"otherFee":otherFee}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def completeReleaseContract(self,releaseContractId):
        #108、确认解约合同
        '''
        :param releaseContractId:解约合同id
        :return:
        '''
        url = 'http://118.178.242.96:8371/FffdAppServer/contract/createReleaseContract.rest'
        logging.info('current url is %s' % url)
        dict1 = { "releaseContractId":releaseContractId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def cancelRentApplyList(self,contractId):
        #109、退租申请记录 >
        url = 'http://118.178.242.96:8371/FffdAppServer/contract/cancelRentApplyList.rest'
        logging.info('current url is %s' % url)
        dict1 = {"contractId":contractId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getEContractInfo(self,contractId):
        #101、获取租赁电子合同详情 >
        url = 'http://118.178.242.96:8371/FffdAppServer/contract/getEContractInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"contractId":contractId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def terminateRentContract(self,n):#终止合同
        url = "http://118.178.242.96:8371/FffdAppServer/contract/terminateRentContract.rest"#104、终止租赁合同   请求参数{"contractId":111}
        logging.info('current url is %s' % url)
        dict1 = {"contractId": self.contractId[n]}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        requests.post(url, headers=header, data=json_dict)
        logging.info('ID为%s的合同解约成功'%n)

    def  listRentBill(self,a,b):
        #110、获取租赁账单列表  请求参数{"contractId":111,"rentId":111,"pageNo":1,"pageSize":20}#    #rentId出租id
        url='http://118.178.242.96:8371/FffdAppServer/bill/listRentBill.rest'
        logging.info('current url is %s' % url)
        dict1 = {"contractId": a,'rentId':b,"pageNo":1,"pageSize":20}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response=requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getRentBillDetail(self,billId):
        #111、获取租赁账单详情 >
        '''
        :param billId: 账单类型 1.普通账单 2.解约账单
        :return:
        '''
        url = 'http://118.178.242.96:8371/FffdAppServer/bill/getRentBillDetail.rest'
        logging.info('current url is %s' % url)
        dict1 = {"billId":billId,"type":1}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def invalidRentBill(self,billId):
        #112、作废租赁账单 >
        url = 'http://118.178.242.96:8371/FffdAppServer/bill/getRentBillDetail.rest'
        logging.info('current url is %s' % url)
        dict1 = {"billId": billId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def markBillPaid(self,billId):
        #114、标记账单为已支付 v1.3新增 >
        url = 'http://118.178.242.96:8371/FffdAppServer/bill/getRentBillDetail.rest'
        logging.info('current url is %s' % url)
        dict1 = {"billId": billId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def getAllBillLivingTypes(self):
        #115、查询所有生活账单类型 >
        url = 'http://118.178.242.96:8371/FffdAppServer/bill/getAllBillLivingTypes.restt'
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

    def  realname_register(self,name,idCard):
        #3实名登记
        url = 'http://118.178.242.96:8371/FffdAppServer/user/realname_register.rest'  # 请求参数{"cityId":2,"keyword":"上大路"}cityId; //城市id，默认2上海， keyword; //小区关键词
        logging.info('current url is %s' % url)
        dict1 = {"realName": name, "idCard": idCard}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def channel_list(self):
        #获得账户各平台注册情况
        url = 'http://118.178.242.96:8371/FffdAppServer/user/channel_list.rest'
        logging.info('current url is %s' % url)
        dict1 = {"":""}#请求参数为空时
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

    def publish_joint_rent_house(self,c):
        #55、发布合租房子信息[v1.4修改]
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

    def publish_joint_rent_room(self,B):
        #56、发布合租房间信息[v1.4修改]
        # 请求参数{ "houseId":"房子ID","roomType":1,"spaceArea":"面积","ventilation":"朝向","genderRequirement":1,"payMethod":"付款方式","price":"租金","houseEquipment":"房屋配置，多个用英文逗号隔开","roomName":"房间备注名"}
        #roomType 房间类型：1、主卧，2、次卧
        #ventilation 朝向：1、东，2、西，3、南，4、北，5、南北，6、东西，7、东南，8、东北，9、西南，10、西北
        #decorateType 装修等级：1、毛坯；2、简装；3、精装；4、豪装
        #Integer genderRequirement 性别要求：1、男女不限，2、限女生，3、限男生，4、限夫妻
        #Integer payMethod 付款方式：1、押一付一，2、押一付三，3、半年付，4、年付，5、面议
        #房屋配置：1、床，2、沙发，3、洗衣机，4、空调，5、电视，6、冰箱，7、热水器，8、宽带，9、可做饭，10、阳台，11、独立卫生间
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
        #81、我的房子统计 >
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

    def myHouseEstate(self):
        #82、我的房子小区列表V1.2 >
        url = 'http://118.178.242.96:8371/FffdAppServer/house/myHouseEstate.restt'
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

    def updateDND(self,userID,startTime,endTime):
        #更新免打扰模式  请求参数{"userId": 111,"startTime":"开始时间","endTime":"结束时间","type":1}
        #type;//0 关闭 1 开启
        url = 'http://118.178.242.96:8371/FffdAppServer/user/getVirtualMobileInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"userId": userID,"startTime":startTime,endTime:"结束时间","type":1}
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

    def getDoorBaseInfo(self,doorId):
        #120、获取门锁基本信息(v1.0新增)  "doorId":11，门锁ID
        url = 'http://118.178.242.96:8371/FffdAppServer/door/getDoorBaseInfo.rest'
        logging.info('current url is %s' % url)
        dict1 = {"doorId":doorId}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def listDoorTempPWD(self,doorId,authUserId,source):
        #121、获取门锁临时密码列表(v1.0新增)
        #请求参数 "doorId":1,门锁ID，"authUserId":授权人ID, "source":来源 1.房东 2.租客
        url = 'http://118.178.242.96:8371/FffdAppServer/door/listDoorTempPWD.rest'
        logging.info('current url is %s' % url)
        dict1 = {"doorId":doorId,"authUserId":authUserId, "source":source}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def listDoorOpen(self,doorId,authUserId,startTime,endTime):
        #122、获取门锁开门记录(v1.0新增)
        #请求参数"doorId":1，"authUserId":1, "startTime":"开始时间 yyyy-MM-dd","endTime":"结束时间 yyyy-MM-dd"
        url = 'http://118.178.242.96:8371/FffdAppServer/door/listDoorTempPWD.rest'
        logging.info('current url is %s' % url)
        dict1 = {"doorId": doorId, "authUserId": authUserId, "startTime":startTime,"endTime":endTime }
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def updateDoorPWD(self,doorId,authUserId,pwd,source):
        #Xiaoxiangyoupin、修改门锁密码(v1.0新增)
        #请求参数   String pwd密码
        url = 'http://118.178.242.96:8371/FffdAppServer/door/updateDoorPWD.rest'
        dict1 = {"doorId": doorId, "authUserId": authUserId, "pwd": pwd, "source": source}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
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
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def  checkIdentity(self,idCard):
        #146、校验身份证(v1.1新增)
        #请求参数{ "idCard":"320xxx",}
        url = 'http://118.178.242.96:8371/FffdAppServer/system/getConfigInfo.rest'
        dict1 = {"idCard":idCard}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def allot_xphone(self,bizType,id,channelTag):
        #160、分配渠道小号 [v1.3新增]
        #请求参数{"bizType":1、出租；2、出售, "id":"出售ID或出租ID","channelTag":"1百姓网 2安居客 3房多多 4赶集 5豆瓣 6五八 7爱屋吉屋 8嗨住 9一楼租房"}
        url = 'http://118.178.242.96:8371/FffdAppServer/user/allot_xphone.rest'
        dict1 = {"bizType":bizType,"id":id,"channelTag":channelTag}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def  channel_group_list(self, bizType,houseRentId):
        #161、获得房源同步平台情况 小号分组详情 [v1.3新增]
        #请求参数{"bizType":1、出租；2、出售, "houseRentId":"出租ID",}
        url = 'http://118.178.242.96:8371/FffdAppServer/user/allot_xphone.rest'
        dict1 = {"bizType": bizType, "houseRentId":houseRentId }
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def  rentHouseList4ff(self):
        #162、获取待发布一楼租房列表 <V1.3新增>
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

    def publishRentHouseToff(self,rentIds):
        #163、发布到一楼租房 <V1.3新增>
        #请求参数{"rentIds":"1,2,3",}
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

    def addAssistant(self,name,mobile):
        #170、添加助理账号 v1.3新增 >
        #请求参数{}"name":"姓名","mobile":"手机号"
        url = 'http://118.178.242.96:8371/FffdAppServer/user/addAssistant.rest'
        dict1 = {"name": name,"mobile":mobile}
        json_dict = json.dumps(dict1, ensure_ascii=False)
        A = Paixu()
        B = A.get_canshu(dict1, A.pingguo)
        header = B[1]
        header['u_ticket'] = self.token
        logging.info("now header is %s" % header)
        response = requests.post(url, headers=header, data=json_dict)
        print(response.json())

    def delAssistant(self,userId):
        #171、删除助理账号 v1.3新增 >
        #请求参数{"userId":1}
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
        #172、获取全部助理账号列表 >
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
        #176、房东年付订单列表[v1.3新增]
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
        #177、房东年付订单详情[v1.3新增]
        #请求参数{}
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


D=Test_Api()
#D.getDoorBaseInfo(10131)
#D.listDoorTempPWD(10131,10003,1)
#D.get_task_count(872)
#D.account_login(13044159642,1)
#D.h5_urls()
#D.get_last_house(2,188374,5,13)
#regJobId=D.account_reg(1,13044159642)
#D.account_reg_check(regJobId)
#D.queryEstate("fangzhoushidai")
#D.querySubEstates(35925)
#D.getBuildingInfo(188374)
#D.copy_house(913,3)
#D.publish_rent(A)
#D.channel_list1(825)
#D.listUserContact(10312)
#D.getVirtualMobileInfo(10312)
#D.myHouseContractCount()
#D.getDNDInfo()
#D.getMyInfo()
#D.realname_register("455","320882199012243215")
#D.channel_list()
#D.pay_verify()
#D.login_in("18621512473")
#a=D.myHouseList1()
#b=D.getJointRentHouseDetail(1)
#c=D.listJointRentRoom(872)
#d=D.houseDetail(n=913)
#D.openDoor(10133)
#e=D.listRentContract4RentHouse(n=912)
#D.getRentContractDetail(0)
#D.listRentBill(a=913,b=1082)


