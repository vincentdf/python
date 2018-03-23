#!/usr/bin/python
# coding=utf-8
"""
将一个数组逆序输出。
"""

l=[1,2,3,4,5,66,7,8,9]
l2=[]
for i in range(len(l)-1,-1,-1):
    l2.append(l[i])
print l2
l.reverse()    ##函数
print l