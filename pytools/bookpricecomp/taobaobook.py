#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/3/0003 14:14
# @Author  : Hython.com
# @File    : taobaobook.py
# def spider(sn, books=[]):
#     """爬取淘宝图书信息"""


# !/usr/bin/python3
# -*- coding:utf-8 -*-
__auther__ = 'gavin'

import requests
import re
import json
import time
from hashlib import md5


# 数据
DATA = []

t = time.localtime()
# 搜索关键字
find_word = 'python'
# 参数
find_arg = {
    'q': find_word,
    'initiative_id': 'staobaoz_%s%02d%02d' % (t[0], t[1], t[2])
}
# 搜索页面url
# https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180305&ie=utf8
first_url = "https://s.taobao.com/search?imgfile=&js=1&stats_click=search_radio_all%3A1&ie=utf8"

# url = 'https://s.taobao.com/search?q=python&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
# 发送请求
response = requests.get(first_url, params=find_arg)  # response.json()方法同json.loads(response.text)
html = response.text
print(html)

# 提取，筛选，清洗数据
content = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html, re.S)[0]  # 正则表达式处理的结果是一个列表，取第一个元素（字典）

# 格式化，将json格式的字符串切片
content = content.strip()[:-1]
# 将json转为dict
content = json.loads(content)

# 借助json在线解析分析，取dict里的具体data
data_list = content['mods']['itemlist']['data']['auctions']

# 提取数据
for item in data_list:
    temp = {
        'title': item['title'],
        'view_price': item['view_price'],
        'view_sales': item['view_sales'],
        'view_fee': '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if item['shopcard']['isTmall'] else '否',
        'area': item['item_loc'],
        'name': item['nick'],
        'detail_url': item['detail_url'],
    }
    DATA.append(temp)

print(len(DATA))  # 36 首页有12条异步加载的数据 ，应该是48
