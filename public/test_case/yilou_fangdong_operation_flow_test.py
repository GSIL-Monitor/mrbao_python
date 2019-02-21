# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\config')
sys.path.append(r'd:\Python_study\PYREQUESTS\business')
from startEnd import StartEnd
from fuangyuan_parameters import FuanYuan_Parameters
import logging.config
import unittest
log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

class Test_Operation_Flow(StartEnd,FuanYuan_Parameters):
    '''创建合租房'''