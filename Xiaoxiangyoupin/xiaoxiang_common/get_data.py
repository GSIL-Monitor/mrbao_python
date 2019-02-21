# -*- coding: UTF-8 -*-
import os
from Xiaoxiangyoupin.xiaoxiang_common import read_yaml


class Get_data():
    '''获取请求url header data'''

    def get_url(self, yaml_name):
        '''获取api url'''
        result_content = read_yaml.get_peizhi(wenjianming='xiaoxiang_api', yaml_name=yaml_name,
                                              content_name='xiaoxiang_api_test.yaml')

        return result_content

    def get_header(self, type=1):
        '''
        获取请求头信息
        :param type: 1.为首次登陆调取  2.非首次调取
        :return: 
        '''
        header = {}
        if type != None and type == 1:
            result = read_yaml.get_peizhi(wenjianming='xiaoxiang_api', yaml_name='header',
                                          content_name='xiaoxiang_api_test.yaml')
            header['Accept-Encoding'] = result['Accept-Encoding']
            header['User-Agent'] = result['User-Agent']
            return header
        elif type == 2:
            result = read_yaml.get_peizhi(wenjianming='xiaoxiang_api', yaml_name='header',
                                          content_name='xiaoxiang_api_test.yaml')
            header['Accept-Encoding'] = result['Accept-Encoding']
            header['User-Agent'] = result['User-Agent']
            if 'token' in result.keys():  # 判断是否存在token这个key
                header['token'] = result['token']
                return header
            else:
                return header

    def get_canshu(self,wenjianming,yaml_path):
        '''获取用例'''
        if wenjianming!=None:
            wenjian_list=read_yaml.start_async(read_yaml.chaxun_wenian(yaml_path,wenjianming))#查询用例路径
            case_list=read_yaml.start_async(read_yaml.get_path_yaml(wenjian_list))#查询具体用例
            return case_list

    def jiexi_case(self,*args):
        '''解析用例'''
        pass


if __name__ == '__main__':
    a = Get_data()
    yaml_path='F:/mrbao_python/Xiaoxiangyoupin'
    print(a.get_canshu(yaml_path=yaml_path,wenjianming='xiaoxiang_test_case'))
