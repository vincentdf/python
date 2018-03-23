#!/usr/bin//python
# coding=utf-8
"""
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""

x=int(raw_input("插入一个数\n"))
l=[1,4,6,9,13,16,19,28,40,100]
print "原数列\n",l
l.append(x)
l.sort()
print "插入后的数列\n",l
