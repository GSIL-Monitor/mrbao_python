# -*- coding: UTF-8 -*-
from api_request import request_post, request_get
from jiexi_request_response import jiexi_json
from read_yaml import get_peizhi, write_data
from get_data import Get_data
import logging.config
con_log=r'F:\mrbao_python\Xiaoxiangyoupin\xiaoxiang_peizhi\logging.conf'
logging.config.fileConfig(con_log)
class Nianhuojie_jika(Get_data):

    def drawCard(self):
        '''抽卡'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='nianhuojie',
                         content_name='xiaoxiang_api_test.yaml')['drawCard']  # 获取url['recommendPage']
        logging.info("请求的url为:%s" % url)
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',
                           content_name='xiaoxiang_token.yaml')# 获取header
        logging.info("token：%s" % token)
        data = {'token': token}
        logging.info("请求的data为:%s" % data)
        header = self.get_header()
        logging.info("请求的header为:%s" % header)
        logging.info("正在请求......")
        response = request_post(base_url=url, dict_data=data, header=header)
        logging.info("请求结束......")
        print(response)
        return response

    def surplusDrawCardCount(self):
        '''查询用户剩余抽卡次数'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='nianhuojie',
                         content_name='xiaoxiang_api_test.yaml')['surplusDrawCardCount']  # 获取url['recommendPage']
        logging.info("请求的url为:%s" % url)
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',

                           content_name='xiaoxiang_token.yaml')# 获取header
        logging.info("token：%s" % token)
        header = self.get_header()
        logging.info("请求的header为:%s" % header)
        data = {'token': token}
        logging.info("token：%s" % token)
        logging.info("正在请求......")
        response = request_post(base_url=url, dict_data=data, header=header)
        logging.info("请求结束......")
        print(response)
        return response

    def queryCashOrNot(self):
        '''查询用户是否能兑奖'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='nianhuojie',
                         content_name='xiaoxiang_api_test.yaml')['queryCashOrNot']  # 获取url['recommendPage']
        logging.info("请求的url为:%s" % url)
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',
                           content_name='xiaoxiang_token.yaml')# 获取header
        logging.info("token：%s" % token)
        header = self.get_header()
        logging.info("请求的header为:%s" % header)
        data = {'token': token}
        logging.info("请求的data为:%s" % data)
        logging.info("正在请求......")
        response = request_post(base_url=url, dict_data=data, header=header)
        logging.info("请求结束......")
        print(response)
        return response

    def queryDrawCardCollectInfo(self):
        '''查询用户集卡信息'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='nianhuojie',
                         content_name='xiaoxiang_api_test.yaml')['queryDrawCardCollectInfo']  # 获取url['recommendPage']
        logging.info("请求的url为:%s" % url)
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',
                           content_name='xiaoxiang_token.yaml')# 获取header
        logging.info("token：%s" % token)
        header = self.get_header()
        logging.info("请求的header为:%s" % header)
        data = {'token': token}
        logging.info("请求的data为:%s" % data)
        logging.info("正在请求......")
        response = request_post(base_url=url, dict_data=data, header=header)
        logging.info("请求结束......")
        print(response)
        return response

    def share(self):
        '''用户分享行为上报接口'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='nianhuojie',
                         content_name='xiaoxiang_api_test.yaml')['share']  # 获取url['recommendPage']
        logging.info("请求的url为:%s" % url)
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',
                           content_name='xiaoxiang_token.yaml')# 获取header
        logging.info("token：%s" % token)
        header = self.get_header()
        logging.info("请求的header为:%s" % header)
        data = {'token': token}
        logging.info("请求的data为:%s" % data)
        logging.info("正在请求......")
        response = request_post(base_url=url, dict_data=data, header=header)
        logging.info("请求结束......")
        print(response)
        return response

    def getUserAwardList(self):
        '''用户现金奖励明细接口'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='nianhuojie',
                         content_name='xiaoxiang_api_test.yaml')['getUserAwardList']  # 获取url['recommendPage']
        logging.info("请求的url为:%s" % url)
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',
                           content_name='xiaoxiang_token.yaml')# 获取header
        header = self.get_header()
        logging.info("请求的header为:%s" % header)
        data = {'token': token}
        logging.info("请求的data为:%s" % data)
        logging.info("正在请求......")
        response = request_post(base_url=url, dict_data=data, header=header)
        logging.info("请求结束......")
        print(response)
        return response

    def cash(self):
        '''用户现金奖励明细接口'''
        url = get_peizhi(wenjianming='xiaoxiang_api', yaml_name='nianhuojie',
                         content_name='xiaoxiang_api_test.yaml')['cash']  # 获取url['recommendPage']
        logging.info("请求的url为:%s" % url)
        token = get_peizhi(wenjianming='xiaoxiang_peizhi', yaml_name='token',
                           content_name='xiaoxiang_token.yaml')# 获取header
        header = self.get_header()
        logging.info("请求的header为:%s" % header)
        data = {'token': token}
        logging.info("请求的data为:%s" % data)
        logging.info("正在请求......")
        response = request_post(base_url=url, dict_data=data, header=header)
        print(response)
        return response

if __name__ == '__main__':
    A=Nianhuojie_jika()
    A.drawCard()

