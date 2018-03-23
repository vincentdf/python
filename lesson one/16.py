#!/usr/bin/python
# coding=utf-8

"""
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
"""

import datetime
print datetime.date.today().strftime("%d/%m/%Y")
print datetime.date.today().strftime("%Y/%m/%d")
print datetime.date.today().strftime("%m/%d/%Y")
