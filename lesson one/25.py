#!/usr/bin/python
# coding=utf-8
"""
题目：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
"""
n=20
s=0
x=range(1,n+1)
def op(x):
    r = 1
    for i in range(1,x+1):
        r=r*i
    return r
s= sum(map(op,x))
print s