#! /usr/bin/python
# coding=utf-8

"""
比较大小
"""
if __name__=="__main__":
    a=int(input("输入第一个数字a\n"))
    b=int(input("输入第一个数字b\n"))
    if a>b:
        print "a>b"
    elif a<b:
        print "a<b"
    elif a==b:
        print "a=b"
    else:
        print "未知"

