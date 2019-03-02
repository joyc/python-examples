#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/2/0002 19:34
# @Author  : Hython.com
# @File    : dangdangbook.py
import requests
from lxml import html


def spider(sn):
    """爬取当当网图书数据"""
    url = f"http://search.dangdang.com/?key={sn}&act=input"
    # 获取html
    html_data = requests.get(url).text
    # xpath对象
    selector = html.fromstring(html_data)
    # 获取图书列表
    ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')
    print(len(ul_list))
    for li in ul_list:
        title = li.xpath('a/@title')    # 书名
        link = li.xpath('a/@href')    # 链接
        price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')    # 价格
        store = li.xpath('p[@class="search_shangjia"]/a/text()')
        print(title[0])
        print(link[0])
        print(price[0].replace('¥',''))
        print(store[0] if store else '当当自营')


if __name__ == '__main__':
    sn = '9787115428028'
    spider(sn)
