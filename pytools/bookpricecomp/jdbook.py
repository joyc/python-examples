#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/2/0002 20:19
# @Author  : Hython.com
# @File    : jdbook.py
import requests
from lxml import html


def spider(sn, books=[]):
    """爬取京东图书数据"""
    url = 'https://search.jd.com/Search'
    # 需要设置header模拟用户
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3710.0 Safari/537.36',
        'DNT': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': 'https://www.jd.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ja-JP,ja;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6,en;q=0.5',
    }
    params = (
        ('keyword', sn),
        ('enc', 'utf-8^'),
        ('suggest', '1.his.0.0^'),
        ('wq', '^'),
        ('pvid', '333b3b60534d4c78828f91757c600b0b'),
    )
    r = requests.get(url, headers=headers, params=params)
    r.encoding = 'utf-8'
    html_data = r.text
    # 获取xpath对象
    selector = html.fromstring(html_data)
    # 图书获取列表
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    # 解析列表内容
    for li in ul_list:
        title = li.xpath('div/div[@class="p-name"]/a/@title')  # 标题
        link = li.xpath('div/div[@class="p-name"]/a/@href')  # 链接
        price = li.xpath('div/div[@class="p-price"]/strong/i/text()')  # 价格
        store = li.xpath('div//a[@class="curr-shop"]/@title')  # 店铺
        store_n = [store[0] if store else '第三方商家']  # 店铺过滤电子书
        books.append({
            'title': title[0],
            'price': price[0],
            'link': link[0],
            'store': store_n[0]
        })
    print(books)


if __name__ == '__main__':
    spider('9787115428028')
