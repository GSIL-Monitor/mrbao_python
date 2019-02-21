# -*- coding: UTF-8 -*-
from yilou_fangdong_contract import Yilou_fangdong_Contract
from fuangyuan_parameters import FuanYuan_Parameters
from yilou_zuke_contract import Yilou_Zuke_Contract
from contract_parameters import Contract_parameters
import logging.config
con_log='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

def create_contract_queren(renterMobile, FangYuan_Name='汤臣一品', Room_Name='房间02'):
    '''合租创建合同并且确认合同'''
    FuanYuan_Parameters_ = FuanYuan_Parameters()
    fangdong_contract = Yilou_fangdong_Contract()  # 获取租约
    zuke_contract = Yilou_Zuke_Contract()
    result = FuanYuan_Parameters_.myHouseList_parameters(FangYuan_Name=FangYuan_Name, Room_Name=Room_Name)  # 查询房屋信息
    try:
        rentId = result[0]['room_rentId']  # 获取房间id
    except ValueError as E:
        logging.info(E)
    else:
        if rentId != None:
            fangdong_contract.click_create_contract(rentId=rentId)  # APP点击创建合同
            response_result = fangdong_contract.Lessee(renterMobile=renterMobile, renterName='565656')  # 输入承租人
            mainRenterId = response_result['data']['shareRenterId']  # 获取租客id
            if response_result['data']['shareRenterId'] != None and response_result['message'] == 'success':
                response_result1 = fangdong_contract.next_step(day=360, mainRenterId=mainRenterId,
                                                               rentId=rentId)  # 点击创建合同
                if response_result1['message'] == '已经存在有效的合同':
                    logging.info('已经存在有效的合同')
                    return
                if response_result['message'] != '已经存在有效的合同':
                    contractId = response_result1['data']['contractId']  # 获取合同id
                    if contractId != None and response_result['message'] == 'success':
                        fangdong_contract.create_bill(contractId=contractId)  # 创建账单
                        fangdong_contract.setBillPaid(contractId=contractId)  # 生成账单
                        zuke_contract.renter_confirm_contract(contractId=contractId)  # 租客z确认合同
                else:
                    logging.info("创建合同失败")
            else:
                logging.info('mainRenterId is None')
        else:
            logging.info("room_rentId is None")


def create_zhengzu_contract_queren(renterMobile, FangYuan_Name='汤臣一品', Room_Name='房间01'):
    '''整租创建合同并且确认合同'''
    FuanYuan_Parameters_ = FuanYuan_Parameters()
    fangdong_contract = Yilou_fangdong_Contract()  # 获取租约
    zuke_contract = Yilou_Zuke_Contract()
    result = FuanYuan_Parameters_.myHouseList_parameters(FangYuan_Name=FangYuan_Name, Room_Name=Room_Name)  # 查询房屋信息
    rentId = result[1]['rentId']  # 获取房间id
    if rentId==None:
        return None
    if rentId != None:
        fangdong_contract.click_create_contract(rentId=rentId)  # APP点击创建合同
        response_result = fangdong_contract.Lessee(renterMobile=renterMobile, renterName='565656')  # 输入承租人
        mainRenterId = response_result['data']['shareRenterId']  # 获取租客id
        if response_result['data']['shareRenterId'] != None and response_result['message'] == 'success':
            response_result1 = fangdong_contract.next_step(day=360, mainRenterId=mainRenterId, rentId=rentId)  # 点击创建合同
            if response_result1['message'] == '已经存在有效的合同':
                logging.info('已经存在有效的合同')
                return
            if response_result['message'] != '已经存在有效的合同':
                contractId = response_result1['data']['contractId']  # 获取合同id
                if contractId != None and response_result['message'] == 'success':
                    fangdong_contract.create_bill(contractId=contractId)  # 创建账单
                    fangdong_contract.setBillPaid(contractId=contractId)  # 生成账单
                    zuke_contract.renter_confirm_contract(contractId=contractId)  # 租客z确认合同
            else:
                logging.info("创建合同失败")
        else:
            logging.info('mainRenterId is None')
    else:
        logging.info("room_rentId is None")

def create_contract_queren_tongzhurn(shareRenterMobile,renterMobile, FangYuan_Name='汤臣一品', Room_Name='房间02'):
    '''创建合同并且确认合同加同住租客'''
    FuanYuan_Parameters_ = FuanYuan_Parameters()
    fangdong_contract = Yilou_fangdong_Contract()  # 获取租约
    zuke_contract = Yilou_Zuke_Contract()
    result = FuanYuan_Parameters_.myHouseList_parameters(FangYuan_Name=FangYuan_Name, Room_Name=Room_Name)  # 查询房屋信息
    print(result)
    rentId = result[0]['room_rentId']  # 获取房间id
    if rentId != None:
        fangdong_contract.click_create_contract(rentId=rentId)  # APP点击创建合同
        response_result = fangdong_contract.Lessee(renterMobile=renterMobile, renterName='565656')  # 输入承租人
        mainRenterId = response_result['data']['shareRenterId']  # 获取主租客id

        response_result = fangdong_contract.Lessee(renterMobile=shareRenterMobile, renterName='565656')  # 输入承租人
        shareRenterId = response_result['data']['shareRenterId']  # 获取同住租客id

        if response_result['data']['shareRenterId'] != None and response_result['message'] == 'success':
            response_result1 = fangdong_contract.next_step_tongzhuren(shareRenterIdListStr=shareRenterId,mainRenterId=mainRenterId, rentId=rentId)  # 点击创建合同
            if response_result1['message'] == '已经存在有效的合同':
                logging.info('已经存在有效的合同')
                return
            if response_result['message'] != '已经存在有效的合同':
                contractId = response_result1['data']['contractId']  # 获取合同id
                if contractId != None and response_result['message'] == 'success':
                    fangdong_contract.create_bill(contractId=contractId)  # 创建账单
                    fangdong_contract.setBillPaid(contractId=contractId)  # 生成账单
                    zuke_contract.renter_confirm_contract(contractId=contractId)  # 租客z确认合同
            else:
                logging.info("创建合同失败")
        else:
            logging.info('mainRenterId is None')
    else:
        logging.info("room_rentId is None")


