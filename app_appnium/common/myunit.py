import unittest

from common.appnium_desired import appnium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):

    def setUp(self):
        logging.info('---- setup ----')
        self.driver=appnium_desired()

    def tearDown(self):
        logging.info('---- tearDown ----')
        sleep(5)
        self.driver.close_app()
