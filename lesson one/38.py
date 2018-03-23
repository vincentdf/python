#!/usr/bin/python
# coding=utf-8
"""
求一个3*3矩阵主对角线元素之和。
"""
n=int(raw_input("___介矩阵"))
if n<=1:
    exit("请重新输入")
k=1
j=1
a=2
l=[]
for i in range(1,n**2+1):
    x=int(raw_input("输入第%d个数字"%i))
    if i==k:
        l.append(x)
        k=j*n+a
        j=j+1
        a=a+1
print sum(l)