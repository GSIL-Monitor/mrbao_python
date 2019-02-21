# -*- coding: UTF-8 -*-

import unittest


class StartEnd(unittest.TestCase):
    def setUp(self):
        print('------TEST START------')

    def tearDown(self):
        print('------TEST END------')