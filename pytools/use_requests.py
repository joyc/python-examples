#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/2/0002 19:03
# @Author  : Hython.com
# @File    : use_requests.py
import requests

def get_book():
    """获取书本信息"""
    url = "http://search.dangdang.com/"
    rest = requests.get(url, params={
        'key': '9787115428028',
        'act':'input'
    })
    print(rest.text)
    print(rest.status_code)
    print(rest.encoding)


if __name__ == '__main__':
    get_book()
