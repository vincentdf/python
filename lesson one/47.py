#!/usr/bin/python
# coding=utf-8

"""
两个变量值互换。
"""
a=int(input("输入第一个数字a\n"))
b=int(input("输入第二个数字b\n"))
print "a=%d,b=%d"%(a,b)
def exchange(a,b):
    print "两个变量值互换。。。\n"
    a,b=b,a
    return a,b
print "交往后的值，a=%d，b=%d"%exchange(a,b)
