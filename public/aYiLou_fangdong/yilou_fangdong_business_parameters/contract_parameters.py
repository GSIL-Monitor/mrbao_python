# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')

import logging.config
from yilou_fangdong_contract import Yilou_fangdong_Contract
con_log='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

class Contract_parameters(Yilou_fangdong_Contract):
    '''合同接口参数获取'''
    def contract_canshu(self,contractId):
        '''租约参数获取'''
        #contractId=3702  defaultFee=-2.25 deposit=-3.00 livingFee=0.00 otherFee=+7.95  rental=-2.70 remark=
        contract_shuju={}
        result=self.getReleaseContractDetail(contractId)#调取合同详情接口
        data_row = result['data'] # 获取接口返回数据
        landlordBillItemInfo=data_row['landlordBillItemInfo']#获取数据
        renterBillItemInfo=data_row['renterBillItemInfo']

        deposit = renterBillItemInfo['deposit']
        contract_shuju['deposit'] = deposit

        totalFeeStr = landlordBillItemInfo['totalFeeStr']
        contract_shuju['totalFeeStr'] = totalFeeStr

        rental = landlordBillItemInfo['rental']
        contract_shuju['rental'] = rental

        defaultFee = landlordBillItemInfo['defaultFee']
        contract_shuju['defaultFee'] = defaultFee

        livingFee = landlordBillItemInfo['livingFee']
        contract_shuju['livingFee'] = livingFee


        return contract_shuju

if __name__ == '__main__':
    A=Contract_parameters()
    print(A.contract_canshu(3962))

