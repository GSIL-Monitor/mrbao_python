# -*- coding: UTF-8 -*-
from api_request import request_post, request_get
from jiexi_request_response import jiexi_json
from read_yaml import get_peizhi, write_data
import logging.config
import sys

con_log = r'F:\mrbao_python\Xiaoxiangyoupin\xiaoxiang_peizhi\logging.conf'
logging.config.fileConfig(con_log)


class Xixoxiang_Login(object):
    '''小象登录模块'''

    def __init__(self):
        '''读取配置信息'''
        self.url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='Login',
                              content_name='xiaoxiang_api_test.yaml')  # 获取url
        # self.__tiken = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token', content_name='xiaoxiang_token.yaml')#获取header

    async def yaml_load(self):
        pass

    def login(self, mobile, verifcode, type=1):
        '''（移动端）登录'''
        funcName = sys._getframe().f_back.f_code.co_name  # 获取调用函数名
        lineNumber = sys._getframe().f_back.f_lineno  # 获取行号

        current_fun = sys._getframe().f_code.co_name  # 获取当前函数名
        print(current_fun)
        login_url = self.url['login_url']  # 获取url
        logging.info("请求的url为:%s" % login_url)
        # header=self.__header['token']
        data = {'mobile': mobile, 'verCode': verifcode}
        logging.info("请求的data为:%s" % data)
        response = request_post(base_url=login_url, header='', dict_data=data)  # 发起请求
        logging.info("正在请求中......")
        if response['body'] != None:  # 如果response_result值为不为空
            body = response['body']  # 获取到body的值
            if body['token'] != None and 'token' in body.keys():  # 如果’token‘这个可以在body的KEY里面并且不为空
                token = body['token']  # 获取token的值
                logging.info("token：%s" % token)
                try:
                    if type == 1:
                        write_data(wenjianming='xiaoxiang_peizhi', yaml_name=mobile + 'token_test', yaml_data=token,
                                   content_name='xiaoxiang_token.yaml')  # 写入token值

                    if type == 2:
                        write_data(wenjianming='xiaoxiang_peizhi', yaml_name=mobile + 'token_prod', yaml_data=token,
                                   content_name='xiaoxiang_token.yaml')  # 写入token值

                except:
                    raise ("写入失败")
                logging.info(response)
        return response


if __name__ == '__main__':
    A = Xixoxiang_Login()
    c = A.login(mobile='18501787064', verifcode=888888)
