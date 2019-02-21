#coding:utf-8
import time
import unittest
from HTMLTestRunner_cn import HTMLTestRunner


test_dir='F:\\mrbao_python\\Xiaoxiangyoupin\\xiaoxiang_test_case'#测试用例地址
path = 'F:\\mrbao_python\\Xiaoxiangyoupin\\xiaoxiang_report\\'#报告地址

def test_run():
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*test.py')#测试集
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = path + now + 'result.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='xiaoxiang JieKou Test Report',
                                description='XIAOXIANG')
        runner.run(discover)
    fp.close()

    #A = Send_email()
    #file_name = A.check_report_time()
    #A.send_email(file_name)
if __name__ == '__main__':
    test_run()