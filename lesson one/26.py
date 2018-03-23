#!/usr/bin/python
# coding=utf-8

"""
题目：利用递归方法求5!。
"""
n=int(raw_input("n=\n"))
s=1
def m(n):
    s=1
    for i in range (1,n+1):
        s=s*i
    return s

"""for j in range (1,n+1):
    print "%d!=%d"%(j,m(j))
"""

print m(n)