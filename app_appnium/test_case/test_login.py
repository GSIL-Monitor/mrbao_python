import unittest

from common.appnium_desired import appnium_desired
from businessView.loginView import Loginview
from common.myunit import StartEnd
import logging

class TestLogin(StartEnd):

    def test_login(self):
        logging.info('----test_login----')
        I=Loginview(self.driver)
        I.login_action('18621512473')


if __name__ == '__main__':
    unittest.main()