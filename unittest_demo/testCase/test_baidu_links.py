#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/1/14/0014 13:52
# @Author  : Hython.com
# @File    : test_baidu_links.py.py
from selenium import webdriver
import unittest


class BaiduLink(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Python\webdrive\chromedriver.exe')
        self.driver.get('http://www.baidu.com/')

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        '''toppage -> 贴吧 page'''
        self.driver.find_element_by_link_text('贴吧').click()
        self.assertEqual(self.driver.current_url, 'https://tieba.baidu.com/index.html')

    def test_baidu_map(self):
        '''toppage -> 地图 page'''
        self.driver.find_element_by_link_text('地图').click()
        self.assertEqual(self.driver.current_url, 'https://map.baidu.com/')


if __name__ == '__main__':
    unittest.main(verbosity=2)
