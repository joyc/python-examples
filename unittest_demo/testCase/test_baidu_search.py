#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/1/14/0014 13:53
# @Author  : Hython.com
# @File    : test_google_search.py
from selenium import webdriver
import unittest


class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Python\webdrive\chromedriver.exe')
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_baidu_so_enable(self):
        '''toppage -> can input keywords'''
        search = self.driver.find_element_by_id('kw')
        self.assertTrue(search.is_enabled())


    def test_baidu_search(self):
        """toppage -> can search"""
        search = self.driver.find_element_by_id('kw')
        search.send_keys('unittest')
        self.driver.find_element_by_id('su').click()
        print(search.get_attribute('value'))
        self.assertEqual(search.get_attribute('value'), 'unittest')


if __name__ == '__main__':
    unittest.main(verbosity=2)
