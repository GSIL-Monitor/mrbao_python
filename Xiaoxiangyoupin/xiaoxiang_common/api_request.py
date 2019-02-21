import requests
import json
import asyncio
import aiohttp


def request(request_type, request_method):
    '''
    web和app请求类型
    :param request_type: 1为app请求   2为异步请求
    :param request_method: 1为get请求  2为post请求
    :return: 
    '''
    if request_type == 1:
        if request_method == 1:
            request_post(base_url, header, dict_data)
        if request_method == 2:
            request_get(base_url, header, dict_data)
    if request_type == 2:
        if request_method == 1:
            asyc_post(base_url, dict_data, header)
        if request_method == 2:
            asyc_post(base_url, dict_data, header)


def request_post(base_url, header, dict_data):
    '''
    :param base_url: 请求地址
    :param header: 请求头
    :param dict_data: 请求参数
    :return: 
    '''
    response = requests.post(base_url, headers=header, data=dict_data, verify=False)
    response_result = response.json()
    return response_result


def request_get(base_url, header, dict_data):
    '''
    :param base_url: 请求地址
    :param header: 请求头
    :param dict_data: 请求参数
    :return: 
    '''
    response = requests.post(base_url, headers=header, params=dict_data)
    response_result = response.json()
    return response_result, response.status_code


async def asyc_post(base_url, dict_data, header):
    '''
    异步get请求
    :param base_url: 请求地址
    :param dict_data: 请求参数
    :param header: 请求头
    :return: 
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(url=base_url, params=dict_data, header=header) as request_result:
            res= await request_result.text()
            return {
                'response':res,
                'url':base_url,
                'params':dict_data
            }


async def asyc_get(base_url, dict_data, header):
    '''
    异步post请求
    :param base_url: 请求地址
    :param dict_data: 请求参数
    :param header: 
    :return: 
    '''
    async with aiohttp.ClientSession() as session:
        async with session.post(url=base_url, data=dict_data, header=header) as request_result:
            res = await request_result.text()
            return {
                'response': res,
                'url': base_url,
                'params': dict_data
            }


if __name__ == '__main__':
    header = {'Accept-Encoding': 'gzip,deflate',
              'Accept': 'application/json, text/plain, */*',
              'Content-Type': 'application/json;charset=UTF-8',
              }
    base_url = 'https://dev.xiaoxiangyoupin.com/v2/shoppingGuide/hotSearch/list'
    dict_data = {'pageNum': 1, 'searchKey': '9'}
    json_dict = json.dumps(dict_data, ensure_ascii=True)
    result = request_post(base_url=base_url, header=header, dict_data={})
    print(result[0])
    # jiexi_json(result_data=result[0], key_name='name')
    # jiexi_json(result_data=result[0], key_name='id')
