# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'd:\Python_study\PYREQUESTS\baseView')
sys.path.append(r'd:\Python_study\PYREQUESTS\common')
sys.path.append(r'd:\Python_study\PYREQUESTS\config')
import unittest
import logging.config

log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('------TEST START------')

    def tearDown(self):
        logging.info('------TEST END------')