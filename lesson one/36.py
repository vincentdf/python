#!/usr/bin/python
# coding=utf-8

"""
求100之内的素数。
"""
l=[]
n=int(raw_input("求___以内的素数\n"))
for i in range (2,n+1):
    for j in range (2,i):
        if i%j==0:
            break
    else:  #for else, 只要for循环没有从break中退出，则会执行else，如果在break中退出则不糊执行else。
        l.append(i)
for k in range(len(l)):
    print l[k],
    if k%10==0:
        print