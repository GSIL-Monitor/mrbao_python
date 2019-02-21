import yaml
import os
import re
import logging.config
import aiofiles
import asyncio
import json
import time

con_log = r'F:\mrbao_python\Xiaoxiangyoupin\xiaoxiang_peizhi\logging.conf'
logging.config.fileConfig(con_log)


async def get_path_yaml(yaml_path):
    '''
    根据路径去查用例
    :param yaml_path: 
    :param yaml_name: 
    :return: 
    '''
    case_list=[]#创建用例list
    logging.info("正在执行%s" % get_path_yaml.__name__)
    if yaml_path != None and isinstance(yaml_path, list):
        for file_path in yaml_path:
            logging.info("当前打开地址为%s" % file_path)
            async with aiofiles.open(file_path, 'r', encoding='utf-8') as stream:
                shuju_name = await stream.read()#读取file_path文件中的内容
                shuju =  yaml.load(shuju_name)#序列化
                stream.close()
                for case in shuju:
                    case_list.append(shuju[case])
        return case_list



async def get_yaml(wenjianming, content_name, yaml_name=''):
    '''
    异步读取
    :return: 
    '''
    logging.info("正在执行%s" % get_yaml.__name__)
    yaml_path = os.path.dirname(os.path.dirname(__file__))
    yaml_path = yaml_path + "/" + wenjianming + "/" + content_name
    logging.info("打开地址为%s" % yaml_path)

    async with aiofiles.open(yaml_path, 'r', encoding='utf-8') as stream:
        shuju_name = await stream.read()
        if yaml_name == '':
            shuju = yaml.load(shuju_name)
            stream.close()

            return shuju
        else:
            shuju_name = yaml.load(shuju_name)
            shuju = shuju_name[yaml_name]
            stream.close()
            return shuju


def start_async(func):
    '''
    启动携程
    :param func: 传入方法
    :return: 
    '''
    logging.info("正在执行%s" % start_async.__name__)
    loop = asyncio.get_event_loop()  # 创建事件循环
    semaphore=asyncio.Semaphore()
     # 创建携程对象
    task = asyncio.ensure_future(func)  # 创建任务
    try:
        loop.run_until_complete(task)
    finally:
        loop.close()
    return task.result()


def check_case_address(data, wenjianming):
    '''
    根据接口名获取用例地址
    :param keys: 
    :param wenjianming: 
    :return: 
    '''
    logging.info("正在执行%s"%check_case_address.__name__)
    case_address = []
    wenjian_list = []
    if isinstance(data, dict):#
        keys = data.keys()#获取data字典中的key
        keys = list(keys)#转换成list
        if type(keys) is list:#判断keys是否为list
            yaml_path = os.path.dirname(os.path.dirname(__file__))#获取上一级目录
            # for key in keys:
            #     yaml_path = os.path.join(yaml_path, key+'.yaml')
            #     case_address.append(yaml_path)

            yaml_path = yaml_path + "/" + wenjianming + "/"
            file = os.listdir(yaml_path)#打印yaml_path下的文件
            for filename in file:
                wenjian_path=os.path.join(yaml_path,filename)
                wenjian_list.append(wenjian_path)#把yaml_path下的文件路径放入wenjian_list中
            for key in keys:
                filepath = yaml_path + key + '.yaml'
                logging.info("%s文件地址是%s"%(key,filepath))
                if filepath in wenjian_list:#判断是否在wenjian_list中
                    case_address.append(filepath)#是就加入case_address中
                else:
                    logging.info("%s文件不在wenjian_list中"%key)
            return case_address


# 读取yaml文件
def get_peizhi(wenjianming, content_name='', yaml_name=''):
    '''
    :param yaml_name: 模块名
    :param content_name: yaml文件名
    :return: 模块内容
    '''

    yaml_path = os.path.dirname(os.path.dirname(__file__))
    yaml_path = yaml_path + "/" + wenjianming + "/" + content_name
    logging.info("打开地址为%s" % yaml_path)

    with open(yaml_path, 'r', encoding='utf-8') as stream:
        shuju_name = yaml.load(stream)
        if yaml_name == '':
            return shuju_name
        else:

            shuju = shuju_name[yaml_name]
            stream.close()
            return shuju


def write_data(wenjianming, content_name, yaml_name, yaml_data):
    '''写入数据'''
    yaml_name_ = {}
    yaml_path = os.path.dirname(os.path.dirname(__file__))
    yaml_path = yaml_path + "\\" + wenjianming + "\\" + content_name

    logging.info("打开地址为%s" % yaml_path)
    result = open(yaml_path, 'r', encoding='utf-8')
    shuju_name = yaml.load(result)  # 获取yaml文件父类
    logging.info(shuju_name)
    with open(yaml_path, 'w', encoding='utf-8') as F:
        yaml_name_[yaml_name] = yaml_data
        logging.info("%s正在存储中" % yaml_data)
        yaml.dump(yaml_name_, F, default_flow_style=False)
        '''
        yaml.dump(dataMap,default_flow_style=False,stream=f,indent=4,encoding='utf-8',allow_unicode=True)
        default_flow_style=False 大概就是不要什么风格之类的给我最简单的方式显示就行了 
        encodeing=’utf-8‘ 设置一下编码 
        allow_unicode=True 上传时候是不是转化成unnicode形式 
        indent=4 这个我也不知道

        '''
        logging.info("token存储成功......")
        F.close()


# 在目录中查找文件
wenjian_path = r'F:\Autotest\xiaoxiangyoupin'
global path_name  # 设置全局变量获取值


def check_wenjian(wenjian_path, wenjian_name):
    '''
    :param wenjian_path: 目录地址
    :param wenjian_name: 需要查找的文件名
    :return: 
    '''
    wenjian_list = []
    filelist = os.listdir(wenjian_path)  # 查看目录下目录集合

    for filename in filelist:
        filepath = os.path.join(wenjian_path, filename)

        if os.path.isdir(filepath) == False:
            wenjian_list.append(filepath)

            for wenjian_content in wenjian_list:
                if re.search(wenjian_name, wenjian_content):
                    path_name = wenjian_content
                    return path_name

        else:
            return check_wenjian(filepath, wenjian_name)


if __name__ == '__main__':
    # write_data(wenjianming='xiaoxiang_peizhi',yaml_name='token',yaml_data=123,content_name='xiaoxiangx_dapaijiangjia.yaml')
    coroutine = get_yaml(wenjianming='xiaoxiang_api', content_name='xiaoxiang_api_test.yaml', yaml_name='')
    a = start_async(coroutine)
    c = check_case_address(data=a, wenjianming='xiaoxiang_test_case')
    d = start_async(get_path_yaml(yaml_path=c))
    print(d)
