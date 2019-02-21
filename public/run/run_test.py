#coding:utf-8
import sys
sys.path.append(r'E:\Python_study\PYREQUESTS\aYiLou_fangdong_businessa\yilou_fangdong_baseView')
sys.path.append(r'E:\Python_study\PYREQUESTS\common')
sys.path.append(r'E:\Python_study\PYREQUESTS\aYiLou_fangdong_businessa\yilou_fangdong_config')
sys.path.append(r'E:\Python_study\PYREQUESTS\aYiLou_fangdong_businessa\yilou_fangdong_business')
sys.path.append(r'E:\Python_study\PYREQUESTS\report')
import logging.config
log_path=r'E:\Python_study\PYREQUESTS\config\logging.conf'

import time
import unittest
from HTMLTestReportCN import HTMLTestRunner
from send_email import Send_email

test_dir='E:\\Python_study\\PYREQUESTS\\test_case'#测试用例地址
path = 'E:\\Python_study\\PYREQUESTS\\report\\'#报告地址

def test_run():
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*test.py')#测试集
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = path + now + 'result.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='YILou FangDongDuan JieKou Test Report',
                                description='fangdongduan')
        runner.run(discover)
    fp.close()

    A = Send_email()
    file_name = A.check_report_time()
    A.send_email(file_name)

if __name__ == '__main__':
    test_run()