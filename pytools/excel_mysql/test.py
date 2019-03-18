#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/19/0019 0:42
# @Author  : Hython.com
# @File    : test.py
import MySQLdb

def get_conn():
    """获取mysql连接"""
    conn = MySQLdb.connect(host='localhost',
                           db='user_grade',
                           user='root',
                           password='root',
                           charset='utf8')
    return conn

conn = get_conn()
cursor = conn.cursor()
sql = 'INSERT INTO `score`(`year`,`max`,`avg`) VALUES(2015,500,470)'
cursor.execute(sql)
conn.autocommit(True)
print(conn)