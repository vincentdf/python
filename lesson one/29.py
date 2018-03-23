#!/usr/bin/python
# coding=utf-8
"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""

x=raw_input("输入一个正整数")
n=len(x)

def op(n):
    for i in range(n):
        print x[n-1-i],
print "x是%d位数"%n
op(n)
