# -*- coding: utf-8 -*-
import pytest
import allure
import os
import logging.config
#
#
#

'''
1、Features定制详解
Feature: 标注主要功能模块
Story: 标注Features功能模块下的分支功能
Severity: 标注测试用例的重要级别
Step: 标注测试用例的重要步骤
Issue和TestCase: 标注Issue、Case，可加入URL

4 、Severity定制详解

Allure中对严重级别的定义：
1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
2、 Critical级别：临界缺陷（ 功能点缺失）
3、 Normal级别：普通缺陷（数值计算错误）
4、 Minor级别：次要缺陷（界面错误与UI需求不符）
5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
'''
def func(x):
    return x + 1


@allure.feature('test_answer_01')
def test_answer_01():
    assert func(3) == 4


@allure.feature('test_answer_02')
def test_answer_02():
    assert func(5) == 6


@allure.feature('test_answer_03')
def test_answer_03():
    assert func(7) == 5


@allure.feature('test_answer_04')
def test_answer_04():
    assert func(8) == 9


@allure.feature('test_answer_05')
def test_answer_05():
    assert func(3) == 5

def command_line():
    cmd_path=r'F:\mrbao_python\Pytest'

    f=os.popen("allure generate report/ -o report/html")
    rizhi=f.read()
    logging.info(rizhi)
if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report'])
    command_line()
    # pytest.main(['allure generate report/ -o report/html'])
    #pytest.main()

