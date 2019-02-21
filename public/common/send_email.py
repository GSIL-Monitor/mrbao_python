# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_config')
sys.path.append(r'd:\Python_study\PYREQUESTS\aYiLou_fangdong\yilou_fangdong_business')
sys.path.append(r'd:\Python_study\PYREQUESTS\report')
import smtplib
import os
import logging.config
from email.mime.text import MIMEText
from read_Yaml_Config import Read_Yaml_Config

log_path='d:\\Python_study\\PYREQUESTS\\config\\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

#①email模块：负责构建邮件
#②smtplib模块：负责发送邮件

class Send_email(Read_Yaml_Config):
    '''
    发送邮件
    
     ①email模块：负责构建邮件
     ②smtplib模块：负责发送邮件
    
    '''
    def __init__(self):
        data = self.get_peizhi('Formail', 'smpt.yaml')
        self.password = data['Formain_password']
        self.qq_email_name = '929433269@qq.com'
        self.send_name = 'baotao.sh@superjia.com'#发送邮件账号
        self.smpt_server = data['send_sever']#邮件服务
        self.smpt_port = 25#邮件服务端口号
        self.test_dir='E:\\Python_study\\PYREQUESTS\\report'#报告地址

    def check_report_time(self):
        '''
        查找最新文件
        :return: 
        '''
        file_lists=os.listdir(self.test_dir)#其获取目录下的文件列表

        file_lists.sort(key=lambda fn: os.path.getmtime(self.test_dir + "\\" + fn)
                 if not os.path.isdir(self.test_dir + "\\" + fn) else 0)

        logging.info('The latest document is %s'%file_lists[-1])#获取最新文件

        file=os.path.join(self.test_dir,file_lists[-1])#最新报告完整路径

        logging.info('rerort complete path is %s'%file)

        return file

    def send_email(self,file_name,receiver_email_name = '929433269@qq.com'):

        send_email_name = self.send_name#邮件发送者

        smpt_server = self.smpt_server
        smpt_port = self.smpt_port

        with open(file_name,'rb')as F:#读取html内容
            mail_body=F.read()
        F.close()

        message_content = MIMEText(mail_body,'html', 'utf_8')
        # receiver_name=qq_email_name
        message_content['From'] = send_email_name#邮件发送者
        message_content['To'] = receiver_email_name#邮件接受者
        message_content['Subject'] = 'Automated test results'
        server = smtplib.SMTP(smpt_server, smpt_port)
        try:
            server.login( self.send_name, password=self.password)#登录邮件
            server.sendmail(send_email_name, receiver_email_name, message_content.as_string())#发送邮件
        except:
            logging.info('Mail delivery faile')
        else:
            logging.info('Mail sent successfully')

        finally:
            server.quit()


if __name__ == '__main__':
    A=Send_email()
    file_name=A.check_report_time()
    print(file_name)
    A.send_email(file_name)






