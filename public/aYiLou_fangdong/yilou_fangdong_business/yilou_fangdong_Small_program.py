# -*- coding: UTF-8 -*-
import logging.config

from CanShuPaiXu1 import Paixu
from read_Yaml_Config import Read_Yaml_Config
from request_bane import Request_

con_log=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(con_log)
logger=logging.getLogger()

class Small_Program(Request_,Read_Yaml_Config,Paixu):
    '''小程序'''

    def rent_analysis(self):
        '''出房分析图表'''
        send_url = self.get_peizhi('xiaochengxu', yaml_ming='yilou_fangdong.yaml')
        send_url = send_url['rent_analysis']  # 出房分析图表

        logging.info('url is %s' % send_url)

        send_dict = {'':''}
        logging.info(send_dict)

        response = self.request_post(send_url, send_dict)
        # logging.info(response)
        return response

if __name__ == '__main__':
    A=Small_Program()
    response=A.rent_analysis()
    data=response['data']
    print(data)
    currentVacancy=data['currentVacancy']#当前空置数量
    print(currentVacancy)
    todayRent=data['todayRent']#今日出租数量
    print(todayRent)
    todayVacancy=data['todayVacancy']#今日空置数S
    print(todayVacancy)

    day7View=data['day7View']

    dateWeek=day7View['dateWeek']#获取周
    noLockData=day7View['noLockData']#无锁的数量
    lockData=day7View['lockData']#有锁的数量
    dateStr=day7View['dateStr']#获取日期

