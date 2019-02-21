# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_operation_flow')
sys.path.append('d:\\Python_study\PYREQUESTS\\aYiLou_fangdong\\yilou_fangdong_business_parameters')
import logging.config
from fuangyuan_parameters import  FuanYuan_Parameters

con_log='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

class Create_house(FuanYuan_Parameters):
    '''创建房屋'''

    def rented_house(self,estateName=''):
        '''创建合租房屋'''
        try:
            queryEstate=self.queryEstate_parameter(xiaoqu_Name=estateName)
            logging.info(queryEstate)
            estateId=queryEstate[0]#小区ID
            estateName=queryEstate[1]#小区名称

            querySubEstates=self.querySubEstates_parameter(estateId=estateId)
            logging.info(querySubEstates)
            subEstateId=querySubEstates[1]#子划分ID
            subEstateName=querySubEstates[0]#小区路名

            houseId=self.publish_joint_rent_house_parameter(estateId=estateId,estateName=estateName,subEstateId=subEstateId,subEstateName=subEstateName)
            logging.info(houseId)

        except:
            print('创建合租房屋失败')

    def rented_house_create_apply(self,estateName=''):
        '''创建房源并且填写房间信息，且申请装锁成功'''
        try:
            queryEstate=self.queryEstate_parameter(xiaoqu_Name=estateName)
            logging.info(queryEstate)
            estateId=queryEstate[0]#小区ID
            estateName=queryEstate[1]#小区名称

            querySubEstates=self.querySubEstates_parameter(estateId=estateId)
            logging.info(querySubEstates)
            subEstateId=querySubEstates[1]#子划分ID
            subEstateName=querySubEstates[0]#小区路名

            houseId=self.publish_joint_rent_house_parameter(estateId=estateId,estateName=estateName,subEstateId=subEstateId,subEstateName=subEstateName)
            logging.info(houseId)
            rentIds = self.getJointRentHouseDetail_parameter(houseId=houseId)#获取房间id
            for i in rentIds:
                self.update_rent(rentId=i, houseId=houseId)
                logging.info('Fill in %s information successfully' % i)
            self.applyInstallLock(houseId=houseId)
            logging.info('房源为%s申请装锁成功'%houseId)
        except:
            print('创建合租房屋失败')

    def rented_house_delete(self,estateName=''):
        '''创建房源并且删除房屋'''
        try:
            queryEstate=self.queryEstate_parameter(xiaoqu_Name=estateName)
            logging.info(queryEstate)
            estateId=queryEstate[0]#小区ID
            estateName=queryEstate[1]#小区名称

            querySubEstates=self.querySubEstates_parameter(estateId=estateId)
            logging.info(querySubEstates)
            subEstateId=querySubEstates[1]#子划分ID
            subEstateName=querySubEstates[0]#小区路名

            houseId=self.publish_joint_rent_house_parameter(estateId=estateId,estateName=estateName,subEstateId=subEstateId,subEstateName=subEstateName)
            logging.info(houseId)
            if houseId !=None:
                self.removeHouse(houseId=houseId)
                logging.info('删除%ssuccess！'%houseId)
            else:
                logging.info('删除%faus！'%houseId)
        except:
            print('创建合租房屋失败')

    def rented_house_create(self,estateName=''):
        '''创建房源并且填写房间信息，且申请装锁成功并且删除'''
        try:
            queryEstate=self.queryEstate_parameter(xiaoqu_Name=estateName)
            logging.info(queryEstate)
            estateId=queryEstate[0]#小区ID
            estateName=queryEstate[1]#小区名称

            querySubEstates=self.querySubEstates_parameter(estateId=estateId)
            logging.info(querySubEstates)
            subEstateId=querySubEstates[1]#子划分ID
            subEstateName=querySubEstates[0]#小区路名

            houseId=self.publish_joint_rent_house_parameter(estateId=estateId,estateName=estateName,subEstateId=subEstateId,subEstateName=subEstateName)
            logging.info(houseId)
            rentIds = self.getJointRentHouseDetail_parameter(houseId=houseId)#获取房间id
            for i in rentIds:
                self.update_rent(rentId=i, houseId=houseId)
                logging.info('Fill in %s information successfully' % i)
            self.applyInstallLock(houseId=houseId)
            logging.info('房源为%s申请装锁成功'%houseId)
            self.cancelDoorInstallApply(houseId=houseId)
            logging.info('房源为%s取消装锁成功'%houseId)
            self.removeHouse(houseId=houseId)
            logging.info('房源为%s删除成功'%houseId)
        except:
            print('创建合租房屋失败')

    def whole_rent(self,estateName=''):
        '''创建整租房屋'''
        try:
            queryEstate=self.queryEstate_parameter(xiaoqu_Name=estateName)
            logging.info(queryEstate)
            estateId=queryEstate[0]#小区ID
            estateName=queryEstate[1]#小区名称

            querySubEstates=self.querySubEstates_parameter(estateId=estateId)
            logging.info(querySubEstates)
            subEstateId=querySubEstates[1]#子划分ID
            subEstateName=querySubEstates[0]#小区路名

            houseId=self.publish_rent(estateId=estateId,estateName=estateName,subEstateId=subEstateId,subEstateName=subEstateName)
            logging.info(houseId)
        except:
            print('创建整租房屋失败')
if __name__ == '__main__':
    A=Create_house()
    #A.rented_house(estateName='中粮海景壹号',building='5',room='11')
    #A.whole_rent(estateName='中粮海景壹号',building='5',room='11')
    A.rented_house_create_apply(estateName='中粮海景壹号')
