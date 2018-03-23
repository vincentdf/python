#!/usr/bin/python
# coding=utf-8
"""
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""

def outpu(s,l):
    for i in range(l):
        l=l-1
        print s[l],
s=raw_input("输入字符")
l=len(s)
outpu(s,l)