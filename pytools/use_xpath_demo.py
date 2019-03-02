#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/2/0002 16:39
# @Author  : Hython.com
# @File    : use_xpath_demo.py
from lxml import html


def parse():
    """xpath提取html"""
    f = open('./static/index.html', 'r', encoding='utf-8')
    s = f.read()
    selector = html.fromstring(s)
    #h3标题
    h3 = selector.xpath('/html/body/h3/text()')
    print(h3[0])
    # 获取ul>li
    # ul = selector.xpath('/html/body/ul/li')
    ul = selector.xpath('//ul/li')
    for li in ul:
        print(li.xpath('text()')[0])

    #解析指定元素值
    ul2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')
    print(ul2[0])
    #解析a标签内容
    # a = selector.xpath('//div[@id="container"]/a/text()')
    a = selector.xpath('//div[@id="container"]/a')
    print(a[0].xpath('text()')[0])
    #href属性
    print(a[0].xpath('@href')[0])
    #获取第二个p标签的内容
    p = selector.xpath('//p[last()]/text()')
    print(p[0])
    f.close()


if __name__ == '__main__':
    parse()
