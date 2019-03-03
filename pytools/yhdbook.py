#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/3/0003 13:29
# @Author  : Hython.com
# @File    : yhdbook.py
from requests import get
from lxml import html


def spider(sn, books=[]):
    """爬取一号店图书信息"""
    url = f"http://search.yhd.com/c0-0/k{sn}/"
    # 获取html
    html_data = get(url).text
    # 构建xpath对象
    selector = html.fromstring(html_data)
    # 取得书籍列表
    ul_list = selector.xpath('//div[@id="itemSearchList"]/div')
    # print(len(ul_list))
    # 解析书籍数据
    for li in ul_list:
        title = li.xpath('div/p[@class="proName clearfix"]/a/@title')
        price = li.xpath('div/p[@class="proPrice"]/em/@yhdprice')
        link = li.xpath('div/p[@class="proName clearfix"]/a/@href')
        store = li.xpath('div/p[@class="searh_shop_storeName storeName limit_width"]/a/@title')

        books.append({
            'title': title[0],
            'price': price[0],
            'link': link[0],
            'store': store
        })
    print(books)


if __name__ == '__main__':
    spider('9787115428028')
