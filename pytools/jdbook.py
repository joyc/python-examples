#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/2/0002 20:19
# @Author  : Hython.com
# @File    : jdbook.py
import requests
from lxml import html


def spider(sn):
    """爬取京东图书数据"""
    url = f"https://search.jd.com/Search?keyword={sn}"
    resp = requests.get(url)
    # resp.encoding = 'utf-8'
    html_data = resp.text
    selector = html.fromstring(html_data)
    print(html_data)


if __name__ == '__main__':
    sn = '9787115428028'
    spider(sn)
