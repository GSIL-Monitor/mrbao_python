# coding: UTF-8
import json
import logging
import re

import requests

from CanShuPaiXu1 import Paixu

LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='API.log',level=logging.INFO,format=LOG_FORMAT)

class ZuYue(object):
    def __init__(self):
        self.token=""
        self.contractId=[]
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
