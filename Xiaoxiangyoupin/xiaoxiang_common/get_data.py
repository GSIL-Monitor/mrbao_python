# -*- coding: UTF-8 -*-
from Xiaoxiangyoupin.xiaoxiang_common import read_yaml


class Get_data():
    '''获取请求url header data'''

    def get_url(self, yaml_name):
        '''获取api url'''
        result_content = read_yaml.get_peizhi(wenjianming='xiaoxiang_api', yaml_name=yaml_name,
                                              content_name='xiaoxiang_api_test.yaml')
        '''        
        for key in key_list:
            result = result_content[key]['result']  # 获取api文档结果
            expected_result = result['expected_result']  # 获取预期结果
            actual_result = result['actual_result']  # 获取实际结果
            case_name = result_content[key]['case_name']  # 获取用例名称
            login_url = result_content[key]['login_url']  # 获取接口url
            data = result_content[key]['data']  #
            pass
            
            '''

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

    def get_canshu(self):
        '''获取请求参数'''
        pass

    def save_data(self):
        '''保存数据'''
        pass


if __name__ == '__main__':
    a = Get_data()
    print(a.get_url(yaml_name='dapaijiangjia'))
