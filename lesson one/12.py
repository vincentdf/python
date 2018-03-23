#!/usr/bin/python
# coding=utf-8

"""
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""
leap=0
d=int(raw_input(("查找___以内的素数")))
for i in range (1,d):
    for j in range (2,i):
        if i%j==0:
            break
    else:
        print "%12ld"%i,
        leap+=1
        if leap%5==0:
           print""

print "\n\n总共有%d个素数"%leap