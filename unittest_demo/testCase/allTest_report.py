#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/1/14/0014 13:53
# @Author  : Hython.com
# @File    : allTest.py
import unittest
import os
import HTMLTestRunner
import time


def all_tests():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite


def get_time():
    return time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))


def run():
    fp = os.path.join(os.path.dirname(__file__), 'report', get_time()+'testReport.html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fp, 'wb'),
        title='自动化测试报告',
        description='自动化测试报告详细').run(all_tests())


if __name__ == '__main__':
    run()
