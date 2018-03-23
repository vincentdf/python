#!/usr/bin/python
# coding=utf-8
"""
输入3个数a,b,c，按大小顺序输出。
"""
n1=int(raw_input("input one\n"))
n2=int(raw_input("input two\n"))
n3=int(raw_input("input three\n"))
def swap(a,b):
    return b,a
if n1<n2:n1,n2=swap(n1,n2)
if n1<n3:n1,n3=swap(n1,n3)
if n2<n3:n2,n3=swap(n2,n3)
print n1,n2,n3