#!/usr/bin/python
# coding=utf-8
"""
打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *
"""
"""i=1
j=1
while i <=(n+1)/2+1:
    print " "*((n+1)/2-j),
    print "*"*i
    i=i+2
    j=j+1
    if i>(n+1)/2+1:
        break
while i <=n:
    print " "*((n+1)/2-j),
    print "*"*i
    i=i-2
    j = j - 1
    if i <1:
        break
"""
i=1
n=int(raw_input("请输入行数（奇数）"))
k=1
j = 1
if n%2!=1:
    exit("请输入奇数")
for i in  range (1,(n+1),2):
    print " "*((n+1)/2-i),
    print "*"*k
    k=k+2
    i=i+1
for k in range((n-2),0,-2):
    print " " * (j),
    print "*" * k
    i=i-1
    j=j+1
