#!/usr/bin/python
# coding=utf-8
"""
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
def fiv(i):
    a=i/10000
    b=i%10000/1000
    c=i%1000/100
    d=i%100/10
    e=i%10
    if a==e and b==d:
        print i

for i in range (10000,100000):
    fiv(i)