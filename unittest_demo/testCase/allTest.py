#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/1/14/0014 13:53
# @Author  : Hython.com
# @File    : allTest.py
import unittest
import os


def allTest():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite


def run():
    unittest.TextTestRunner(verbosity=2).run(allTest())


if __name__ == '__main__':
    run()
