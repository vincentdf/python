#!/usr/bin/python
# coding=utf-8

"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
n=100.0
x=10
m=0
M=[]
tour=[]
for i in range(1,x+1):
    if i==1:
        M.append(n)
    else:
        M.append(2*n)
    n=n/2
    tour.append(n)
print "zonggaodu:M={0}".format(sum(M))
print tour[x-1]
