#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/16/0016 19:13
# @Author  : Hython.com
# @File    : spider_ook.py
from ddbook import spider as dd
from jdbook import spider as jd
from yhdbook import spider as yhd


def main(sn):
    """图书比较"""
    book_list = []

    print('当当网图书数据爬完了')
    dd(sn, book_list)
    print('一号店图书数据爬完了')
    yhd(sn, book_list)
    print('京东网图书数据爬完了')
    jd(sn, book_list)
    # 打印所有数据列表
    for book in book_list:
        print(book)
    print("-----开始排序-----")
    # 排序数据
    book_list = sorted(book_list, key=lambda item: float(item["price"]), reverse=True)
    for book in book_list:
        print(book)


if __name__ == '__main__':
    sn = input("请输入图书ISBN编号: ")
    main(sn)
