# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\config')
sys.path.append('d:\\Python_study\\PYREQUESTS\\aYiLou_fangdong')

from  yilou_fangdong_Small_program import Small_Program
from CanShuPaiXu1 import Paixu
from data_shuju import Test_Db
import logging.config
from startEnd import StartEnd
from visualization02 import bar_graph

log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

small_program=Small_Program()
content_lockDate=[]
content_nolockDate=[]

class Test_Small_Program(StartEnd,Test_Db,Paixu):
    def test_Small_Program(self,category, type=0):
        '''
        :param category: 
        :param type: 0为未装锁，1为装锁
        :return: 
        '''
        execution_yousuo_quantity = 0  # 执行数量
        execution_wusuo_quantity = 0  # 执行数量

        response = small_program.rent_analysis()
        data = response['data']
        currentVacancy = data['currentVacancy']  # 当前空置数量
        todayRent = data['todayRent']  # 今日出租数量
        todayVacancy = data['todayVacancy']  # 今日空置数
        day7View = data['day7View']

        dateWeek = day7View['dateWeek']  # 获取周
        noLockData = day7View['noLockData']  # 无锁的数量
        lockData = day7View['lockData']  # 有锁的数量
        dateStr = day7View['dateStr']  # 获取日期


        for i1, i2, i3 in zip(dateWeek, noLockData, dateStr):  # 无锁
            i4 = str(i1) + str(i2) + str(i3)
            i4 = "日期是%s，%s。无锁的数据为%s " % (str(i3), str(i1), str(i2))
            content_nolockDate.append(i4)
        for i1, i2, i3 in zip(dateWeek, lockData, dateStr):  # 有锁
            i4 = str(i1) + str(i2) + str(i3)
            i4 = "日期是%s，%s。有锁的数据为%s " % (str(i3), str(i1), str(i2))
            content_lockDate.append(i4)


        if category == 1 and type == 0:  # 有锁第一天
            report_date = self.get_time2(day=-7)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date)==lockData[0]:#与数据库做对比
                bar_graph(attr=dateStr, v1=lockData, v2=noLockData)
                logging.info('当前空置数 %s.' % currentVacancy)
                logging.info('今日出租数 %s.' % todayRent)
                logging.info('今日空置数 %s.' % todayVacancy)
                logging.info('%s Implementation success'%report_date)
                return content_lockDate[0]

            else:
                logging.info('%s Data Error'%report_date)

        elif category == 2 and type == 0:  # 有锁第二天

            report_date = self.get_time2(day=-6)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date)==lockData[1]:#与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_lockDate[1]
            else:
                logging.info('%s Data Error'%report_date)

        elif category == 3 and type == 0:  # 有锁第三天

            report_date = self.get_time2(day=-5)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date)==lockData[2]:#与数据库做对比
                logging.info('%s Implementation success' % report_date)
                return content_lockDate[2]
            else:
                logging.info('%s Data Error' % report_date)

        elif category == 4 and type == 0:  # 有锁第四天

            report_date = self.get_time2(day=-4)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date)==lockData[3]:#与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_lockDate[3]
            else:
                logging.info('%s Data Error' % report_date)

        elif category == 5 and type == 0:  # 有锁第五天

            report_date = self.get_time2(day=-3)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date)==lockData[4]:#与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_lockDate[4]
            else:
                logging.info('%s Data Error' % report_date)

        elif category == 6 and type == 0:  # 有锁第六天

            report_date = self.get_time2(day=-2)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date) == lockData[5]:  # 与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_lockDate[5]
            else:
                logging.info('%s Data Error' % report_date)

        elif category == 7 and type == 0:  # 有锁第七天

            report_date = self.get_time2(day=-1)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date) == lockData[6]:  # 与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_lockDate[6]
            else:
                logging.info('%s Data Error' % report_date)

        elif category == 1 and type == 1:  # 无锁第一天
            report_date = self.get_time2(day=-7)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date,hasLock='0') == noLockData[0]:  # 与数据库做对比

                logging.info('当前空置数 %s' % currentVacancy)
                logging.info('今日出租数 %s' % todayRent)
                logging.info('今日空置数 %s' % todayVacancy)
                logging.info('%s Implementation success' % report_date)
                return content_nolockDate[0]
            else:
                logging.info('%s Data Error' % report_date)


        elif category == 2 and type == 1:
            report_date = self.get_time2(day=-6)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date, hasLock='0') == noLockData[1]:  # 与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_nolockDate[1]
            else:
                logging.info('%s Data Error' % report_date)

        elif category == 3 and type == 1:
            report_date = self.get_time2(day=-5)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date, hasLock='0') == noLockData[2]:  # 与数据库做对比
                logging.info('%s Implementation success' % report_date)
                return content_nolockDate[2]
            else:
                logging.info('%s Data Error' % report_date)

        elif category == 4 and type == 1:
            report_date = self.get_time2(day=-4)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date, hasLock='0') == noLockData[3]:  # 与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_nolockDate[3]
            else:
                logging.info('%s Data Error' % report_date)

        elif category == 5 and type == 1:
            report_date = self.get_time2(day=-3)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date, hasLock='0') == noLockData[4]:  # 与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_nolockDate[4]
            else:
                logging.info('%s Data Error' % report_date)


        elif category == 6 and type == 1:
            report_date = self.get_time2(day=-2)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date, hasLock='0') == noLockData[5]:  # 与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_nolockDate[5]
            else:
                logging.info('%s Data Error' % report_date)

        elif category == 7 and type == 1:
            report_date = self.get_time2(day=-1)[5]
            report_date = "\'" + report_date + '\''
            logging.info("%s are being implemented." % report_date)
            if self.select_room_data(report_date=report_date, hasLock='0') == noLockData[6]:  # 与数据库做对比

                logging.info('%s Implementation success' % report_date)
                return content_nolockDate[6]
            else:
                logging.info('%s Data Error' % report_date)

        else:
            return None

if __name__ == '__main__':
    a=Test_Small_Program()
    c=a.test_Small_Program(1,0)
    print(c)

    #for i in range(1,7):
       # c=a.test_Small_Program(i,0)
       # print(c)

    #for i in range(1,7):
        #d=a.test_Small_Program(i,1)
       # print(d)