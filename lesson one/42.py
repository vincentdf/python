#!/usr/bin/python
# coding=utf-8
"""
学习使用auto定义变量的用法。
"""
num=2
def autfunc():
    num=1
    print "num1=%d"%num
    num+=1
for i in range(3):
    print "num2=%d"%num
    num+=1
    autfunc()