def create_contract_jieyue(renterMobile, FangYuan_Name='汤臣一品', Room_Name='房间02'):
    '''确认合同后再解约合同'''
    FuanYuan_Parameters_ = FuanYuan_Parameters()
    fangdong_contract_parameter = Contract_parameters()
    fangdong_contract = Yilou_fangdong_Contract()  # 获取租约
    zuke_contract = Yilou_Zuke_Contract()
    result = FuanYuan_Parameters_.myHouseList_parameters(FangYuan_Name=FangYuan_Name, Room_Name=Room_Name)  # 查询房屋信息
    rentId = result[0]['room_rentId']  # 获取房间id
    if rentId != None:
        fangdong_contract.click_create_contract(rentId=rentId)  # APP点击创建合同
        response_result = fangdong_contract.Lessee(renterMobile=renterMobile, renterName='565656')  # 输入承租人
        mainRenterId = response_result['data']['shareRenterId']  # 获取租客id
        if response_result['data']['shareRenterId'] != None and response_result['message'] == 'success':
            response_result1 = fangdong_contract.next_step(day=360, mainRenterId=mainRenterId,
                                                           rentId=rentId)  # 点击创建合同
            if response_result1['message'] == '已经存在有效的合同':
                logging.info('已经存在有效的合同')
                return
            if response_result['message'] != '已经存在有效的合同':
                contractId = response_result1['data']['contractId']  # 获取合同id
                if contractId == None:
                    logging.info('contractId is None')
                    return
                if contractId != None and response_result['message'] == 'success':
                    fangdong_contract.create_bill(contractId=contractId)  # 创建账单
                    fangdong_contract.setBillPaid(contractId=contractId)  # 生成账单
                    zuke_contract.renter_confirm_contract(contractId=contractId)  # 租客确认合同
                    logging.info('创建合同成功')
                    result = fangdong_contract_parameter.contract_canshu(contractId)  # 查询具体合同
                    if result == None:
                        logging.info('None')
                        return
                    elif result != None:

                        otherFee = 0
                        livingFee = 0
                        rental = 0
                        defaultFee = 0
                        deposit = 0
                        fangdong_contract.createReleaseContract(contractId=contractId, otherFee=otherFee,
                                                                livingFee=livingFee, rental=rental,
                                                                defaultFee=defaultFee, deposit=deposit)#解约合同
                        logging.info('快速退房结账SUCCESS')
            else:
                logging.info("创建合同失败")
        else:
            logging.info('mainRenterId is None')
    else:
        logging.info("room_rentId is None")

def jieyue_contract(contractId):
    '''解约合同'''
    fangdong_contract_parameter = Contract_parameters()
    fangdong_contract = Yilou_fangdong_Contract()
    result = fangdong_contract_parameter.contract_canshu(contractId)  # 查询具体合同
    if result == None:
        logging.info('None')
        return
    elif result != None:
        #if result['otherFee'] == 0:
            #otherFee = result['otherFee']
        #if result['otherFee'] < 0:
            #otherFee = result['otherFee'] + abs(result['otherFee'])
        #if result['otherFee'] > 0:
            #otherFee = result['otherFee'] - result['otherFee'] * -1
        otherFee = 0
        livingFee = 0
        rental = 0
        defaultFee = 0
        deposit = 0
        fangdong_contract.createReleaseContract(contractId=contractId, otherFee=otherFee,
                                                livingFee=livingFee, rental=rental,
                                                defaultFee=defaultFee, deposit=deposit)  # 解约合同
        logging.info('快速退房结账SUCCESS')

if __name__ == '__main__':
    #create_contract_queren(renterMobile='17400880088',FangYuan_Name='富特三村',Room_Name='房间02')
    #create_contract_queren(renterMobile='17400330093',FangYuan_Name='万科翡翠滨江',Room_Name='房间01')
    #create_contract_queren_tongzhurn(shareRenterMobile='17400330094',renterMobile='17400330095', FangYuan_Name='万科翡翠滨江',Room_Name='房间01')
    create_zhengzu_contract_queren(renterMobile='17400880088', FangYuan_Name=' 阳光公寓')
    #jieyue_contract(3936)


