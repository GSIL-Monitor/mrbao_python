import yaml
import os
import re
import aiofiles

async def yaml_load(dir='',file=''):
    '''
    异步读取yaml文件，并转义其中特殊值
    :param dir: 目录名
    :param file: 文件名
    :return: 
    '''
    if dir:
        file=os.path.join(dir,file)
    async with aiofiles.open(file,'r',encoding='utf-8',errors='ignore') as f:
        data=await f.read()

    data=yaml.load(data)
    # 匹配函数调用形式的语法
    pattern_function = re.compile(r'^\${([A-Za-z_]+\w*\(.*\))}$')
    pattern_function2 = re.compile(r'^\${(.*)}$')
    # 匹配取默认值的语法
    pattern_function3 = re.compile(r'^\$\((.*)\)$')

def my_iter(data):